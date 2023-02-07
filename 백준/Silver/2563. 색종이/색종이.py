N = int(input())

paper = [ [0]*100 for i in range(100)] 

for j in range(N):
    x, y = map(int, input().split())
    for k in range(y,y+10):
        for l in range(x, x+10):
            paper[k][l] = 1
count = 0

for i in range(100):
    count += paper[i].count(1)

print(count)