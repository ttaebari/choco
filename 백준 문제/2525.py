a, b = map(int,input().split())
c= int(input())
if b+c >= 60:
    mul = (b+c)//60
    if a+mul >=24 :
        print(a+mul-24,b+c-(60*mul))
    else :
        print(a+mul,b+c-(60*mul))
else :
    print(a,b+c)