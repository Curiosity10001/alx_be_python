def safe_divide(numerator, denominator):
    try:
        # convert both inputs
        num = float(numerator)
        den = float(denominator)
        # risky operation
        result = num / den
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except ValueError:
        return "Please enter numeric values only"