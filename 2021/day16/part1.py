from math import prod
from operator import eq, gt, lt


def evaluate_expression(transmission):
    n = len(transmission)

    def bits_to_int(l):
        return int("".join(l), 2)

    def parse_packet(l, r, sc):
        if r - l < 8 or sc == 0:
            return l, [], 0
        vsum = 0
        version = bits_to_int(transmission[l : l + 3])
        vsum += version
        l += 3
        type_id = bits_to_int(transmission[l : l + 3])
        l += 3
        values = []
        if type_id == 4:
            value_bits = []
            while l < n:
                value_bits += transmission[l + 1 : l + 5]
                is_last_group = transmission[l] == "0"
                l += 5
                if is_last_group:
                    break
            value = bits_to_int(value_bits)
            values.append(value)
        else:
            length_type_id = int(transmission[l])
            l += 1
            total_length = subpacket_count = None
            if length_type_id:
                subpacket_count = bits_to_int(transmission[l : l + 11])
                l += 11
            else:
                total_length = bits_to_int(transmission[l : l + 15])
                l += 15
            l, vals, ver = parse_packet(
                l,
                l + total_length if total_length else n,
                subpacket_count if subpacket_count else n,
            )
            type_id_to_func = {
                0: sum,
                1: prod,
                2: min,
                3: max,
                5: lambda x: gt(*x),
                6: lambda x: lt(*x),
                7: lambda x: eq(*x),
            }
            func = type_id_to_func[type_id]
            values.append(func(reversed(vals)))
            vsum += ver
        l, vals, ver = parse_packet(l, r, sc - 1)
        return l, vals + values, vsum + ver

    return parse_packet(0, n, n)
