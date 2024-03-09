b = int(input())
a = int(input())
a1= a//100
a2 = (a-(a1 * 100)) // 10
a3 = a-(a1 *100 + a2 *10)
print(a1,a2,a3)
print(b*a3)
print(b*a2)
print(b*a1)
print(b*a)