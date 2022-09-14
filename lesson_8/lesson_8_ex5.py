my_list = list(range(1, 11))

xy = lambda x: x + 1

my_list = list(map(xy, my_list))

print(my_list[1:])

