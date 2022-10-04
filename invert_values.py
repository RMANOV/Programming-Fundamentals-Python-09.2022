

inicial_string = input().split()

inicial_list = [int(i) for i in inicial_string]


oposite_list = []

for i in range(len(inicial_list)):
    oposite_list.append(inicial_list[i] * -1)
    
print(oposite_list)