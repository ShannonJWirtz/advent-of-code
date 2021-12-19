#This took me all day and is in no way optimised.
#Takes ~5 minutes to run on a macbook pro. Too long.
#(probably minor?) optimisation: calculate the unique yaw, pitch, roll combos upfront, rather than filtering down every time.
#Losing momentum on writing tests, which is possibly why this took me too long: loads of errors, felt like a drag to solve them all.
import re
import numpy as np
from collections import defaultdict
from itertools import combinations, product, chain
from copy import copy, deepcopy

def get_inputs(filename):
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    scanners = {0: []}
    current_scanner = 0
    while len(lines) > 0:
        line = lines.pop(0)
        if len(line) == 0:
            continue
        elif line[:3] == '---':
            scanner = int(re.sub(r'[^0-9]', '', line))
            scanners[scanner] = []
            current_scanner = scanner
        elif line[0] in '0123456789-':
            scanners[current_scanner].append(eval('('+line+')'))

    return scanners

def get_rotation(point, yaw_cos, yaw_sin, pitch_cos, pitch_sin, roll_cos, roll_sin):
    x, y, z = point
    xr = yaw_cos*pitch_cos*x + (yaw_cos*pitch_sin*roll_sin-yaw_sin*roll_cos)*y + (yaw_cos*pitch_sin*roll_cos+yaw_sin*roll_sin)*z
    yr = yaw_sin*pitch_cos*x + (yaw_sin*pitch_sin*roll_sin+yaw_cos*roll_cos)*y + (yaw_sin*pitch_sin*roll_cos-yaw_cos*roll_sin)*z
    zr = -pitch_sin*x + pitch_cos*roll_sin*y + pitch_cos*roll_cos*z
    # print((x,y,z), 'to', (xr, yr, zr), 'after', [(yaw_cos, yaw_sin), (pitch_cos, pitch_sin), (roll_cos, roll_sin)])
    return (xr, yr, zr)

def get_rotation_of_scan(scan, yaw_cos, yaw_sin, pitch_cos, pitch_sin, roll_cos, roll_sin):
    return [get_rotation(point, yaw_cos, yaw_sin, pitch_cos, pitch_sin, roll_cos, roll_sin) for point in scan]

cos_sin_90deg_pairs = [(1,0), (0,1), (-1,0), (0,-1)]
rev_cos_sin_90deg_pairs_map = {
    (1,0): (1,0), (0,1): (0,-1), (-1,0): (-1,0), (0,-1): (0,1)
}
def get_rotations_of_scan(scan):
    new_scans = dict()
    for yaw_cos, yaw_sin in cos_sin_90deg_pairs:
        for pitch_cos, pitch_sin in cos_sin_90deg_pairs:
            for roll_cos, roll_sin in cos_sin_90deg_pairs:
                new_scan = get_rotation_of_scan(scan, yaw_cos, yaw_sin, pitch_cos, pitch_sin, roll_cos, roll_sin)
                if new_scan not in new_scans.values():
                    new_scans[(yaw_cos, yaw_sin, pitch_cos, pitch_sin, roll_cos, roll_sin)] = new_scan

    return new_scans

def get_reverse_rotation(rot):
    return rev_cos_sin_90deg_pairs_map[rot[0:2]] +\
        rev_cos_sin_90deg_pairs_map[rot[2:4]] +\
        rev_cos_sin_90deg_pairs_map[rot[4:6]]


def add_tuples(tup1, tup2, tup2_multiplier = 1):
    return tuple(tup1[i] + pt2 * tup2_multiplier for i, pt2 in enumerate(tup2))

def check_overlap_of_scans(scan1, scan2):
    scan2_newscans = get_rotations_of_scan(scan2)
    max_count, max_overlaps, max_rot, max_adjustment = 0, [], tuple(), tuple()
    for rot, scan2_newscan in scan2_newscans.items():
        rot_max_count, rot_max_overlaps, rot_max_adjustment = 0, [], (0,0,0)
        k = 0
        for point1 in scan1:
            for point2 in scan2_newscan:
                #assume point1 is point2, adjust all points in scan2_newscan2 to be in scan1's coordinate grid
                adjustment = add_tuples(point1, point2, -1)
                tmp_scan2 = [add_tuples(pt, adjustment) for pt in scan2_newscan]
                overlaps = [i for i, pt in enumerate(tmp_scan2) if pt in scan1]
                if len(overlaps) > rot_max_count:
                    rot_max_count = len(overlaps)
                    rot_max_overlaps = overlaps
                    rot_max_adjustment = adjustment
            k+=1
        if rot_max_count > max_count:
            max_count = rot_max_count
            max_overlaps = rot_max_overlaps
            max_rot = rot
            max_adjustment = rot_max_adjustment
    return max_count, max_overlaps, max_rot, max_adjustment

def get_overlaps(scans):
    overlaps = defaultdict(list)
    for i in range(len(scans) - 1):
        for j in range(i+1, len(scans)):
            max_count, max_overlaps, max_rot, max_adjustment = check_overlap_of_scans(scans[i], scans[j])
            if max_count >= 12:
                overlaps[(i, j)].append((max_count, max_overlaps, max_rot, max_adjustment))
        print(i, 'done!!')
    return dict(overlaps)



def rotate_adjust_scan(scan, rot, adj, rot_first=True):
    if rot_first:
        return [add_tuples(point, adj) for point in get_rotation_of_scan(scan, *rot)]
    else:
        return get_rotation_of_scan([add_tuples(point, adj) for point in scan], *rot)


def get_graph_from_zero(edges):
    edges = set(edges)
    layers = [[]]
    first_layer_nodes = [0]
    lm = 0
    while len(edges) > 0:
        lm += 1
        edges_tmp = copy(edges)
        for edge in edges:
            if edge[0] in first_layer_nodes:
                layers[0].append((edge, 1))
                edges_tmp.remove(edge)
            if edge[1] in first_layer_nodes:
                layers[0].append((edge, -1))
                edges_tmp.remove(edge)
        edges = edges_tmp
        if len(edges) > 0:
            first_layer_nodes = [ item[0][1] if item[1] == 1 else item[0][0] for item in layers[0]]
            layers.insert(0, [])
    return layers

def get_reverse_adjustment(tup, rot):
    rev_rot = get_reverse_rotation(rot)
    print(get_rotation(tup, *rev_rot))
    return get_rotation(get_rotation(tup, *rev_rot), *rev_rot)

def get_reverse_tuple(tup):
    return tuple(-i for i in tup)


def get_coords(inputs, overlaps, actual_inputs):
    graph_from_zero = get_graph_from_zero(overlaps.keys())
    inputs_copy = deepcopy(inputs)
    overlaps = deepcopy(overlaps)

    for layer in graph_from_zero:
        for item in layer:
            if item[1] == 1:
                inputs_copy[item[0][0]].extend( rotate_adjust_scan(inputs_copy[item[0][1]], overlaps[item[0]][0][2], overlaps[item[0]][0][3]) )
                inputs_copy[item[0][1]] = []
            if item[1] == -1:
                overlap = check_overlap_of_scans(actual_inputs[item[0][1]], actual_inputs[item[0][0]]) # Couldn't get any inverse rotations + translations to work, so recalculating....
                inputs_copy[item[0][1]].extend( rotate_adjust_scan(inputs_copy[item[0][0]], overlap[2], overlap[3]) )
                inputs_copy[item[0][0]] = []

    return inputs_copy

def part2(inputs, overlaps):
    print('graph',get_graph_from_zero(overlaps.keys()))
    scanners = {k: [(0,0,0)] for k in inputs.keys()}
    coords = set(get_coords(scanners, overlaps, inputs)[0])
    print('part2 coords set len', len(coords), coords)
    print('First Answer calc is:', sum(len(k) for k in inputs.values()) - sum(val[0][0] for val in overlaps.values()))
    c = get_coords(inputs, overlaps, inputs)
    print('part2 coords v2', len(set(c[0])))
    print('dadadada', [(k, len(val)) for k,val in c.items()])
    return max(
        sum(abs(pt1[i] - pt2[i]) for i in range(len(pt1))) for pt1, pt2 in combinations(coords,2)
        )


if __name__ == '__main__':
    t = get_inputs('input.txt')
    o = get_overlaps(t)
    print('First Answer is:', sum(len(k) for k in t.values()) - sum(val[0][0] for val in o.values()))
    print('Second Answer is:', part2(t, o))
