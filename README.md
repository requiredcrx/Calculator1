# Calculator
This is a Python program that simulates a basic calculator that can perform addition, subtraction, multiplication, modulus, floor-divisions and division operations. The program imports a logo art from the art module and a clear function from the replit module. The program prompts the user to enter a number, then presents a list of available operations, and prompts the user to select an operation. The program then prompts the user to enter another number, and performs the selected operation on the two numbers, displaying the result. The program allows the user to continue performing calculations with the result and provides the option to start a new calculation.

## Usage
To run the program, simply execute the calculator.py script in a Python environment. The program will display the logo, prompt the user to enter a number, present a list of available operations, and prompt the user to select an operation. The program will then prompt the user to enter another number, and performs the selected operation on the two numbers, displaying the result. The program allows the user to continue performing calculations with the result and provides the option to start a new calculation.

## Examples
```py
$ python calculator.py

 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|

What's the first number?: 1
+
-
*
/
Pick an operation: +
What's the next number?: 2
1.0 + 2.0 = 3.0
 
Enter the first number: 5
Pick an operator: +
Enter the next number: 10
5.0 + 10.0 = 15.0
Type 'yes' to continue calculating with 15.0.  or  type 'no' to start a new calculation 
yes
Pick an operator: *
Enter the next number: 2
15.0 * 2.0 = 30.0
Type 'yes' to continue calculating with 30.0.  or  type 'no' to start a new calculation 
```
## Note
+This program is using an imported module art and replit that contains the logo art and the clear function respectively.
+A test version is available on [replit](https://replit.com/@labelisaiah/calculator-start?v=1)
+Also, this program creates a loop that allows user to keep running the program as long as they want.

## Requirements
+ Python 3.x
+ import module art and replit

## Dependencies
This program has two dependencies art and replit modules, that should be available in the same directory as the calculator.py file.

## Limitations
The program does not handle upper case letters, special characters and digits.
The program assumes that the user will input valid integers or floats for the numbers.

## Contributions
+This is part of my Day 10 project of 100days of python code. Contributions and suggestions for improvements are welcome. If you would like to contribute to the development of this program, please fork the repository and submit a pull request with your proposed changes.

## License
This program is licensed under the **MIT License.**

## Acknowledgements
I would like to thank Dr. Angela Yu who has helped improve my understanding of Python and the basic calculator algorithm.

Thank you for using Calculator.
