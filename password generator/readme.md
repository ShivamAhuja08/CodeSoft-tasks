# Password Generator

## Author
SHIVAM AHUJA

This is a simple password generation application built using Python's Tkinter library. It allows users to generate random passwords based on their input for name and desired password length.

## How It Works

The password generation application consists of a graphical user interface (GUI) with entry fields for the user's name and desired password length. Upon clicking the "Create Strong password" button, the application generates a random password of the specified length and displays it in the designated entry field.

### Features:
- Enter your name
- Specify password length
- Create Strong password
- Copy password to clipboard

When the user clicks the "Create Strong password" button, the application generates a random password by selecting random characters from ASCII range 33 to 126 (which includes printable characters, symbols, and punctuation). The generated password is then displayed in the entry field.

## How to Run

1. Clone or download the project repository to your local machine.

2. Navigate to the project directory in the terminal.

3. Run the following command to execute the password generation application:

   ```bash
   python pwdGenerator.py
   ```