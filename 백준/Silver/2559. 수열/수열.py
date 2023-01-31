N, K = map(int, input().split())
temps = list(map(int,input().split()))

result_temp = []
result_temp.append(sum(temps[:K]))

for i in range(N - K) :
    result_temp.append( result_temp[i] - temps[i] + temps[i+K] )

print(max(result_temp))