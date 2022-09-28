


initial_string = input()
initial_list = []
initial_list.append((initial_string))
initial_list.remove(' ' or '\t' or '\n')

for i in initial_list:
    if i == ' ' or '\t' or '\n':
        initial_list.remove(i)


    if i == 'wolf' and initial_list.index(i) == len(initial_list):
        print("Please go away and stop eating my sheep")
        print("Please go away and stop eating my sheep")
        print("Please go away and stop eating my sheep")
        break


#how to get the index of the wolf in the list?



# print(wolf_position+1)




# near = 0
# # near = initial_list[i].count()
# sheep_position = 0
# sheep_position = initial_list[j]




# for j in range(len(initial_list)):
    


#     near = len(initial_list[j]) - len(initial_list)
#     if near == 0 and initial_list[j] == "wolf":
#         print("Please go away and stop eating my sheep")
#         break
#     else:
#         print("Oi! Sheep number {sheep_position}! You are about to be eaten by a wolf!")
#         break







    # for i in initial_list:
        
    #     if i == "wolf" and near == 0:
    #         print("Please go away and stop eating my sheep")
    #     else:
    #         print("Oi! Sheep number {j} You are about to be eaten by a wolf!")
