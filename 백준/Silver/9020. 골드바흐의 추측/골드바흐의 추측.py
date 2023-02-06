def is_prime(a) :
    if a == 1 :
        return False

    for i in range(2, int(a ** 0.5) + 1 ) :
        if a % i == 0 :
            return False
    
    return True

    #에라토스테네스의 체 활용. 소수판별을 함수로 사용해보기.

for i in range(int(input())) :
    n = int(input())

    for j in range(n//2, 0, -1) : #range 사용법
        if is_prime(j) and is_prime(n-j) : #두 소수의 합은 n
            print(j, n-j)
            break