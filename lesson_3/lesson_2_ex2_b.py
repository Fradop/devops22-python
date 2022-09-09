from operator import itemgetter


persons = []

name_1 = input("Please tell me your name: ")
age_1 = input("Please tell me your age: ")
size_1 = input("Please tell me your shoe size: ")
person_1 = (name_1, age_1, size_1)
persons.append(person_1)

name_2 = input("Please tell me your name: ")
age_2 = input("Please tell me your age: ")
size_2 = input("Please tell me your shoe size: ")
person_2 = (name_2, age_2, size_2)
persons.append(person_2)

name_3 = input("Please tell me your name: ")
age_3 = input("Please tell me your age: ")
size_3 = input("Please tell me your shoe size: ")
person_3 = (name_3, age_3, size_3)
persons.append(person_3)

sorted_shoe_size = sorted(persons, key=itemgetter(2))
sorted_age = sorted(persons, key=itemgetter(1))

oldest = sorted_age[2]
median_size = sorted_shoe_size[1]
print(f"The oldest person is {oldest[0].capitalize()} who has shoe size {oldest[2]}")
print(f"The person with the median shoe size is {median_size[0].capitalize()} who is {median_size[1]} years old")

searches = {
    "age": {str(age_1): person_1, str(age_2): person_2, str(age_3): person_3},
    "shoe": {},
    "name": {}
}

prop, value = input("Please enter search value, name, age or size followed by a value: ").split(" ")
print(searches[prop][value])


names = (name_1 + name_2 + name_3)
ages = (age_1 + age_2 + age_3)
sizes = (size_1 + size_2 + size_3)
#Sorted_ages = sorted(ages)

#print(Sorted_ages)

#print(ages[0])
#print(person_1)
#print(ages)
# print(ages)
#print("The oldest person is .... who has shoe size ....")

all_persons = {name_1 : (age_1, size_1),
name_2 : (age_2, size_2), name_3 : (age_3, size_3)}
#oldest_person = sorted(all_persons.values(), key=lambda y: y[0])
#oldest_person(sorted (reverse=True))
#print(oldest_person)
#vänd på sorten
#"print(oldest_person[-1])







