

inicial_string = input().split()
inicial_list = []
inicial_list.append(inicial_string)
oposite_list = []

for i in range(len(inicial_list)):
    # inicial_list[i] = int(inicial_list[i])
    oposite_list.append((inicial_list[i]) * -1)
print(oposite_list)