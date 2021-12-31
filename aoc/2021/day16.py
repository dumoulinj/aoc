from aocd.models import Puzzle
from aocd import lines
from collections import defaultdict, Counter
from copy import copy, deepcopy
import itertools
import sys
import math

import attr
# a:
# b:

puzzle = Puzzle(year=2021, day=16)

hex_2_bin = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
}

count_version = 0

def get_literal(p):
    number = ""
    idx = 0
    stop = False
    while not stop:
        if p[idx] == "0":
            stop = True
        number += p[idx+1:idx+5]
        idx += 5
    
    while idx % 5 != 0:
        idx += 1
    
    return int(number, 2), idx

def read_packet(p):
    global count_version
    idx = 0
    try:
        version = int(p[idx:idx+3], 2)
        count_version += version
        type_id = int(p[idx+3:idx+6], 2)
    except:
        print("error ", p)
        assert False

    idx += 6
    number = 0

    if type_id == 4:
        number, _idx = get_literal(p[idx:])
        idx += _idx
    else:
        leng_type_id = p[idx]
        idx += 1
        vals = list()
        if leng_type_id == "0":
            # the next 15 bits are a number that represents the total length in bits of the sub-packets contained by this packet
            total_length_sub_packets = int(p[idx:idx+15], 2)
            idx += 15
            target = idx + total_length_sub_packets
            while idx < target:
                _, _, _number, _idx = read_packet(p[idx:])
                vals.append(_number)
                idx += _idx
        else:
            # the next 11 bits are a number that represents the number of sub-packets immediately contained by this packet
            nb_sub_packets = int(p[idx:idx+11], 2)
            idx += 11
            for i in range(nb_sub_packets):
                _, _, _number, _idx = read_packet(p[idx:])
                vals.append(_number)
                idx += _idx
        
        if type_id == 0: # SUM
            number = sum(vals)
        elif type_id == 1: # PRODUCT
            number = math.prod(vals)
        elif type_id == 2:
            number = min(vals)
        elif type_id == 3:
            number = max(vals)
        elif type_id == 5:
            assert len(vals) == 2
            number = 1 if vals[0] > vals[1] else 0
        elif type_id == 6:
            assert len(vals) == 2
            number = 1 if vals[0] < vals[1] else 0
        elif type_id == 7:
            assert len(vals) == 2
            number = 1 if vals[0] == vals[1] else 0
    #print(idx)
    return version, type_id, number, idx

bseq = ""

h_message = lines[0]
# h_message = "8A004A801A8002F478"
# h_message = "620080001611562C8802118E34"
# h_message = "C0015000016115A2E0802F182340"
# h_message = "A0016C880162017C3686B18A3D4780"
#h_message = "EE00D40C823060"
#h_message = "38006F45291200"
#h_message = "D2FE28"
#h_message = "9C0141080250320F1802104A08"
# while h_message.endswith("0"):
#     h_message = h_message[:-1]

for c in h_message:
    bseq += hex_2_bin[c]

idx = 0
# bseq = "110100101111111000101000"
# bseq = "00111000000000000110111101000101001010010001001000000000"
# bseq = "11101110000000001101010000001100100000100011000001100000"
while True:
    version, type_id, res_b, _idx = read_packet(bseq[idx:])
    idx += _idx
    if idx + 11 > len(bseq):
        break


# Ignore trainling 0s
# Header
# 3 bits -> version
# 3 bits -> type ID


# Type ID 4 -> literal value
# leading 0s until lenght is multiple of 4bits
# then broken into 4bits groups, each of them prefixed with a 1 except the last group (prefixed with 0) -> so each group is 5 not 4


print("part a: {}".format(count_version))
#puzzle.answer_a = count_version 

print("part b: {}".format(res_b))
puzzle.answer_b = res_b