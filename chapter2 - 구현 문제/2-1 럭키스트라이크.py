import sys

# chapter 2 - 구현 문제
# 07 럭키 스트레이트

score = input()

score = str(score)
mid = int(len(score)/2)
left_sum = sum(list(map(int, score[0:mid])))
right_sum = sum(list(map(int, score[mid:])))

if left_sum == right_sum:
    print('LUCKY')
else:
    print('READY')
