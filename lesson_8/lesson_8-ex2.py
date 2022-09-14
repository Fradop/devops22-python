from logging import exception
from tokenize import Number


"""def int_input(text):
    number = None
    while True:
        try:
            number = int(input(text))
            break
        except ValueError:
            print("Sorry, not an int")
    return number

my_number = int_input("Enter a number: ")"""


"""def input_retry(number):
    try:
        return int(input(number))
    except ValueError:
        print("Sorry, not an int")
        return input_retry(number)
    except exception:
        if (my_number % 2) == 0:
            print("Sorry, even numbers are not allowed")
    return input_retry(number)



my_number = input_retry("Enter a number: ")"""

    #except my_number % 2 == 0:

"""def input_retry(number):
    try:
        if (my_number % 2) == 0:
            print("Sorry, even numbers are not allowed")
        return input_retry(number)
    except ValueError:
        print("Sorry, not an int")
        return input_retry(number)
    except:
        return int(input(number))
        

my_number = input_retry("Enter a number: ")"""

"""def input_retry(number):
    try:
        return int(input(number))
    except ValueError:
        print("Sorry, not an int")
        return input_retry(number)
    raise Exception
if (my_number % 2) == 0:
            print("Sorry, even numbers are not allowed")
    return input_retry(number)"""

def int_input(text):
    number = None
    while True:
            try:
                my_number = int(input(text))
                break
            except ValueError:
                print("Not a valid integer!")
            except:  
                raise Exception
    if (my_number % 2 == 0):
            print("Even numbers is not allowed! ")
            return int_input(text)        
    else:
        return my_number


my_number = int_input("Enter a number: ")
print(f'result: {my_number}')


    






