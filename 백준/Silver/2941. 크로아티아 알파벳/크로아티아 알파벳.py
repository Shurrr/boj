croatia_alphabet = ['c=', 'c-', 'dz=','d-','lj','nj','s=','z=']

croatia_word = input()
cnt = 0

for i in croatia_alphabet :

    if i in croatia_word :
        i_cnt = croatia_word.count(i)
        cnt += i_cnt
    
print(len(croatia_word) - cnt)