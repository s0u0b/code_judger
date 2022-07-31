data = []

with open("read.txt", "r") as file:
    for line in file:
        data.append(line.rstrip('\n').split(' '))
        print(line)


heights = [eval(height) for name, height, weight in data]
weights = [eval(weight) for name, height, weight in data]
tallest = heights.index(max(heights))
heaviest = weights.index(max(weights))
average_height = sum(heights) / len(data)
average_weight = sum(weights) / len(data)

print(f"""Average height: {average_height:.2f}
Average weight: {average_weight:.2f}
The tallest is {data[tallest][0]} with {eval(data[tallest][1]):.2f}cm
The heaviest is {data[heaviest][0]} with {eval(data[heaviest][2]):.2f}kg""")
