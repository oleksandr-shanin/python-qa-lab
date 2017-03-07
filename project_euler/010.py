from time import time

start_time = time()
primes_lst = []

for i in range(2, 2 * 10**6):
    is_prime = True
    for prime in primes_lst:
        is_prime = is_prime and i % prime
        if prime ** 2 > i:
            break
    if is_prime:
        # print(i)
        primes_lst.append(i)

end_time = time()

print(end_time - start_time, 'seconds spent')
print('sum =', sum(primes_lst))

# 142913828922
# 393.5636308193207 seconds spent

upper_boundary = 2 * 10**6
start_time = time()
primes_set = set(range(2, upper_boundary))
el = 2
while el * el < upper_boundary:
    primes_set -= set(range(el * el, upper_boundary, el))
    el += 1
    while el not in primes_set:
        el += 1

end_time = time()

print(end_time - start_time, 'seconds spent')
print('sum =', sum(primes_set))

# 142913828922
# 2.2081334590911865 seconds spent
