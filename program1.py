print("Hello This is my First Program")

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a > b:
        return a / b
    else:
        return b / a

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter your choice: ")
num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))

if choice == '1':
    print(add(num1, num2))
elif choice == '2':
    print(sub(num1, num2))
elif choice == '3':
    print(mul(num1, num2))
elif choice == '4':
    print(div(num1, num2))
else:
    print("Invalid choice")
