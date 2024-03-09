n = list(int(input())for _ in range(9))

max = n[0]
num = 1
for i in range(0,9):
    if n[i] > max:
        max = n[i]
        num = i+1

print(max)
print(num)
