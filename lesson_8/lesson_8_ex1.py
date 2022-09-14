
def num(numb):
    if isinstance(numb, float):
        print("this is a float")
    else:
        raise TypeError("This is not a float")

num(2.4)