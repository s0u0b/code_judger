dict1 = {}
while True:
    key = input("Key: ")
    if key == 'end':
        break
    value = input("Value: ")
    dict1[key] = value
search_key = input("Search key: ")
print(search_key in dict1.keys())
