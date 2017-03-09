from time import time

start_time = time()

max_counter = 1
max_init = 1
for init in range(10**6):
    counter = 1
    i = init
    while i > 1:
        if i % 2:
            i = 3 * i + 1
        else:
            i //= 2
        counter += 1
    if counter > max_counter:
        max_counter = counter
        max_init = init

end_time = time()

print('{} -> {} sequence'.format(max_init, max_counter))
print('{time:.4f} seconds spent'.format(time=end_time - start_time))

# 837799 -> 525 sequence
# 98.6146 seconds spent
