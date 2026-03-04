def greet(name):
    print("Hello",name)
    greet(Anur)
def add(a, b):
    return a + b

result = add(10, 5)
print("Sum:", result)
def even_numbers(numbers):
    result = []

    for num in numbers:
        if num % 2 == 0:
            result.append(num)

    return result


nums = [1,2,3,4,5,6,7,8]
print(even_numbers(nums))
def word_count(text):
    words = text.split()
    return len(words)


sentence = input("Enter sentence: ")
print("Word count:", word_count(sentence))