n = int(input())
su = n
line = 1
while n > 0 :
    n = n-line
    line += 1
if line % 2 == 1 :
    a = n+line-1
    b = line-a
else :
    b = n+line-1
    a = line -b
print(a,'/',b,sep='')