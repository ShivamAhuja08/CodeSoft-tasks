# Calculator Application

This is a simple calculator application built using Python's Tkinter library. It allows users to perform basic arithmetic operations such as addition, subtraction, multiplication, and division.

## How It Works

The calculator application consists of a graphical user interface (GUI) with buttons for numbers, arithmetic operators, and a text entry field to display the input and result. Users can input numbers and perform calculations by clicking on the buttons. 

### Features:
- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`)
- Percentage (`%`) [For getting a remainder]
- Clear (`C`)
- Equals (`=`)

When the user clicks the "=" button, the application evaluates the expression entered in the text entry field using Python's `eval()` function. If the expression is valid, it computes the result and displays it in the text entry field. If the user enters an invalid or incorrect input like: '+' or any other operator at a same time, it will generate an **ERROR**

## How to Run

1. Clone or download the project repository to your local machine.
2. Navigate to the project directory in the terminal.
3. Run the following command to execute the calculator application:

   ```bash
   python calculator.py
   ```