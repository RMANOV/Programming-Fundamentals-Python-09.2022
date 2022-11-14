

baned_words = input().split(', ')
text = input()

for word in baned_words:
    text = text.replace(word, '*' * len(word))

print(text)