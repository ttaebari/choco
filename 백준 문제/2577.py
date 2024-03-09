a =int(input())
b =int(input())
c =int(input())

def check(n,N):
    lis = list(map(int,str(N)))
    num = lis.count(n)
    return num

N = a*b*c
for i in range(10):
    print(check(i,N))