from collections import Counter

filepath = 'day1.txt'

with open(filepath, 'r') as file:
    left_list = []
    right_list = []
    for line in file:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

    left_list.sort()
    right_list.sort()

    resultdis = sum(abs(l - r) for l, r in zip(left_list, right_list))


with open(filepath, 'r') as file:
    left_list = []
    right_list = []
    for line in file:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

    right_counts = Counter(right_list)

    resultsim = sum(num * right_counts[num] for num in left_list)

print(resultdis)
print(resultsim)
