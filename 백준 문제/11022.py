import sys 
n = int(sys.stdin.readline())
a = [sys.stdin.readline().split()for i in range(n)]

def mi(lis):
    return int(lis[0])+int(lis[1])

for i in range(0,len(a)):
    print("Case #%d: %d + %d = %d"%(i+1,int(a[i][0]),int(a[i][1]),mi(a[i])))