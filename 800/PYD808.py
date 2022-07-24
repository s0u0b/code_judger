import re

ssn = input()
if re.match(f'\d\d\d-\d\d-\d\d\d\d', ssn):
    print('Valid SSN')
else:
    print('Invalid SSN')
