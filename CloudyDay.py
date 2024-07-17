#!/bin/python3

import math
import os
import random
import re
import sys
import operator


#
# Complete the 'maximumPeople' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY p
#  2. LONG_INTEGER_ARRAY x
#  3. LONG_INTEGER_ARRAY y
#  4. LONG_INTEGER_ARRAY r
#

def maximumPeople(people, tower_pos, lclouds, lranges):
    clouds = []
    for c, r in zip(lclouds, lranges):
        clouds.append((max(c - r, 0), c + r))
    # sort by start
    clouds.sort(key=lambda x: x[0])

    towers = []
    for pos, p in zip(tower_pos, people):
        towers.append((pos, p))
    towers.sort(key=lambda x: x[0])

    last_tower_pos = towers[-1][0]
    last_cloud = clouds[-1][1]
    ghost_pos = max(last_tower_pos, last_cloud) + 100

    clouds.append((ghost_pos, ghost_pos))
    cend = -10 * 9
    covered = 0
    uncovered = 0
    max_covered = 0
    t_idx = 0

    def count(pos, exc=False):
        res = 0
        nonlocal t_idx
        # uses less than or less or equal operator
        op = operator.lt if exc else operator.le
        while (t_idx < len(towers) and op(towers[t_idx][0], pos)):
            res += towers[t_idx][1]
            t_idx += 1
        return res

    for start, end in clouds:
        if start > cend:
            covered += count(cend)
            max_covered = max(max_covered, covered)
            covered = 0
            uncovered += count(start, exc=True)
            cend = end
        # next cloud starts and ends before the next cloud
        elif start <= cend and end < cend:
            covered += count(start, exc=True)
            _ = count(end)
        # or it start before but ends later
        elif start <= cend and end >= cend:
            covered += count(start, exc=True)
            max_covered = max(max_covered, covered)
            covered = 0
            _ = count(cend)
            cend = end

    return max_covered + uncovered


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    x = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    y = list(map(int, input().rstrip().split()))

    r = list(map(int, input().rstrip().split()))

    result = maximumPeople(p, x, y, r)

    fptr.write(str(result) + '\n')

    fptr.close()
