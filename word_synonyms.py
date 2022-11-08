

number_of_words = int(input())

for i in range(number_of_words):
    word = input()
    synonyms = input()
    dictionary = {}
    if word not in dictionary:
        dictionary[word] = []
    dictionary[word].append(synonyms)
    
    for key, value in dictionary.items():
        print(f"{key} - {', '.join(value)}")

