num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation  \n1 for +\n2 for -\n3 for *\n4 for /\n ")
match operation:
    case '1':
        result = num1 + num2
    case '2':
        result = num1 - num2
    case '3':
        result = num1 * num2
    case '4':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero!")
    case default:
        print("Error: Invalid operation!")
if 'result' in locals():
    print("Result:", result)
