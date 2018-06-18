# Create a list, called my_list, with three numbers. The total of the numbers added together should be 100.
my_list = [30, 20, 50]
sum=0
for i in my_list:
    sum += i

print(sum)

# Create a tuple, called my_tuple, with a single value in it
my_tuple = ('hello',)

print(my_tuple)

# Modify set2 so that set1.intersection(set2) returns {5, 77, 9, 12}
set1 = {14, 5, 9, 31, 12, 77, 67, 8}
set2 = {5, 77, 9, 12}

print(set1.intersection(set2))
