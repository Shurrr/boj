list = []
list2 = []

    
for i in range(28) :
    list.append(int(input()))

for i in range(1, 31) :
    
    if i not in list :
        list2.append(i)

list2.sort()
print(list2[0])
print(list2[1])