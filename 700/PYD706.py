times = eval(input())
alpha_beta = set(chr(a) for a in range(ord('a'), ord('z') + 1))
for _ in range(times):
    input_string = set(input().lower())
    print(alpha_beta.issubset(input_string))
