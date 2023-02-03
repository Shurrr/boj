N = int(input())

max_bee_house = 1
cnt = 1

while True :

    if N > max_bee_house :
        max_bee_house += 6 * cnt
        cnt += 1

    else :
        break

print(cnt)