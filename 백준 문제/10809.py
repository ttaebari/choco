stri = list(input())
count = 0
check = 0
for j in range(97,123):
    for i in range(0,len(stri)):
        if ord(stri[i]) == j :
            check = i
            count = 12
            break
        else :
            count = 0
    if count == 12:
        print(check,end= " " )
    else :
        print(-1, end=" ")