states = {
    'Karnataka' : 'KR',
    "Jharkhand" : 'JH',
    "Uttar Pradesh" : 'UP',
 }

cities = {
    'KR' : "Banglore",
    'JH' : "Bokaro",
}

# adding more cities
cities['UP'] = "Lucknow"

print("Jharkhand has: ",cities[states['Jharkhand']])
print("Uttar Pradesh has: ",cities[states['Uttar Pradesh']])


print("-" * 10)
for abbrev,city in cities.items():
    print(f"{abbrev} contains {city}.")

print("-" * 10)
for state,abbrev in states.items():
    print(f"{state} it's short form is {abbrev}.")
    print(f"This state has : {cities[abbrev]}")

state = states.get("Himachal")

if not state:
    print("This is not in the dict.")

city = cities.get("HM" , "Does not exists.")
print(f'The city for the state HImachaal is {city}.')