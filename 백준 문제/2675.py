import sys 
n = int(sys.stdin.readline())
a = [sys.stdin.readline().split()for i in range(n)]

def multi(n):
    mul = int(n[0])
    lis = list(n[1])
    str = ''
    for i in lis:
        str = str + (i*mul)
    return str

for i in a :
    print(multi(i))