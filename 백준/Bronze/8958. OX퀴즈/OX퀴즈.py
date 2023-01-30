N = int(input())

for i in range(N):

    cnt = 0
    sum = 0
    oxlist = list(input())

    for j in range(len(oxlist)) :
        
        if oxlist[j] == 'O' :

            cnt += 1
            sum += cnt

        else :
            cnt = 0
        
    print(sum)