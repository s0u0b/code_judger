x = eval(input())
y = eval(input())
z = eval(input())

secs = x * 60 + y
miles = z / 1.6

speed = miles / secs
speed = speed * (60 * 60)

print(f'Speed = {speed:.1f}')
