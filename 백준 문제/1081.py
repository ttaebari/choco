a = int(input())
n = list(map(int,input().split()))

def ma(n):
    max = n[0]
    for i in n:
        if i >max :
            max = i
    return max

def mi(n):
    min = n[0]
    for i in n:
        if i <min :
            min = i
    return min

print(mi(n), ma(n))

