N,A = map(int,input().split())
m = N//A
max = m
while m >= A :
    m = m//A
    max += m
print(max)