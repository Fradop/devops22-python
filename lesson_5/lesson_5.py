from lib2to3.pgen2.literals import test

firstname = "john"
lastname = "smith"
tele = "00468123456789"

#uppgift 1
print(firstname, lastname, tele)
fullname = firstname + " " + lastname
print(fullname)
print(len(fullname), len(firstname), len(lastname))
print(fullname + '\n ' + tele) 

print(fullname + " " + tele)
print(f'{fullname} {tele}')
print('{}'.format(fullname + tele))
print(fullname[:6])
print(fullname[1:-1])
print(fullname.upper()[::2])
print(fullname[::-1])
print(fullname[5:6])

sak = u'\u20ac'
glad = u'\u1f600'
ledsen = u'\u1f625'
a = 2000
pris = input("What does your new car cost: ")
print(f"Your new car cost {pris} {sak}")
#print(sak)
#if pris < 2000:
 #   print(glad)
#else print(ledsen)

print(glad) if str(pris) < str(a) else print(ledsen)
lön = 200
lön = str(lön)
print(f"Your current salery is 2000 {sak}")
okning = input("How much more salery do you want? ")
print(okning)
prcent_1 = okning//lön
print(prcent_1)

"""procent_1 = okning // lön
print(f"That is an increase of {procent_1} %, that is too much")
okning_2 = print("Give me another suggestion ")
procent_2 = okning_2 // lön
print(f"That is an increase of {procent_2} %")"""





