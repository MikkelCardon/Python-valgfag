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


index = len(forfattere)-1
while index >= 0:
    print(forfattere[index])
    index -= 1