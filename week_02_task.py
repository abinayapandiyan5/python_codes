F. Type identification & Casting
Use Case 1:
Write a program that asks for an employee’s age.
1. Checks its type is of string (think about using isinstance() function)
2. Converts it to int (continue writing your program from here..)
3. Prints the years pending for retirement, for eg. 60 is the retirement age.
Example:
Enter your age: 40
You will retire in 20 years at Inceptez Technologies.

Sol:
====
age = input("Enter your age: ")
if age.isdigit():
    age = int(age)
    retired_age = 60
    if retired_age > age:
        eligible_years = retired_age - age
        print(f"You will retire in {eligible_years} years at Inceptez Technologies")
    else:
        print("You are not eligible to work")
else:
    print("Please enter your age in number")


Use Case 2 (Debug):
Fix the type error in the following code for salary calculation:

salary = '50000'
bonus = 10000
print('Total Salary in Inceptez:', salary + bonus)

Sol:
====
salary = '50000'
salary = int(salary)
bonus = 10000
print('Total Salary in Inceptez:', salary + bonus)

G. Data types and casting
Use Case 1 — Employee Salary Breakdown Using Numeric & String Types
Employee Salary Breakdown
a. Write a program that asks the user for:
employee_name (string)
base_salary (float)
hra_percent (integer)
bonus_amount (float)

B. Convert inputs to the correct datatype if required.
Calculate:
 HRA = base_salary * (hra_percent / 100)
 Total Salary = base_salary + HRA + bonus_amount


C. Print the output like this:
Employee: Arun
Base Salary: 40000.0
HRA @ 20%: 8000.0
Bonus: 5000.0
Total Salary Payable: ₹53000.0

Sol:
=====
employee_name: str = input("Enter your name: ")
base_salary: float = float(input("Enter your basic salary: "))
hra_percent: int = int(input("Enter your HRA percent: "))
bonus_amount: float = float(input("Enter your bonus_amount: "))

HRA = base_salary * (hra_percent / 100)
Total_Salary = base_salary + HRA + bonus_amount

print("Employee: ", employee_name)
print("Base Salary: ", base_salary)
print("HRA @ 20%: ", HRA)
print("Bonus: ", bonus_amount)
print("Total Salary Payable: " ,"₹" ,Total_Salary)


Use Case 2: Student Result Classification
a. Write a program that takes marks as input (initially as a string).
B. Check if the value can be converted to float.
C. Then classify (try using if condition with the help of AI, however we will learn about if condition soon):
Marks >= 90 --> Outstanding
 Marks >= 75 --> Excellent
 Marks >= 50 --> Pass
 Marks < 50 --> Fail
D. If the input is not numeric, print:
 Invalid marks entered — Please provide numeric input.


Sol:
====
marks = float(input("Enter your mark: "))
if marks >= 90:
    print("Outstanding")
elif marks >= 75:
    print("Excellent")
elif marks >= 50:
    print("Pass")
else:
    print("Fail")



Use Case 3: Bug Fixing — Datatype Mismatch
The below code is intended to calculate total price, but it has datatype errors. Fix it.
Incorrect code:
item_name = input("Enter product name: ")
 price = input("Enter price per item: ")
 quantity = input("Enter quantity: ")
total_cost = price * quantity
print("You purchased " + quantity + " units of " + item_name)
 print("Total payable: " + total_cost)
Expected output after fixing:
Enter product name: Notepad
 Enter price per item: 35.50
 Enter quantity: 3
You purchased 3 units of Notepad
 Total payable: 106.5 INR


Sol:
====
item_name = input("Enter product name: ")
price = float(input("Enter price per item: "))
quantity = int(input("Enter quantity: "))
total_cost = price * quantity
print("You purchased ", quantity, " units of ", item_name)
print("Total payable: ", total_cost, "INR")


H. Python Operators Usecases
Use Case 1: Internet Data Usage Calculator
Write a program that asks the user for:
Total monthly data limit (in GB)
Data used so far (in GB)


Calculate using arithmetic operators:
 Remaining data = limit - used
 Usage percentage = (used / limit) * 100
Print:
Remaining data
Usage percentage rounded to 2 decimals


If usage percentage is greater than or equal to 80, print:
 "Warning: High usage, consider upgrading your plan."


Sol:
====
limit = float(input("Enter your total monthly data limit (in GB): "))
used = float(input("Enter the data used so far (in GB): "))

remaining = limit - used
usage_percentage = (used / limit) * 100

print(f"Remaining data: {remaining} GB")
print(f"Usage percentage: {usage_percentage:.2f}%")

if usage_percentage >= 80:
    print("Warning: High usage, consider upgrading your plan.")


Use Case 2: Shopping Discount Calculation
Write a program that takes:
Original price (float)
Discount percent (int)


Using assignment and arithmetic operators, calculate:
 Discount amount = (price * discount_percent) / 100
 Final price = price - discount_amount
Print:
 Original price, discount applied, and final payable amount.

Sol:
====
original_price = float(input("Enter the original amount: "))
discount_percent = int(input("Enter the discount percent: "))

discount_amount = (original_price * discount_percent) / 100
final_price = original_price - discount_amount

print("Original price: ", original_price, ",", "Discount_amount: ", discount_amount,"and","final_price: ", final_price)



Use Case 3 (Bug Fixing): Logical and Comparison Operator Errors
The following code should determine voting eligibility, but it contains operator mistakes. Fix it.
Incorrect code:
age = input("Enter age: ")
 citizen = input("Are you an Indian citizen? (yes/no)")
if age > "18" and citizen = "yes":
 print("Eligible to vote")
 else:
 print("Not eligible")


Expected behavior:
Convert age to integer before comparison.

Only print "Eligible to vote" if age is 18 or above AND citizen input is "yes" (case-insensitive).

Sol:
====
age = int(input("Enter your age: "))
citizen = input("Are you an Indian citizen? (yes/no): ")
if age >= 18 and citizen.lower() == "yes":
    print("Eligible to vote")
else:
    print("Not eligible")



I. Conditional Structure
Use Case 1: Banking Eligibility Check
Write a program that asks the user for:
Age
Monthly income


Conditions:
If age < 18: print "Not eligible for a bank account."
If age >= 18 and income < 15000: print "Eligible for basic savings account."
If age >= 18 and income between 15000 and 50000: print "Eligible for savings + salary account."
If age >= 18 and income > 50000: print "Eligible for premium account."

Sol:
====
age = int(input("Enter your age: "))
income = float(input("Enter your income: "))
if age < 18:
    print("Not eligible for a bank account")
elif age >= 18 and income < 15000:
    print("Eligible for basic savings account")
elif age >= 18 and 15000 < income < 50000:
    print("Eligible for savings + salary account")
elif age >= 18 and income > 50000:
    print("Eligible for premium account")



Use Case 2: Check room availability
-Check room availability
    - If available:
        - If guest is VIP
            → Offer complimentary upgrade
        - Else if member 5+ years
            → Offer discount
        - Else
            → Standard price
    - Else:
        → Show: "No rooms available"


Sol:
===
total_rooms = int(input("Enter total number of rooms in the hotel: "))
booked_rooms = int(input("Enter number of rooms already booked: "))

available_rooms = total_rooms - booked_rooms

if available_rooms > 0:
    print(f"Rooms available: {available_rooms}")

    is_vip = input("Is the guest a VIP? (yes/no): ").lower()
    membership_years = int(input("Enter guest membership years: "))


    if is_vip == "yes":
        print("Offer complimentary upgrade")
    elif membership_years >= 5:
        print("Offer discount")
    else:
        print("Standard price")
else:
    print("No rooms available")


Use Case 3 (Bug Fixing): Nested Condition Logic Issue
Fix the following code so that it correctly determines whether the entered temperature indicates normal, fever, or high fever.
Incorrect code:
temp = input("Enter body temperature in Celsius: ")
if temp < "37":
 print("Normal temperature")
 elif temp > "37" and temp < "39":
 print("Fever")
 else
 print("High fever")

Expected behavior:
Convert temperature to float before comparison.
Conditions should print:

 Normal temperature (less than 37)
 Fever (between 37 and 39)
 High fever (39 and above)


Sol:
====
temp = float(input("Enter body temperature in Celsius: "))
if temp < 37:
 print("Normal temperature")
elif temp > 37 and temp < 39:
 print("Fever")
else:
 print("High fever")
