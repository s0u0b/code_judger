color_dict = {}
while True:
    key = input("Key: ")
    if key == 'end':
        break
    value = input("Value: ")
    color_dict[key] = value
for key in sorted(color_dict.keys()):
    print(f'{key}: {color_dict[key]}')
