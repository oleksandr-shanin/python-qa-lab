from time import time


def routes_count(x, y):
    if not x or not y:
        return 1
    else:
        return routes_count(x, y - 1) + routes_count(x - 1, y)


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def routes_count_math(x, y):
    return(factorial(x + y) // factorial(x)**2)



# for i in range(1, 21):
#     start_time = time()
#     print('{i}x{i}: {routes} paths'.format(i=i, routes=routes_count(i, i)))
#     end_time = time()
#     print('{time:.4f} seconds spent\n'.format(time=end_time - start_time))

# i = 20
# start_time = time()
# print('{i}x{i}: {routes} paths'.format(i=i, routes=routes_count(i, i)))
# end_time = time()
# print('{time:.4f} seconds spent\n'.format(time=end_time - start_time))


i = 20
start_time = time()
print('{i}x{i}: {routes} paths'.format(i=i, routes=routes_count_math(i, i)))
end_time = time()
print('{time:.4f} seconds spent\n'.format(time=end_time - start_time))

# 20x20: 137846528820 paths
# 0.0070 seconds spent
