n = int(input())
count = 0

if n >= 3 and n <= 10000:
    for i in range(n):
        num = int(input())
        if num % 7 == 1:
            count += 1

if count == 0:
    print('NO')
else:
    print(count)