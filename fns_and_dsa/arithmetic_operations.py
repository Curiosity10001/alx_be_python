def perform_operation(num1:float,num2:float,operation:str=['add','substract','multiply','divide']):
    #definition of simple arithmetic functions
    match operation:
        case 'add':
            result = num1 + num2
        case 'substract':
            result = num1 - num2
        case 'multiply':
            result = num1 * num2
        case 'devide':
            result = num1 / num2