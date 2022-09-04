x = int(input("Enter x = "))
operator = input("Enter operator ")
y = int(input("Enter y = "))

if operator == "+":
    print(x + y)
elif operator == "-":
    print(x - y)
elif operator == "*":
    print(x * y)
elif operator == "/":
    if y == 0:
        print("Division by 0 is not allowed")
    else:
        print(x / y)
else:
    print('bad operator')
