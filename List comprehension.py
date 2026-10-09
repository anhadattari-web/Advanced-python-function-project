n = int(input("Enter a number: "))
odd_numbers = [i for i in range(1, n + 1) if i % 2 != 0]
print("Odd numbers:", odd_numbers)
numbers = [i for i in range(1, n + 1)]
print("All numbers:", numbers)
fruits = ["apple", "banana", "mango", "orange", "grapes"]
updated_fruits = [fruit.capitalize() for fruit in fruits]
print("Updated fruit list:", updated_fruits)
