no1 = no2 = null_vote = 0
for _ in range(5):
    vote = int(input())
    if vote == 1:
        no1 += 1
    elif vote == 2:
        no2 += 1
    else:
        null_vote += 1
    print(f"""Total votes of No.1: Nami =  {no1}
Total votes of No.2: Chopper =  {no2}
Total null votes =  {null_vote}""")
if no1 > no2 and no1 > 0:
    print('=> No.1 Nami won the election.')
elif no2 > no1 and no2 > 0:
    print('=> No.2 Chopper won the election.')
else:
    print('=> No one won the election.')

