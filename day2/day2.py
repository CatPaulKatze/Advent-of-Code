filepath = "day2.txt"
safe_reports = 0
new_safe_reports = 0

with open(filepath, 'r') as file:
    for line in file:
        numbers = [int(num) for num in line.split(" ")]
        increase = True
        decrease = True

        for i in range(len(numbers) - 1):
            difference = numbers[i + 1] - numbers[i]

            if not (1 <= abs(difference) <= 3):
                increase = decrease = False

            if difference > 0:
                decrease = False
            elif difference < 0:
                increase = False

        if increase or decrease:
            safe_reports += 1

print(safe_reports)

filepath = "day2.txt"
safe_reports = 0


def is_safe(report):
    increase = True
    decrease = True

    for i in range(len(report) - 1):
        difference = report[i + 1] - report[i]

        if not (1 <= abs(difference) <= 3):
            return False

        if difference > 0:
            decrease = False
        elif difference < 0:
            increase = False

    return increase or decrease


def is_safe_with_dampener(report):
    if is_safe(report):
        return True

    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]  # Remove the i-th level
        if is_safe(modified_report):
            return True

    return False


with open(filepath, 'r') as file:
    for line in file:
        numbers = [int(num) for num in line.split()]

        if is_safe_with_dampener(numbers):
            safe_reports += 1

print(safe_reports)
