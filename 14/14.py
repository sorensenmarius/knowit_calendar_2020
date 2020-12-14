import sympy as sp

unike = set([0, 1])
prim_teller = 0
siste1, siste2 = 1, 0
for i in range(2, 1800813 + 1):
    tall = x if (x := siste2 - i) > 0 and x not in unike else siste2 + i

    if sp.isprime(tall):
        prim_teller += 1
    
    unike.add(tall)
    siste2 = siste1
    siste1 = tall

print(prim_teller)