from itertools import permutations

def make(lis) : #리스트를 하나의 정수로 바꿔주는 함수
    int = 0
    for i in range(0,len(lis)):
        int = int + ((lis[i])*(10**i))
    return int

def prime(n): #소수인지 판별하는 함수
    for i in range(2,int(n**(1/2)+1)):
        if n%i == 0 :
            return 0
    return 1

def answer(lis): #답을 구하는 함수
    ans , ans_1 = [], []
    ans_lis = list(permutations(lis,len(lis)))
    for i in range(0,len(ans_lis)) : 
        ans.append(make(ans_lis[i]))

    for i in ans :
        if prime(i) == 0 :
            ans_1.append(i)
    return len(list(set(ans_1)))

n = int(input())
lis = list(map(int, list(str(n))))
ans = answer(lis)
for i in range(1,lis.count(6)+1) :
    lis.remove(6)
    lis.append(9)
    ans += answer(lis)
print(ans)

