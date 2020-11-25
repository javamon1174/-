import sys
from itertools import permutations

# chapter 1 - 그리디 문제
# 05 볼링공 고르기 

# n = int(input())
# data = list(map(int, input().split()))

n, m = 8, 5
data = [1, 3, 2, 3, 2]
data = [1, 5, 4, 3, 2, 4, 5, 2]
res = 0

for a in data:
    for b in data:
        if a != b:
            res += 1

res = res//2

print(res)


