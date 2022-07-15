while True:
    cm = int(input())
    if cm == -9999:
        break
    kg = int(input())
    if kg == -9999:
        break
    bmi = kg / (cm / 100) ** 2
    print(f'BMI: {bmi:.2f}')
    state = ''
    if bmi >= 30:
        state = 'fat'
    elif 30 > bmi >= 25:
        state = 'over weight'
    elif 25 > bmi >= 18.5:
        state = 'normal'
    elif 18.5 > bmi:
        state = 'under weight'
    print(f'State: {state}')