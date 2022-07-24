def compute(sentence, char):
    return sentence.count(char)


sentence_ = input()
char_ = input()
print(f'{char_} occurs {compute(sentence_, char_)} time(s)')
