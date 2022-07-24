print("Input to set1:")
set1 = set()
for _ in range(5):
    set1.add(eval(input()))
print("Input to set2:")
set2 = set()
for _ in range(3):
    set2.add(eval(input()))
print("Input to set3:")
set3 = set()
for _ in range(9):
    set3.add(eval(input()))

print(f"""set2 is subset of set1: {set2.issubset(set1)}
set3 is superset of set1: {set3.issuperset(set1)}""")
