import math
import os
import random
import re
import sys
def unboundedKnapsack(k, arr):
    arr.sort()
    ans = [0]
    ans += [0 for i in range(k)]
    for i in arr:
        for j in range(len(ans)):
            if i > j:
                continue
            ans[j] = max(ans[j], i + ans[j - i])
    return ans[k]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for _ in range(t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        k = int(first_multiple_input[1])
        arr = list(map(int, input().rstrip().split()))

        result = unboundedKnapsack(k, arr)

        fptr.write(str(result) + '\n')

    fptr.close()
