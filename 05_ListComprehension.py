my_list = [0, 1, 2, 3, 4]
an_equal_list = [x for x in range(5)]

multiply_list = [x * 3 for x in range(5)]
# print(multiply_list)

# print(8 % 3)
# print(9 % 2)

# print([n for n in range(10) if n % 2 == 0])

# for my_number in range(10):
#     print(my_number)
#
# [my_number for my_number in range(10)]
#
# [my_number * 2 for my_number in range(10)]
#
# 1 % 2
# 2 % 2
# 5 % 2
# 8 % 3
#
# [n for n in range(10) if n % 2 == 0]
#
names_list = ["John", " Rolf", "anne", "GREG"]
normalised_people = [person.strip().title() for person in names_list]
print(normalised_people)
# lowercase_names = [name.lower() for name in names_list]
# print(lowercase_names)
