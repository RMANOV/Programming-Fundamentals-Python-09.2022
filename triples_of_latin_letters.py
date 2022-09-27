

number_of_letters = int(input())
letters = [chr(i) for i in range(97, 97 + number_of_letters)]
triples = [f"{i}{j}{k}" for i in letters for j in letters for k in letters]
print(*triples, sep='\n')
