import sys

# chapter 2 - 구현 문제
# 09 문자열 압축

# data = input()
data = "aabbaccc"

res_str = ''
index = 0
cut = 0
min_len = 1001

while cut < len(data):
    this_len = 1001

    i = 0
    cnt_arr = []
    
    for c in range(0, len(data), cut): 
        if data[c:cut] == data[c+cut]:
            cnt_arr[c] += 1
        print(data[c])

    break

    # 압축 형태를 만들어야 됨    

    if min_len > this_len:
        min_len = this_len

    cut += 1


print(min_len)