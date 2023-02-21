N, K = map(int, input().split())
ls=[]
cnt = 0

for i in range(1, N + 1):
    if N % i == 0:
        ls.append(i)
    cnt += 1

if K > len(ls):
    print(0)
    
else:
    print(ls[K-1])