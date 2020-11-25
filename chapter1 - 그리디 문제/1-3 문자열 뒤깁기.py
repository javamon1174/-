import sys

# chapter 1 - 그리디 문제
# 03 문자열 뒤집기 
# 다음수가 바뀌는 경우 카운트

data = list(map(str, input()))
res_one = 0
res_zero = 0

# 첫번쨰 문자열 선처리
if data[0] == '1':
    res_one += 1
else:
    res_zero += 1

for _ in range(len(data)-1):
    if data[_] != data[_+1]:
        if data[_+1] == '0':
            res_zero += 1
        elif data[_+1] == '1':
            res_one += 1

print(min(res_zero, res_one))
