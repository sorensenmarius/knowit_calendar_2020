import math
import time

# A bit slow
def find_divisor_sums(num):
    divisors = [1] * num
    for n in range(2, num):
        for index in range(n - 1, num, n):
            divisors[index] += n
    return divisors

counter = 0
for i, n in enumerate(find_divisor_sums(1000000)):
    diff = n - 2*(i+1)
    if diff > 0 and diff == math.isqrt(diff) ** 2:
        counter += 1
print(counter)

# Several minutes slower
def find_divisors(num):
    divisors = []
    j = 1
    while j <= math.sqrt(num):
        if num % j == 0:
            if num / j == j:
                divisors.append(j)
            else:
                divisors.append(j)
                divisors.append(num / j)
        j += 1
    return divisors

counter = 0
for i in range(1, 20):
    s = sum(find_divisors(i))
    diff = int(s - (2*i))
    if diff > 0 and diff == math.isqrt(diff) ** 2:
        counter += 1
print(counter)