n = int(input())
lis = list(map(int,input().split()))
max = max(lis)
aver = 0

for i in range(0,n):
    lis[i] = (lis[i]/max) * 100

for j in range(0,n):
    aver += lis[j]

print(aver/n)
