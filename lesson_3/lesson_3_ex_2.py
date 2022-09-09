from audioop import reverse


x = 1
y = 4
addresses = {"Adam": "Ormvägen 5", "Bella": "Klockgatan 1", "Cornelia": "Vikingagatan 3"}
cars = ["Volvo", "Opel", "BMW"]
numbers1 = {1, 2, 3, x, 6}
numbers2 = {y, 2, 3, 4, 7}

print(addresses["Bella"])
addresses["Daniel"] = "Prinsgränd 2"
print(addresses["Daniel"])
print(len(addresses))

last_key = sorted(addresses)[-1]
print(addresses[last_key])

addresses = {v: k for k, v in addresses.items()}

#print(sorted(addresses, reverse=True))
first_value = sorted(addresses)[0]
print(addresses[first_value])



# addresses = {v: k for k, v in addresses.items()}


#uppgift 6: list

#uppgift 7
print(cars[x])
#opel

#uppgift 8
#print(cars[y])
#inget, eftersom y = 4, vilket blir objekt 5 i listan, då det bara finns 3 objekt i listan så retuneras inget

#uppgift 9 
cars.sort()
print(cars[0])
#bmw kommer upp då man först sorteras listan cars i alfabetsordning och sen ber om första i listan

#uppgift 10
cars_2 = list(cars)
cars.append("saab")
print(cars_2)
print(cars)
#cars_2 pekar på cars, cars pekar på listan, varje gång cars får in något nytt får cars_2 också det
#med cars_2 = list(cars) så skapar cars en egen lista osm den pekar på, när saab läggs till i cars så läggs
#den inte till i cars_2 då den pekar på sin egfna lista'

#10.1
cars_3 = list(cars)
print(cars_3)

#10.2
#cars_3.sort(reverse=True)
#print(cars_3)

#cars_4 = cars + cars_3
#print(cars_4)
cars = cars*2
cars.sort(reverse=True)
print(cars)

#10.3
unique_cars = set(cars)
print(unique_cars)

#uppgift 11
#set 

#uppgift 12
#int och variablar
print(numbers1)
print(numbers2)

#uppgift 13
print(numbers1 & numbers2)
#& = intersection

#uppgift 14
print(numbers1.union(numbers2))

#uppgift 15
print(numbers1 - numbers2)
print(numbers1.symmetric_difference(numbers2))
print(numbers2 - numbers1)
#den symmetriska skillnaden är 1,4,6,7

#b-uppgifter









