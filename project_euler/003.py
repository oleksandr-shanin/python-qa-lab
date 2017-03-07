# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

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


n = 600851475143
print(prime_fact(n))
print(prime_fact(n)[-1])

# 6857
