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


min_mult = 1
for i in range(20, 2, -1):
    if min_mult % i:
        number = i
        factors = prime_fact(number)
        print('*', factors)
        for factor in factors:
            if number != factor and min_mult % factor == 0 and (min_mult // factor) % (number // factor):
                number //= factor
                print('/', factor, number, min_mult)
            else:
                print('>', factor, number, min_mult)
        min_mult *= number
        print(i, min_mult)

print(min_mult)

# 232792560
