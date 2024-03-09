import sys 
n = int(sys.stdin.readline())
a = [sys.stdin.readline().split()for i in range(n)]
case = len(a)

def aver(lis):
    n = int(lis[0])
    sum = 0
    count = 0
    for i in range(1,len(lis)):
        sum += int(lis[i])
    aver = sum/n
    for i in range (1,len(lis)):
        if int(lis[i]) > aver :
            count += 1
    return (count/n)*100


for i in range(0,len(a)):
    print('{0:0.3f}%'.format(aver(a[i])))