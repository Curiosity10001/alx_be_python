def perform_operation(num1,num2,operation):
    #definition of simple arithmetic functions
    match operation:
        case 'add':
            result = num1 + num2
        case 'substract':
            result = num1 - num2
        case 'multiply':
            result = num1 * num2
        case 'devide':
            result = num1 / num2 if num != 0 else "cannot divide with 0"
        case _ :
            "please enter a valid arithmetic operation"