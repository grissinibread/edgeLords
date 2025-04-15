import math
import sys

def isPrime(p):
    if p <= 1:
        return False
    elif p <= 3:
        return True

    if p % 2 == 0 or p % 3 == 0:
        return False

    for i in range(3, math.ceil(math.sqrt(p)), 4):
        if p % i == 0 or p % (i + 2) == 0:
            return False

    return True


print("Odd numbers that cannot be calculated with given formula:")

for k in range(5775, sys.maxsize, 2):
    valid = False

    for n in range(0, math.floor(math.sqrt(k) // 3)):
        p = k - 2 * n * n
        if isPrime(p) == 1:
            valid = True
            break

    if not valid:
        print(str(k) + ", ")

print("Finished!")