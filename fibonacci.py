#
# Vrne n-to Fibonaccijeva število.
#

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)

def fibonacci_iter(n):
    if n <= 1:
        return n
    
    predprejsnji = 0
    prejsnji = 1

    for i in range(1, n):
        trenutni = predprejsnji + prejsnji
        predprejsnji = prejsnji
        prejsnji = trenutni

    return trenutni


n = int(input('Vnesi n: '))
print(fibonacci_iter(n))
print(fibonacci(n))



#for i in range(5):
    #print(fibonacci(i))

#for i in range(11):
    #print(fibonacci_iter(i))