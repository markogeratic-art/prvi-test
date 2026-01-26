x = 1
while x <= 10:
    print(x)
    x = x + 1
print(" pa sva preštela")

n = int(137)
while n != 1:
    print(n)
    if n % 2 == 0:
        n //= 2
    else:
        n = n * 3 + 1
print(n)