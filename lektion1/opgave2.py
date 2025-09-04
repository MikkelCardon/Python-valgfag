forfattere = ['Jens', 'Bøv', 'Dennis', 'Flemming']

for forfatter in forfattere:
    print(forfatter)

forfattere.append('Jens')

forfattere.pop(1)

for forfatter in forfattere:
    print(forfatter)

number_of_forfatteres = len(forfattere)

print(number_of_forfatteres)

print(forfattere)
print(forfattere[2:])


