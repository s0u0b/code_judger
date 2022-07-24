print("Enter group X's subjects:")
x = set()
while True:
    subject = input()
    if subject == 'end':
        break
    x.add(subject)
print("Enter group Y's subjects:")
y = set()
while True:
    subject = input()
    if subject == 'end':
        break
    y.add(subject)
print(sorted(x.union(y)))
print(sorted(x.intersection(y)))
print(sorted(y.difference(x)))
print(sorted(x.symmetric_difference(y)))
