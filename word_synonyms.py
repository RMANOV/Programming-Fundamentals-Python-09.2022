

number_of_words = int(input())

for i in range(number_of_words):
    word = input()
    synonyms = input()
    dictionary = {}
    if word not in dictionary:
        dictionary[word] = []
    dictionary[word].append(synonyms)
[print(f"{word} - {', '.join(dictionary[word])}") for word in dictionary]


# [print(f"{word} - {', '.join(synonyms[word])}") for word in synonyms]