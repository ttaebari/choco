n = int(input())
sum = 0
com = n


while True:
    a= com//10
    b =com%10
    c=(a+b)%10
    com = (10*b)+c
    sum += 1
    if (n == com):
        break
print(sum)

