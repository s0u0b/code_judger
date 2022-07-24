run_times = eval(input())
for _ in range(run_times):
    nums = list(map(float, str.split(input())))
    print(f'{max(nums) - min(nums):.2f}')
