max_number = 100

# sum_of_numbers = int((1 + max_number) * max_number / 2)
# sum_of_numbers = sum([i for i in range(101)])
# square_of_sum = sum_of_numbers ** 2
square_of_sum = sum([i for i in range(101)]) ** 2
print(square_of_sum)

sum_of_squares = sum([i ** 2 for i in range(101)])
print(sum_of_squares)

print(square_of_sum - sum_of_squares)

# 25164150
