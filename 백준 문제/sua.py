sum = 1
n = 7
w = int(input())
if w < 8 :
    print(1)
else :
    while w > sum :
        sum += n
        if w-sum < n+7 :
            print(n)
            break
        n += 7