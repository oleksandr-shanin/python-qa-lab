from time import time


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


def div_func(n):
    pf_lst = prime_fact(n)
    pf_dict = {}
    for i in pf_lst:
        pf_dict[i] = pf_dict.get(i, 0) + 1
    result = 1
    for i in pf_dict:
        result *= pf_dict[i] + 1
    return result


start_time = time()
i = 1
while div_func(i * (i + 1) / 2) <= 500:
    i += 1

end_time = time()

print('{time:.4f} seconds spent'.format(time=end_time - start_time))
print(i * (i + 1) / 2)
print(sum(range(i + 1)))

# 76576500
# 3.5862 seconds spent
