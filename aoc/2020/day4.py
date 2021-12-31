from aocd.models import Puzzle
from aocd import lines
import os

puzzle = Puzzle(year=2020, day=4)

REQUIRED_FIELDS = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')

passports_data = puzzle.input_data.split(os.linesep + os.linesep)
passports = list()
nb_valid = 0
for passport_data in passports_data:
    passport = dict()
    passport_data = passport_data.replace('\n', ' ')
    kvs = passport_data.split(' ')
    for kv in kvs:
        (k, v) = kv.split(':')
        passport[k] = v
    
    valid = True
    for rf in REQUIRED_FIELDS:
        if rf not in passport:
            valid = False
    
    if valid == True:
        nb_valid += 1

print("part a: {}".format(nb_valid))