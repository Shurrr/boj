ls = []

for i in range(5) :
    ls.append(int(input()))

ls.sort()
avg = sum(ls) // 5
mid = ls[2]

print(avg, mid, sep='\n')