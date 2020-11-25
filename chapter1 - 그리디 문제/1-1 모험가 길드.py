import sys

# chapter 1 - 그리디 문제
# 01 모험가 길드 
 
# 공포도와 그룹 구성원 수는 같아야함
# n 은 모험가 수
# 모든 모험가가 갈 필욘 없음

# n = int(input())
# arr = list(map(int, input().split()))
n = 5
arr = [2, 3, 1, 2, 2]
res = 0 # 결과 값
g_cnt = 0 # 그룹된 모험가 수

arr.sort()
for _ in arr:
    g_cnt += 1
    if g_cnt >= _:
        res += 1
        g_cnt = 0

print(res)