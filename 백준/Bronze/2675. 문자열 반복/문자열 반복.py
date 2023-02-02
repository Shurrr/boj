T = int(input())

for i in range(T) :
    
    R, S = input().split()

    for j in S :
        print(int(R) * f"{j}", end='')

    print()