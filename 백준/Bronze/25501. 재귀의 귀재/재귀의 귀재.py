import sys

N = int(sys.stdin.readline().rstrip())

def recursion(s, l, r) :
    global cnt
    cnt += 1
    if l >= r :
        return 1

    elif s[l] != s[r] :
        return 0
    
    else :
        return recursion(s, l+1, r-1)

def isPalindrome(S) :
    return recursion(S, 0, len(S)-1)

for i in range(N) :
    cnt = 0
    print(isPalindrome(sys.stdin.readline().rstrip()), cnt)