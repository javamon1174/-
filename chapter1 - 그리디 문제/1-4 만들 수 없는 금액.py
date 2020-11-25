import sys

# chapter 1 - 그리디 문제
# 04 만들 수 없는 금액 

# n = int(input())
# data = list(map(int, input().split()))

n = 5
data = [3, 2, 1, 1, 9]
data.sort()
t = min(data)

for x in data:
    if t < x:
        break
    t += x

print(t)