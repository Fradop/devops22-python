


"""return x / y
    if y == 0:
    elif y == str:
        raise TypeError
    else:
        print(try_except)


print(try_except(10, 0))"""



        
def try_except():
    try:
       x = int(input("Skriv en siffra du vill dela: "))
       y = int(input("Skriv den siffra du vill dela med: "))
       a = x/y
       print(a)
       pass
    except ZeroDivisionError:
        print("Division by 0 is not allowed")
        return try_except()
    except ValueError:
        print("This is not a valid integer")
        return try_except()

try_except()
    
        




