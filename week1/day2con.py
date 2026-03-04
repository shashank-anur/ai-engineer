def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
print(celsius_to_fahrenheit(30))
def remove_duplicate(numbers):
    unique = []
    for num in numbers:
        if num not in unique:
            unique.append(num)
    return unique
print(remove_duplicate([1,2,2,2,3,4,5,5,5,6]))
def find_min_max(numbers):
    if not numbers:
        return None, None

    minimum = numbers[0]
    maximum = numbers[0]

    for num in numbers[1:]:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num

    return minimum, maximum
print(find_min_max([4,8,19,23,54,0]))
def grade(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "Fail"
print(grade(76))
def expense_tracker():
    expenses = []
    while True:
        entry = input("Enter expense (or 'quit'): ")
        if entry == "quit":
            break
        expenses.append(float(entry))
        print("Total spent:", sum(expenses))