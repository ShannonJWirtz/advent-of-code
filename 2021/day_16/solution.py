from functools import reduce

hex_to_bin_map = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}

def get_bin_from_hex(hexstring):
    return ''.join(hex_to_bin_map[hex_digit] for hex_digit in hexstring)

def get_input_binstring(filename):
    with open(filename) as f:
        return get_bin_from_hex(f.read().strip())


def get_next_packet_metadata(binstring):
    metadata = dict()
    metadata['version'] = int(binstring[:3],2)
    metadata['type'] = int(binstring[3:6],2)

    if metadata['type'] != 4:
        metadata['length_type'] = int(binstring[6],2)
        if metadata['length_type'] == 1:
            metadata['length'] = int(binstring[7:18],2)
        else:
            metadata['length'] = int(binstring[7:22],2)

    return metadata


def split_literal(binstring):

    literal_chunk_count = binstring[::5].index('0') + 1

    value = int(''.join(binstring[1+i:5+i] for i in range(0, literal_chunk_count*5,5)),2)

    return value, binstring[(literal_chunk_count)*5:]


def parse_packets(binstring):
    metadata = get_next_packet_metadata(binstring)

    packet_data = dict(metadata=metadata)

    if metadata['type'] == 4:
        binstring = binstring[6:]
        packet_data['value'], binstring = split_literal(binstring)
        return packet_data, binstring
    else:
        if metadata['length_type'] == 1:
            binstring = binstring[18:]

            packet_data['value'] = []
            while len(packet_data['value']) < metadata['length']:
                value_to_add, binstring = parse_packets(binstring)
                packet_data['value'].append(value_to_add)

            return packet_data, binstring
        else:
            remaining_binstring  = binstring[22+metadata['length']:]
            binstring = binstring[22:22+metadata['length']]

            packet_data['value'] = []
            while len(binstring) > 0:
                value_to_add, binstring = parse_packets(binstring)
                packet_data['value'].append(value_to_add)

            return packet_data, remaining_binstring


def get_version_sum_from_parsed_packets(parsed_packets):

    version = parsed_packets['metadata']['version']

    if type(parsed_packets['value']) == int:
        return version

    return version + sum(get_version_sum_from_parsed_packets(value) for value in parsed_packets['value'])

def get_version_sum_from_file(filename):
    parsed_packets, _ = parse_packets(get_input_binstring(filename))

    return get_version_sum_from_parsed_packets(parsed_packets)


type_func_lookup = {
    0: lambda x, y: x + y,
    1: lambda x, y: x * y,
    2: lambda x, y: min(x,y),
    3: lambda x, y: max(x,y),
    5: lambda x, y: x > y,
    6: lambda x, y: x < y,
    7: lambda x, y: x == y
}

def get_evaluation_from_parsed_packets(parsed_packets):

    if type(parsed_packets['value']) == int:
        return parsed_packets['value']

    aggfunc = type_func_lookup[parsed_packets['metadata']['type']]

    return reduce(aggfunc, [get_evaluation_from_parsed_packets(value) for value in parsed_packets['value']])

def get_evaluation_from_file(filename):
    parsed_packets, _ = parse_packets(get_input_binstring(filename))

    return get_evaluation_from_parsed_packets(parsed_packets)


if __name__ == '__main__':
    print('First answer is:', get_version_sum_from_file('input.txt'))
    print('Second answer is:', get_evaluation_from_file('input.txt'))
