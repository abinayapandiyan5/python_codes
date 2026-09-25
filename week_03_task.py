J. Looping Constructs
Use Case 1: Table Generator
 Write a program that takes a number from the user and prints the multiplication table from 1 to 10 for that number.
Example:
 If user enters 5, output should be:
 5 x 1 = 5
 5 x 2 = 10
 ...
 5 x 10 = 50


Sol:
===
number = int(input("Enter the number: "))
for i in range(1, 11):
    fin_num = number * i
    print(number, '*', i, "=", fin_num)


Use Case 2: Sum of Even and Odd Numbers
 Write a program that asks the user for a positive integer n.
 Using a loop, calculate and print:
Sum of all even numbers from 1 to n


Sum of all odd numbers from 1 to n

Sol:
====
num = int(input("Enter the number: "))
odd_num = 0
even_num = 0
i = 1
while i <= num:
    if i % 2 == 0:
        even_num += i
    else:
        odd_num += i
    i = i + 1
print(f"Sum of all even numbers from 1 to {num} = ", even_num)
print(f"Sum of all odd numbers from 1 to {num} = ", odd_num)



Use Case 3 (Bug Fixing): Infinite Loop Issue
 Fix the code below so that it prints numbers from 1 to 10 and stops correctly.
Incorrect code:
i = 1
 while i <= 10:
 print(i)
Expected behavior:
 The program must increment i and stop when 10 is printed.

Sol:
====
i = 0
while i < 10:
 i += 1
 print(i)


K. Collection Types
Use Case 1: Product Price Lookup
Create a dictionary with at least 5 products and their prices.
Ask the user to enter a product name.
If found, print the price.
If not found, print: "Product not available." (Hint: use dictionary_var.get(key) function)

Sol:
====
products = {"Apple": 120, "Pomegranate": 150, "Guava": 50, "Banana": 20, "Avocado": 200}
user_inp = input("Enter the product: ")
for key, value in products.items():
    if user_inp.lower() == key.lower():
        print("Price: ", value)
        break
else:
    print("Product is not available")


Use Case 2: City Entry and Duplicate Removal
Ask the user to enter city names repeatedly.
 Stop when the user types "exit".
Requirements:
Store every entered city name in a list (even if it's repeated).
Also store the cities in a set to maintain only unique values.

Finally print:
The complete list of entered cities (with duplicates).
The set of unique cities (duplicates removed).


Sol:
====cities = []
while True:
    city = input("Enter the city: ")
    if city.lower() == "exit":
        break
    cities.append(city)

print("Cities using list: ", cities)
print("Cities using set: ", set(cities))


Use Case 3 (Bug Fixing): List Index Error
 Fix the following code so that it prints all items correctly without an index error:
Incorrect code:
items = ["Pen", "Book", "Mouse", "Keyboard"]
 i = 0
 while i <= len(items):
 print(items[i])
 i = i + 1
Expected behavior:
 The loop should print all the items exactly once and exit without an error.

Sol:
====
items = ["Pen", "Book", "Mouse", "Keyboard"]
i = 0
while i < len(items):
    print(items[i])
    i = i + 1


L. Exception Handling
Use Case 1: Division Safe Calculator
 Ask the user for two numbers.
 Perform division and print the result.
 If the user tries to divide by 0, print:
 "Error: Division by zero is not allowed."

Sol:
====
try:
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Division by zero is not allowed")



Use Case 2: Safe Integer Input
Ask the user to enter a number.
Try converting it to an integer.
If conversion fails, print:
"Invalid input. Please enter a numeric value."

Sol:
====
try:
    num1 = int(input("Enter number 1: "))
    print(num1)
except ValueError:
    print("Invalid input. Please enter a numeric value")



Use Case 3 (Bug Fixing): Multiple Exception Handling
 Fix the below code so it handles both invalid input and division by zero correctly.
Incorrect code:
num1 = int(input("Enter number 1: "))
 num2 = int(input("Enter number 2: "))
 result = num1 / num2
 print("Result:", result)
Expected behavior:
If user enters non-numeric values → print "Invalid input"
If num2 is zero → print "Cannot divide by zero."
Otherwise print the result.

Sol:
====
try:
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Division by zero is not allowed")
except ValueError:
    print("Invalid input. Please enter a numeric value")
