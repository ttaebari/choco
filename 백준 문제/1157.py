a = input()
a = a.upper()
lis = list(a)
set = list(set(lis))
def check(lis,set):
    num,max  = 1,0
    for i in set :
        num = lis.count(i)
        if num > max :
            max = num
            pri = i
        elif max == num :
            pri = "?"
    return pri

print(check(lis,set))

