N = int(input())
def plus(n):
    count = 0
    for i in n:
        if i>= 100:
            lis =str(i)
            if 2*int(lis[1]) == int(lis[0])+ int(lis[2]) :
                count += 1
    return count

if N < 100:
    print(N)
else :
    print(99 + plus(range(1,N+1)))

