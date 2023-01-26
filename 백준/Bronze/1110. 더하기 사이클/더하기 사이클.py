N = int(input())
sum = 0
cnt = 0

T = N

while True:
    a = T // 10
    b = T % 10
    c = (a + b) % 10
    sum = (b * 10) + c

    cnt += 1
    
    if (sum == N) :
        break
    else :
        T = sum

print(cnt)