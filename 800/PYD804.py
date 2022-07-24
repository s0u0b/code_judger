sentence = input()
words = sentence.split()
for index, word in enumerate(words):
    print(word.upper(), end='')
    if index != len(words)-1:
        print(' ', end='')
print()
for index, word in enumerate(words):
    print(word.capitalize(), end='')
    if index != len(words)-1:
        print(' ', end='')
