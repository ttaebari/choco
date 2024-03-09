from math import factorial as fac
n=str(fac(int(input())))
res=n[len(n)-1]
for i in range(1,len(n)):
    if n[-i]!='0':
        res=n[-i]
        break
print(res)