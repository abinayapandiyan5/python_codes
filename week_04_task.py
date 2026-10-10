M. Function Based Programming
Usecase 1: Food Delivery Discount (Convert this program to Exception Handling & FBP)

Sol:
=====
min_cart_amt = 600
disc_pct_whole = 10
max_disc_amt = 100


def calculate_discount(cart_amt):

    if cart_amt < 0:
        raise ValueError("Cart amount cannot be negative")

    if cart_amt >= min_cart_amt:
        print("Eligible for offer")

        disc_pct_fraction = disc_pct_whole / 100
        calc_discount_amt = cart_amt * disc_pct_fraction

        if max_disc_amt >= calc_discount_amt:
            final_bill_amount = cart_amt - calc_discount_amt

            print(
                f"Final bill amount after reducing discount of {disc_pct_whole}%: "
                f"{calc_discount_amt}"
            )
            print(f"Final bill amount: {final_bill_amount}")

        else:
            final_bill_amount = cart_amt - max_disc_amt

            print(
                f"Final bill amount after reducing maximum discount: "
                f"{max_disc_amt}"
            )
            print(f"Final bill amount: {final_bill_amount}")

    else:
        print(
            f"Not eligible for offer. "
            f"Add this amount to your cart: {min_cart_amt - cart_amt}"
        )


try:
    cart_amt = int(input("Enter the cart amount: "))
    calculate_discount(cart_amt)

except ValueError as e:
    print(f"Error: {e}")


Use Case 2: Salary Processing System (HR / Payroll Automation)
Demonstrates input/output functions, default arguments, arbitrary args, returning values, and composing multiple functions.
What Problem It Solves:
Companies calculate employee salary differently depending on bonus percentage, incentives, PF, tax, etc.
How Function-Based Programming Helps:
We create multiple small reusable functions (bonus calc, tax calc, net salary calc)
Then compose them together.

Sol:
====
def get_employee_details():
    name = input("Enter employee name: ")
    basic_salary = float(input("Enter basic salary: "))

    return name, basic_salary


def calculate_bonus(basic_salary, bonus_pct=10):
    bonus = basic_salary * bonus_pct / 100
    return bonus


def calculate_incentives(*incentives):
    total_incentive = sum(incentives)
    return total_incentive


def calculate_pf(basic_salary, pf_pct=12):
    pf = basic_salary * pf_pct / 100
    return pf


def calculate_tax(gross_salary, tax_pct=10):
    tax = gross_salary * tax_pct / 100
    return tax


def calculate_net_salary(basic_salary, bonus, incentives, pf, tax):
    gross_salary = basic_salary + bonus + incentives
    net_salary = gross_salary - pf - tax

    return gross_salary, net_salary


# Main program

name, basic_salary = get_employee_details()

bonus = calculate_bonus(basic_salary)

incentives = calculate_incentives(2000, 1500, 1000)

pf = calculate_pf(basic_salary)

gross_salary = basic_salary + bonus + incentives

tax = calculate_tax(gross_salary)

gross_salary, net_salary = calculate_net_salary(
    basic_salary,
    bonus,
    incentives,
    pf,
    tax
)

print("\n--- Salary Details ---")
print("Employee Name:", name)
print("Basic Salary:", basic_salary)
print("Bonus:", bonus)
print("Total Incentives:", incentives)
print("PF:", pf)
print("Tax:", tax)
print("Gross Salary:", gross_salary)
print("Net Salary:", net_salary)



Usecase3: Number Utility Tool
Create functions:
is_even(num) → returns True/False
find_max(*numbers) → returns highest number from arguments
perform_operation(num, operation) →
If operation = "square" → return num*num
If operation = "cube" → return numnumnum
If unknown → return "Invalid operation"


Test the functions with at least 5 numbers.

Sol:
====
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def find_max(*numbers):
    return max(numbers)


def perform_operation(num, operation):
    if operation == "square":
        return num * num

    elif operation == "cube":
        return num * num * num

    else:
        return "Invalid operation"


numbers = (10, 15, 20, 25, 30)

print("Numbers:", numbers)

# Check even or odd
for num in numbers:
    print(num, "is even:", is_even(num))

    # Find maximum number
    print("Maximum number:", find_max(*numbers))

    # Perform square operation
    print("Square of 10:", perform_operation(10, "square"))

    # Perform cube operation
    print("Cube of 5:", perform_operation(5, "cube"))

    # Test invalid operation
    print("Operation result:", perform_operation(10, "multiply"))


Use Case 4  (Bug Fixing): Fix the Function Logic
The following function is supposed to calculate the square of a number and return the result.
 However, it contains multiple errors. Fix the code so it works correctly.
def find_square():
    num = input("Enter a number: ")
    result = num * num
    print("Square of the number is" result)
    return result
Expected behavior:
The input must be converted to an integer.
The function should print the correct result using proper formatting.
The function must return the square value without errors.

Sol:
====
def find_square():
    num = int(input("Enter a number: "))
    result = num * num
    print("Square of the number is:", result)
    return result


find_square()


Use Case 5: Invoice Generator (**kwargs)
Create a function generate_invoice(**products).
Each key is a product name and each value is its price.
Print all product names with prices and also print the total amount.
Sol:
====
def generate_invoice(**products):

    total_amount = 0

    print("----- Invoice -----")

    for product, price in products.items():
        print(f"{product}: ₹{price}")
        total_amount += price

    print("-------------------")
    print(f"Total Amount: ₹{total_amount}")

    return total_amount


generate_invoice(
    Apple=120,
    Pomegranate=150,
    Guava=50,
    Banana=20
)


Use Case 6: Import vs from import
Create simple functions like add(a,b) and div(a,b) that  returns sum and division of 2 input.
Create a package/sub package/generic_functions.py and place this function .
Create another package/sub package/consumer.py and import the above 2 functions using import, from import with and without alias.

Sol:
====
import fundamental.fundamental2.generic_functions
var1 = fundamental.fundamental2.generic_functions.add(10, 20)
var2 = fundamental.fundamental2.generic_functions.div(100,10)
print(var1, var2)

import fundamental.fundamental2.generic_functions as add1
var1 = add1.add(10, 20)
var2 = add1.div(100,10)
print(var1, var2)

from fundamental.fundamental2.generic_functions import add, div
var1 = add(10, 20)
var2 = div(100, 10)
print(var1, var2)

from fundamental.fundamental2.generic_functions import add as ad, div as dv
var1 = ad(10, 20)
var2 = dv(100, 10)
print(var1, var2)



Use Case 7: global vs local variable
Create a functions add(a,b) that stores the result of a+b to variable c and make the variable c as global variable that should be accessible outside of the function after executing the function.

Sol:
====
def add(a, b):
    global c
    c = a + b

add(10, 20)
print(c)



