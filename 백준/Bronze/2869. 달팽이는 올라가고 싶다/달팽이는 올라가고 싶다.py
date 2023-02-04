A, B, V = map(int, input().split())

day = (V-B)/(A-B) # 달팽이는 낮에 결국 끝까지 도착한다. 도착하는날이 x라고 한다면 총 올라가는 횟수는 x, 내려오는 횟수는 x-1 이다. Ax - B(x-1) = V 에서 x = (V-B) / (A-B)의 식을 얻어낸다.

if day == int(day):
    print(int(day))

else:
    print(int(day) + 1)