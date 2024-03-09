def check(n):
    count = 0 
    sum = 0
    for i in n:
        if i == 'O' :
            count += 1
            sum += count
        else :
            count = 0     
    return sum

n = int(input())
for i in range(n):
    lis = list(input())
    print(check(lis))