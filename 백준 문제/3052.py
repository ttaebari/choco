n = list(int(input())for _ in range(10))

for i in range(0,10):
    n[i] = n[i] % 42

n = list(set(n))
print(len(n))
