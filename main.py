def sum(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b


print("Select any one of the following - ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your Choice : "))

a = int(input("Enter First Value : "))
b = int(input("Enter Second Value : "))


if choice == 1:
    print(f"The Sum of your Number is {sum(a,b)}")

elif choice == 2:
    print(f"The Subtraction of your Number is {sub(a,b)}")

elif choice == 3:
    print(f"The Multipication of your Number is {mul(a,b)}")

elif choice == 4:
    print(f"The Division of your Number is {div(a,b)}")

else:
    print("Invalid Number Entered")