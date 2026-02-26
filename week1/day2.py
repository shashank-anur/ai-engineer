numbers = [1,2,3,4,5,6,7,8,9]
#largest = numbers[0]
for num in numbers:
    if num % 2 == 0:
        #largest = num
        print(num)

tasks = []
while True:
    task = input("Enter task( or 'quit' to stop): ")
    if task == "quit":
        break
    tasks.append(task)
print("Your task:")
for i in tasks:
    print("-", i)