import sys 
n = int(sys.stdin.readline())
a = [sys.stdin.readline().split()for i in range(n)]
for i in range(n):
    H = int(a[i][0])
    W = int(a[i][1])
    N = int(a[i][2])
    floor = N%H
    ho = (N//H)
    if floor == 0:
        print(H*100+ho)
    else :
        print(floor*100+ho+1)