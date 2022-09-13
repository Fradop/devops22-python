import string

def numbers(stop=11, start=1):
    for x in range(start, stop):
        print(x)
numbers()


def my_string(word="hallå", reversed=True):
    if reversed == True:
        print(word[::-1])
    
my_string()

def my_string(word="hallå", reversed=False):
    if reversed == False:
        print(word)
    
my_string()
