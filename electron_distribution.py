

number_of_electrons = int(input())
list_of_shels = []
current_shel = 1
while number_of_electrons > 0:
    max_electrons = 2 * current_shel ** 2
    if number_of_electrons >= max_electrons:
        list_of_shels.append(max_electrons)
        number_of_electrons -= max_electrons
    else:
        list_of_shels.append(number_of_electrons)
        number_of_electrons = 0
    current_shel += 1

print(list_of_shels)