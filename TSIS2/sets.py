my_set = {1, 2, 3, 4, 5}
print(my_set)

my_set.add(6)
print(my_set)

my_set.remove(3)
print(my_set)

my_set.discard(10)
print(my_set)

another_set = {4, 5, 6, 7}
union_set = my_set | another_set
print(union_set)

intersection_set = my_set & another_set
print(intersection_set)

difference_set = my_set - another_set
print(difference_set)

print(len(my_set))
