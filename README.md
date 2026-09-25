# Python Calculator

A command-line calculator application written in Python.

The project includes two main calculator modes:

1. **General Calculator** — performs common mathematical operations.
2. **Financial Calculator** — performs several common financial calculations.

The program includes input validation and handles common errors such as invalid input, division by zero, and square roots of negative numbers.

---

## Features

### General Calculator

The General Calculator supports the following operations:

- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`)
- Power (`**`)
- Square Root (`sqrt`)

The calculator validates user input and asks the user to enter a new value when invalid data is provided.

Examples of handled errors:

- Entering text instead of a number
- Division by zero
- Square root of a negative number
- Invalid mathematical operation

---

### Financial Calculator

The Financial Calculator provides five financial functions:

#### 1. Loan Monthly Payment

Calculates the monthly payment for a loan using a fixed annual interest rate of **12%**.

User inputs:

- Loan amount
- Loan period in years

The program calculates the required monthly payment using the standard loan amortization formula.

---

#### 2. Future Value

Calculates the future value of an investment.

User inputs:

- Present value
- Annual interest rate
- Number of years

Formula:

`FV = PV × (1 + r)^n`

Where:

- `FV` = Future Value
- `PV` = Present Value
- `r` = Annual interest rate
- `n` = Number of years

---

#### 3. Present Value

Calculates the present value of a future amount.

User inputs:

- Future value
- Annual discount rate
- Number of years

Formula:

`PV = FV / (1 + r)^n`

---

#### 4. Compound Interest

Calculates the final value of an investment with compound interest.

User inputs:

- Initial amount
- Annual interest rate
- Number of years
- Number of compounding periods per year

The calculator displays:

- Final amount
- Total interest earned

Formula:

`A = P × (1 + r/n)^(n×t)`

Where:

- `A` = Final amount
- `P` = Principal
- `r` = Annual interest rate
- `n` = Number of compounding periods per year
- `t` = Number of years

---

#### 5. Investment Return (CAGR)

Calculates the **Compound Annual Growth Rate (CAGR)** of an investment.

User inputs:

- Beginning investment value
- Ending investment value
- Number of years

Formula:

`CAGR = (Ending Value / Beginning Value)^(1 / Years) - 1`

The result is displayed as a percentage.

---

## Main Menu

When the program starts, the user can choose between the two calculators:

```text
MAIN MENU

1. General Calculator
2. Financial Calculator
0. Exit
```

The Financial Calculator has its own menu:

```text
FINANCIAL CALCULATOR

Choose operation:

1. Loan Monthly Payment
2. Future Value
3. Present Value
4. Compound Interest
5. Investment Return (CAGR)
0. Back to Main Menu
```

---

## Requirements

- Python 3.x

The project uses only Python's standard library.

The `math` module is used for square root calculations.

No external packages are required.

---

## How to Run

Clone the repository or download the project files.

Open the project directory in the terminal and run:

```bash
python3 main.py
```

If you are using a virtual environment, activate it first:

### macOS / Linux

```bash
source .venv/bin/activate
```

Then run:

```bash
python3 main.py
```

---

## Project Structure

```text
project-folder/
│
├── main.py
├── README.md
└── requirements.txt
```

Because the project currently uses only Python's standard library, `requirements.txt` does not need any external dependencies.

---

## Input Validation

The program uses `try` / `except` blocks and conditional checks to handle incorrect user input.

For example, it prevents:

```text
Enter first number: hello
Error: Please enter a valid number.
```

It also prevents division by zero:

```text
Enter second number: 0
Error: Cannot divide by zero.
```

And square roots of negative numbers:

```text
Enter first number: -25
Error: Cannot calculate square root of a negative number.
```

---

## Technologies Used

- Python
- Python `math` module
- Functions
- Loops
- Dictionaries
- Exception handling
- Conditional statements
- User input validation

---

## Possible Future Improvements

Future versions of the project could include:

- Graphical User Interface (GUI)
- User-selectable loan interest rates
- Additional financial calculations
- Currency formatting
- Calculation history
- Saving calculations to a file
- Unit tests
- More advanced scientific calculator functions

---

## Author

Created as a Python midterm project.
