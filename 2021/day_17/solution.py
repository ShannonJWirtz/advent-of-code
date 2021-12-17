from collections import defaultdict

def get_x_min_velocity(x_min):
    furthest_point = 0
    i = 0
    while furthest_point < x_min:
        i += 1
        furthest_point = int(i * (i + 1) / 2)

    return i


def check_velocities(x,y,s):
    velocities = [(max(x-i,0), (y-i)) for i in range(s)]
    print([(sum(x for x,y in velocities[:i]), sum(y for x,y in velocities[:i]))  for i in range(s)])


def check_velocities(vx,vy,x_min,x_max,y_min,y_max, with_highest_point):
    step = 0
    x, y = 0, 0
    highest_point = 0
    pos = [(0,0)]
    while x <= x_max and y >= y_min:
        x += vx
        y += vy
        pos.append((x,y))
        if y > highest_point:
            highest_point = y
        if x_min <= x <= x_max and y_min <= y <= y_max:
            return True, highest_point
        vx = vx - 1 if vx > 0 else 0
        vy = vy - 1
        step += 1
    return False, False


def get_highest_possible_point(x_min, x_max, y_min, y_max):
    highest_y = y_min
    for vx in range(get_x_min_velocity(x_min), x_max+1):
        for vy in range(y_min, -y_min):
            check, y = check_velocities(vx,vy,x_min,x_max,y_min,y_max, True)
            if check:
                highest_y = max(highest_y, y)
    return highest_y


def get_velocities(x_min, x_max, y_min, y_max):
    velocities = set()
    for vx in range(get_x_min_velocity(x_min), x_max+1):
        for vy in range(y_min, -y_min):
            check, y = check_velocities(vx,vy,x_min,x_max,y_min,y_max, True)
            if check:
                velocities.add((vx, vy))
    return velocities

def get_velocities_count(x_min, x_max, y_min, y_max):
    return len(get_velocities(x_min, x_max, y_min, y_max))


if __name__ == '__main__':
    print('First answer is:', get_highest_possible_point(56, 76, -162, -134))
    print('Second answer is:', get_velocities_count(56, 76, -162, -134))
