import sys

# chapter 1 - 그리디 문제
# 02 곱하기 혹은 더하기 

data = list(map(str, input()))
res = 0

for _ in data:
    _ = int(_)
    if _ >= 2 and res > 0:
        res *= _
    else:
        res += _

print(res)