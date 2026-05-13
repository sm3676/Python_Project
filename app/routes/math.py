def calculate(operation: str, a: float, b: float):
    if operation == "add":
        return a + b
    elif operation == "sub":
        return a - b
    elif operation == "mul":
        return a * b
    elif operation == "div":
        if b == 0:
            raise ValueError("Division by zero")
        return a / b
    elif operation == "power":
        return a ** b
    elif operation == "mod":
        return a % b
    else:
        raise ValueError("Invalid operation")