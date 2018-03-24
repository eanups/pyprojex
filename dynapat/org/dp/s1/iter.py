print("Hello Neo, Welcome to the real world!")

# Iterator
my_list = [1, 2, 3, 4]
for i in my_list:
    print(i)

print("-" * 50)

# What's happening within Python
my_iter = my_list.__iter__()
for i in range(0, 3):
    print(my_iter.__next__().__str__())


# Comprehension / Transformation
even_sq_list = [n**2 for n in my_list if n % 2 == 0]
print(even_sq_list)

# Matrix flattening
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_n_double = [n*2 for row in matrix for n in row]
print(flat_n_double)


print("-" * 50)


