def safe_divide(numerator, denominator):
    try:
        # convert both inputs
        num = float(numerator)
        den = float(denominator)
        # risky operation
        result = num / den
        return  f"The result of the division is {result:.1f}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."