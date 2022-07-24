print('Create dict1:')
dict1 = {}
while True:
    key = input("Key: ")
    if key == 'end':
        break
    value = input("Value: ")
    dict1[key] = value
print('Create dict2:')
dict2 = {}
while True:
    key = input("Key: ")
    if key == 'end':
        break
    value = input("Value: ")
    dict2[key] = value

for key, value in dict2.items():
    dict1[key] = value

for key in sorted(dict1.keys()):
    print(f'{key}: {dict1[key]}')
