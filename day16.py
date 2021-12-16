from functools import reduce
from operator import mul
from typing import Tuple

from aocd import get_data, submit


def hex_to_bits(hex_str: str) -> str:
    return ''.join([bin(n)[2:].zfill(4) for n in [int(n, base=16) for n in hex_str]])


def take_bits(bits: str, num_bits: int) -> Tuple[str, str]:
    return bits[0:num_bits], bits[num_bits:]


def parse(bits):
    v, bits = take_bits(bits, 3)
    v = int(v, base=2)
    t, bits = take_bits(bits, 3)
    t = int(t, base=2)

    if t == 4:
        literal_payload = ''
        while True:
            chunk, bits = take_bits(bits, 5)
            more, payload_part = take_bits(chunk, 1)
            literal_payload += payload_part
            if more == '0':
                break
        literal_value = int(literal_payload, base=2)
        packet = (v, t, literal_value, [])
        return packet, bits

    i, bits = take_bits(bits, 1)
    if i == '0':
        l, bits = take_bits(bits, 15)
        subpackets_len = int(l, base=2)
        subpackets = []
        sub_bits, bits = take_bits(bits, subpackets_len)
        while sub_bits:
            s, sub_bits = parse(sub_bits)
            subpackets.append(s)
    else:
        l, bits = take_bits(bits, 11)
        subpackets_len = int(l, base=2)
        subpackets = []
        for _ in range(subpackets_len):
            s, bits = parse(bits)
            subpackets.append(s)

    packet = (v, t, None, subpackets)
    return packet, bits


def eval_packet(packet):
    v, t, literal_value, subpackets = packet
    subpacket_values = [eval_packet(packet) for packet in subpackets]
    match t:
        case 0:
            return sum(subpacket_values)
        case 1:
            return reduce(mul, subpacket_values, 1)
        case 2:
            return min(subpacket_values)
        case 3:
            return max(subpacket_values)
        case 4:
            return literal_value
        case 5:
            return 1 if subpacket_values[0] > subpacket_values[1] else 0
        case 6:
            return 1 if subpacket_values[0] < subpacket_values[1] else 0
        case 7:
            return 1 if subpacket_values[0] == subpacket_values[1] else 0


def part_a(data):
    bits = hex_to_bits(data)
    packet, *_ = parse(bits)

    packets = [packet]

    answer = 0

    while packets:
        v, t, _, subpackets = packets.pop(0)
        answer += v
        packets += subpackets

    return answer


def part_b(data):
    bits = hex_to_bits(data)
    packet, *_ = parse(bits)

    answer = eval_packet(packet)

    return answer


def main():
    data = get_data()

    examples = [
        ("38006F45291200", 9, None),
        ("EE00D40C823060", 14, None),
        ("8A004A801A8002F478", 16, None),
        ("620080001611562C8802118E34", 12, None),
        ("C0015000016115A2E0802F182340", 23, None),
        ("A0016C880162017C3686B18A3D4780", 31, None),
        ("C200B40A82", None, 3),
        ("04005AC33890", None, 54),
        ("880086C3E88112", None, 7),
        ("CE00C43D881120", None, 9),
        ("D8005AC2A8F0", None, 1),
        ("F600BC2D8F", None, 0),
        ("9C005AC2F8F0", None, 0),
        ("9C0141080250320F1802104A08", None, 1)
    ]

    for example_data, example_solution_a, _ in examples:
        if example_solution_a is None:
            continue
        example_answer_a = part_a(example_data)
        assert example_answer_a == example_solution_a, f"example_data did not match for part_a: {example_answer_a} != {example_solution_a}"

    answer_a = part_a(data)
    submit(answer=answer_a, part="a")

    for example_data, _, example_solution_b in examples:
        if example_solution_b is None:
            continue
        example_answer_b = part_b(example_data)
        assert example_answer_b == example_solution_b, f"example_data did not match for part_b: {example_answer_b} != {example_solution_b}"

    answer_b = part_b(data)
    submit(answer=answer_b, part="b")


if __name__ == '__main__':
    main()
