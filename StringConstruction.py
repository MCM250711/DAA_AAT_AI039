import sys

n = int(input().strip())
for a0 in range(n):
    s = input().strip()
    se = set()
    ans = 0
    for i in s:
        if i not in se:
            ans += 1
            se.add(i)
    print(ans)
