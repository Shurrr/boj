import sys
input = sys.stdin.readline

N = int(input())
ls = []

for i in range(N) :
    ls.append(list(map(int, input().split())))

ls.sort()

for i in range(N) :
    print(ls[i][0], ls[i][1])