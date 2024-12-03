import re

filepath = "day3.txt"
pattern = r'mul\((\d+),\s*(\d+)\)'
secondpattern = r"(mul\((\d+),(\d+)\)|do\(\)|don't\(\))"


firstresult = 0
secondresult = 0

with open(filepath, 'r') as file:
    for line in file:
        matches = re.findall(pattern, line)
        for match in matches:
            num1, num2 = match
            num1 = int(num1)
            num2 = int(num2)
            firstresult += num1 * num2


with open(filepath) as f:
    data = f.read()
    do = True
    for i, j, k in re.findall(secondpattern, line):
        if i == "don't()":
            do = False
        elif i == "do()":
            do = True
        else:
            if do:
                secondresult += int(j) * int(k)



print(firstresult)
print(secondresult)

