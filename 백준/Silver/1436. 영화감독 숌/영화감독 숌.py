N = int(input())
cnt = 0
death_num = 666
while True:
    if '666' in str(death_num):
        cnt += 1
    if cnt == N:
        print(death_num)
        break
    death_num += 1