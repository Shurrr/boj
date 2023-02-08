import sys

N = int(sys.stdin.readline().rstrip())
ls = [0] * 10000 #미리 리스트를 만들어서 메모리 사용

for i in range(N) :
    num = int(sys.stdin.readline().rstrip())
    ls[num - 1] = ls[num - 1] + 1

for j in range(10000) :
    if ls[j] != 0 :
        for k in range(ls[j]) :
            print(j+1)