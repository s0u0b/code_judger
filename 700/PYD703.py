strings = []
while True:
    str_in = input()
    if str_in == 'end':
        break
    strings.append(str_in)
print(f'{tuple(strings)}\n'
      f'{tuple(strings[:3])}\n'
      f'{tuple(strings[-3:])}')
