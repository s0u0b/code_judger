temperatures = []

for week in range(1, 5):
    print(f'Week {week}:')
    for day in range(1, 4):
        print(f'Day {day}:', end='')
        temperatures.append(eval(input()))
temperature_avg = sum(temperatures) / len(temperatures)
print(f"""Average: {temperature_avg:.2f}
Highest: {max(temperatures)}
Lowest: {min(temperatures)}
""")
