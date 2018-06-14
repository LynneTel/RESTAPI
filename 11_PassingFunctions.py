def methodception(another):
    return another()


def add_two_numbers():
    return 35 + 77


# print(methodception(add_two_numbers))

###

# print(methodception(lambda:35 + 77))

my_list = [13, 56, 77, 484]
# my_list.remove(13)
# print(my_list)

# print(list(filter(lambda x:x != 13, my_list)))  # A lambda function is just a short, one-line function that has no name.
# print(my_list)

# We could also do
###########################################################################
# print((lambda x: x*3)(5))

# is equal to
def f(x):
    return x * 3

# print(f(5))
###########################################################################

def not_thirteen(x):
    return x != 13


print(list(filter(not_thirteen, my_list)))

# filter() passes each element of my_list as a parameter to the function.
# Pretty neat, eh?
