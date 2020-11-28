import sys

# chapter 2 - 구현 문제
# 08 문자열 재정렬

data = input()
int_sum = 0
arr_str = []
res = []

for c in data:
    # 숫자 여부 판별
    if c.isdigit():
        # 숫자일 경우 누적
        int_sum += int(c)

    else:
        # 문자일 경우
        arr_str.append(ord(c))

arr_str.sort()

# 아스키->문자열로 변환한 결과값을 결과 배열에 저장
for _ in arr_str:
    res.append(chr(_))

del arr_str
res.append(str(int_sum))

print("".join(res))