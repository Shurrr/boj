import sys
from collections import Counter
input = sys.stdin.readline

ls = []

N = int(input())

for i in range(N) :
    ls.append(int(input()))
    
ls.sort()


print(round(sum(ls)/N)) #산술평균
print(ls[N//2]) #중앙값


cnt = Counter(ls).most_common() #최빈값. 리스트/딕셔너리로도 가능하지만. collections의 Counter 사용. Counter()는 딕셔너리 타입으로 반환되고, most_common()은 튜플을 가지고 있는 리스트로 반환.
if len(cnt) > 1 and cnt[0][1] == cnt[1][1] :
    print(cnt[1][0])
else :
    print(cnt[0][0])

print(max(ls) - min(ls)) #범위