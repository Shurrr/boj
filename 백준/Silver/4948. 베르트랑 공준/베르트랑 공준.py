while True : 
    cnt = 0
    n = int(input())
    
    if n == 0 :
        break

    else :
        
        for i in range(n+1, 2*n + 1) :

            if i > 1 :

                check = True

                for j in range(2, int(i ** 0.5) + 1 ) :
                    if i % j == 0 :
                        check = False
                        break
                
                if check == True :
                    cnt += 1
    
        print(cnt)