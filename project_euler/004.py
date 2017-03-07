palindrome_lst = []
for i in range(100, 1000):
    for j in range(100, 1000):
        if str(i * j) == str(i * j)[::-1]:
            palindrome_lst.append(i * j)

print(max(palindrome_lst))

# 906609
