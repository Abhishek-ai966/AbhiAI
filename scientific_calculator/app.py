# app.py

from flask import Flask, render_template, request
import re

app = Flask(__name__)

def evaluate_expression(expression):
    # Function to evaluate the arithmetic expression
    try:
        result = eval(expression, {'__builtins__': None}, {})
        return str(result)
    except Exception as e:
        return "Error"

@app.route('/', methods=['GET', 'POST'])
def index():
    display = ''
    result = ''

    if request.method == 'POST':
        display = request.form['display']
        button_clicked = request.form['button']

        if button_clicked == '=':
            # Evaluate the expression when '=' is clicked
            result = evaluate_expression(display)
        elif button_clicked == 'clear':
            # Clear the display when 'Clear' is clicked
            display = ''
        elif button_clicked in ['hex', 'bin', 'oct']:
            # Perform base conversions when 'Hex', 'Bin', 'Oct' is clicked
            try:
                if button_clicked == 'hex':
                    result = hex(int(display))
                elif button_clicked == 'bin':
                    result = bin(int(display))
                elif button_clicked == 'oct':
                    result = oct(int(display))
            except ValueError:
                result = 'Error'
        else:
            # Append the button value to the display
            display += button_clicked

    return render_template('index.html', display=display, result=result)

if __name__ == '__main__':
    app.run(debug=True)
