self_lis = set(range(1,10001))
lis = set()
for i in range(1,10001):
    for j in str(i):
        i += int(j)
    lis.add(i)

self_lis = self_lis - lis
for i in sorted(self_lis):
    print(i)
