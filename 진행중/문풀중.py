import sys

# chapter 2 - 구현 문제
# 11번 문제 - 뱀

# 0 => 사과 없음, 1 => 사과 있음, 2 => 뱀 위치 배열
n = 10 # 행/열 수
k = 4 # 사과 수
second = 0 # 초 시간
dummy_map = [[0] * n for _ in range(n)]

snake_map = []

# 첫 뱀의 위치 => 이동 시 뱀 배열의 데이터 값 모두 이동
snake_map.append([0, 0])

# 인풋 반복문
dummy_map[1][2] = 1
dummy_map[1][3] = 1
dummy_map[1][4] = 1
dummy_map[1][5] = 1

l = 4 # 방향 전환 수
# 인풋 반복문
arr_direct = [[8, 'D'], [10, 'D'], [11, 'D'], [13, 'L']]
directtion = 1

# 북동남서 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while True:
    # 방향 설정
    for d in arr_direct:
        if d[0] == second:
            if d[1] == 'D': # 우회전
                directtion += 1
            elif d[1] == 'L': # 좌회전
                directtion -= 1

            # 방향 범위 넘어가면 값 재설정
            if directtion <= -1:
                directtion = 3
            elif directtion >= 4:
                directtion = 0

    # 이동
    n_x = snake_map[0][0] + dx[directtion]
    n_y = snake_map[0][1] + dy[directtion]
    
    # 시간 추가
    second += 1 

    if n_x >= n or n_y >= n or n_x < 0 or n_y < 0: # 맵 범위 초과시 종료
        break
    
    # 사과가 있을 경우 => 머리 추가
    if dummy_map[n_x][n_y] == 1:
        snake_map.insert(0, [n_x, n_y])
    # 사과가 없을 경우 => 뱀 전체 이동
    else:
        snake_map.insert(0, [n_x, n_y])
        snake_map.pop() # 꼬리 삭제

print(second)