def prime_fact(n):
    pf_lst = []
    d = 2
    while n > 1:
        while n % d == 0:
            pf_lst.append(d)
            n //= d
        if d * d > n and n > 1:
            pf_lst.append(n)
            break
        d += 1
    return pf_lst


primes = [2]
prime_candidate = 3
i = 2
while i <= 10001:
    if len(prime_fact(prime_candidate)) == 1:
        primes.append(prime_candidate)
        i += 1
    prime_candidate += 2

print('last', primes[-1])
print('10001', primes[10000])

# 104743
