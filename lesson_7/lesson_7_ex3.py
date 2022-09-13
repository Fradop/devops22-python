import re


def my_int(x):
    return x + 1
print(my_int(5))

def my_tuple(x, y, z):
    return (x, y, z)
print(my_tuple("hugo", "david", "julian"))

def my_bool():
    return True
    
if my_bool():
    print(True)
else:
    print(False)

def my_float(x, y):
    return x + y
#(my_float(1.2, 1,5))

float_addition = my_float(1.3, 2.0)
print(f'{float_addition}')

def namn(firstname, lastname):
    return(firstname + " " + lastname)
print(namn("hugo", "göransson"))


def area(x, y):
    return x * y
print(area(2, 5))

list_1 = [1, 2, 3, 4]
def sum_int_list(my_list=[]):
    return sum(my_list)
print(sum_int_list(list_1))

def repeat_word(word, repeat):
    return word * repeat
print(repeat_word("hello ", 3))



