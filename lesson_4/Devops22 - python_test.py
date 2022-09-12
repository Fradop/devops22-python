"""x = input("please give me a number: ")

im_even = 6
im_even % 2 == 0
True

im_odd = 5
im_odd % 2 == 0
False

#x = input("please give me a number")
if x == im_even: print("even")
if x == im_odd: print("odd")"""




from tracemalloc import start


num = int(input("Please give me a number: "))
if (num % 2) == 0:
    print("{0} is Even".format(num))
else:
    print("{0} is Odd".format(num))

namn = input("Please tell me your name: ")

vip = ("emma", "hugo", "loke", "alex", "blob")
if namn in vip: 
    print(f"Welcome {namn}, your name is on the list")
else:
    print("Sorry, you are not on the list")


ord = input("Please tell me a word: ")
x = len(ord)
print((ord + ", ") * x)


start  = int(input("Enter start: "))
stop = int(input("Enter stop: "))

total = 0
for i in range(start, stop):
    print(i)
    total += i

print(f"Sum: {total}")

while True:
    text = input("Enter text, or Enter stop to quit: ")
    if text == "stop":
        break
    print(f'{text} has length {len(text)}')





#if loop == quit:
   # break









