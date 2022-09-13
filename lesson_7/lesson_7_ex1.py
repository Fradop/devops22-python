import string

def do_nothing():
    pass
do_nothing()


def hello_world():
    print("hello world")
hello_world()


def results():
    print(1 == 1.0)
results()

def reverse_alphabet():
    print(string.ascii_lowercase[::-1])
reverse_alphabet()

def greet_name(name, greeting="hello"):
    print(f"{greeting} {name}")
greet_name("hugo")

def capital_stirng(word):
    print(word.upper())
capital_stirng("hallå")

def numbers(stop, start=1):
    for x in range(start, stop):
        print(x)
numbers(11)


