square = lambda x: x * x

people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

# Python doesn’t know how to compare two Dictionaries to check if one is less than the other.

# def f(person):
#     return person["name"]

# we can make our code more readable by using a lambda function:

people.sort(key=lambda person: person["name"])

# people.sort(key=f)  #specifies which part of the dictionary we wish to use to sort

print(people)