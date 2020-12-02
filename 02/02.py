def is_prime(x):
    return all(x % i for i in range(2, int(x/2)))


def prev_prime(x):
    for j in range(x, 0, -1):
        if is_prime(j):
            return j

counter = 0
i = 0
while i < 5433000:
    if "7" in str(i):
        i += prev_prime(i)
    else:
        counter += 1
    i += 1
    
print(counter)