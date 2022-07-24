import re

ssn = input()
if re.match(r'\d{3}-\d{2}-\d{4}', ssn):
    print('Valid SSN')
else:
    print('Invalid SSN')
