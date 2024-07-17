import math
import os
import random
import re
import sys
def partition(ar):
    pivot = ar[0]
    l = len(ar)
    new_ar = []
    for i in range(1, l):
        if ar[i] <= pivot:
            new_ar.append(ar[i])
    new_ar.append(pivot)
    for i in range(1, l):
        if ar[i] > pivot:
            new_ar.append(ar[i])

    print('%s' % ' '.join(map(str, new_ar)))
    return ""

m = input()
ar = [int(i) for i in input().strip().split()]
partition(ar)
