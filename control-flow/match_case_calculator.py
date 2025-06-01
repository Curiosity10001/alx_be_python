# prompt to fill the variables with required input
number1 = float(input("Enter the first number:"))
number2 = float(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /):")

#match case use by operation
match operation :
    case "+":
        result = number1 + number2
        print(f"The result is {result}")
    case "-":
        result = number1 - number2
        print(f"The result is {result}")
    case "*":
        result = number1 * number2
        print(f"The result is {result}")
    case "/":
        result = number1 / number2
        print(f"The result is {result}")