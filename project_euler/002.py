a = 1
b = 2
even_fib_sum = b
while b <= 4 * 10**6:
    a, b = b, a + b
    if b % 2 == 0:
        even_fib_sum += b

print(even_fib_sum)

# 4613732
