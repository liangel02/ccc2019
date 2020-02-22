def prime(n):
    c = 2
    if n <= 2:
        return True
    while c * c <= n:
        if n % c == 0:
            return False
        c = c + 1
    return True


def nextPrime(a):
    k = 0
    result = False
    while result is False:
        k = k + 1
        result = prime(a + k)
    return a + k


num = int(input())
values = []
answers = []

for i in range(num):
    N = int(input())
    values.append(N)

for i in range(len(values)):
    found = 0
    integer = values[i] * 2
    varA = 2
    while True:
        varB = integer - varA
        if prime(varB) is True:
            print(str(varA) + " " + str(varB))
            break
        else:
            varA = nextPrime(varA)
