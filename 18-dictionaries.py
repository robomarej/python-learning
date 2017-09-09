d = {"surname":"Smith", "name":"John"}
print(d) # {'surname': 'Smith', 'name': 'John'}
print(d["name"]) # John
d = {
    "surname":"Smith",
    "name":"John",
    "cities":(
        "Porto",
        "San Diego",
        "Bali"
    ),
    "age": 20
}
print(d) # {'name': 'John', 'age': 20, 'cities': ('Porto', 'San Diego', 'Bali'), 'surname': 'Smith'}
city = d["cities"][2]
print(city) # Bali
