# calculator.py

import math

def evaluate_expression(expression):
    try:
        # Evaluate the expression using eval
        result = eval(expression, {"__builtins__": None}, {"math": math})
        return result
    except Exception as e:
        return str(e)
