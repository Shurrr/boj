import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
ls = list(map(int, sys.stdin.readline().rstrip().split()))
result = 0

for i in range(N) :
    for j in range(i+1, N) :
        for k in range(j+1, N) :
            if ls[i] + ls[j] + ls[k] > M :
                continue
            else :
                result = max(result, ls[i] + ls[j] + ls[k])

print(result)