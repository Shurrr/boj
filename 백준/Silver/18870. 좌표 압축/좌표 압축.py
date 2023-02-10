import sys
input = sys.stdin.readline

N = int(input())
ls = list(map(int, sys.stdin.readline().rstrip().split()))
ls2 = sorted(list(set(ls)))

dic = { ls2[i] : i for i in range(len(ls2)) }

for i in ls :
    print(dic[i], end =' ')

#기본적인 시간복잡도를 알아야함.