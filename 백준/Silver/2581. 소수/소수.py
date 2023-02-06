M = int(input())
N = int(input())

sosu_list = []

for i in range(M, N+1) :

    check = 0

    if i > 1 :

        for j in range(2, i) :
            
            if i % j == 0 :
                check = 1
                break

        if check == 0 :
            sosu_list.append(i)

if len(sosu_list) > 0 :
    print(sum(sosu_list))
    print(sosu_list[0])

else :
    print(-1)