import sys

N = int(sys.stdin.readline().rstrip())
ls = []

for i in range(N) :
    ls.append(int(sys.stdin.readline().rstrip()))

ls.sort()

for i in range(N) :
    print(ls[i])