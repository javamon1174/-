import sys

# chapter 2 - 구현 문제
# 10 자물쇠와 열쇠
key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
check = 'true'

# 90도 회전
lenth = len(key)
res = [[0] * lenth for _ in range(lenth)]

for r in range(lenth):
    for c in range(lenth):
        res[c][lenth-1-r] = key[r][c]

key = res
del res

new_rows = []
new_rows.append(key[-1])
for row in key[:-1]:
    new_rows.append(row)

key = new_rows

# 열쇠와 걸쇠 비교
for r in range(lenth):
    for c in range(lenth):
        if key[r][c] == lock[r][c]:
            check = 'false'

print(check)
