

initial_list = [str(x) for x in input().split(" ")]

list_of_even_length = [word for word in initial_list if len(word) % 2 == 0]

for word in range(len(list_of_even_length)):
    # print in new line
    print(list_of_even_length[word])
   