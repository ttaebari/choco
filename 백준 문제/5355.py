import sys 
n = int(sys.stdin.readline())
a = [sys.stdin.readline().split()for i in range(n)]

def op(n,oper):
    if oper == '@' :
        n *= 3
    elif oper == '#' :
        n -= 7
    elif oper == '%':
        n += 5
    return n

def ans(a):
    n = float(a[0])
    oper = a[1:]
    for j in oper :
        n = op(n,j)

    return f"{n:.2f}"

for i in range (0,len(a)):
    print(ans(a[i]))
