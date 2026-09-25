import math


def general_calculator():

    while True:
        operation = input("Choose operation (+, -, *, /, **, sqrt): ")

        if operation in ["+", "-", "*", "/", "**", "sqrt"]:
            break
        else:
            print("Error: Invalid operation. Please try again.")

    # First number
    while True:
        try:
            num1 = float(input("Enter first number: "))

            if operation == "sqrt" and num1 < 0:
                print("Error: Cannot calculate square root of a negative number.")
                continue

            break

        except ValueError:
            print("Error: Please enter a valid number.")

    # Square root only needs one number
    if operation == "sqrt":
        result = math.sqrt(num1)

    else:

        # Second number
        while True:
            try:
                num2 = float(input("Enter second number: "))

                if operation == "/" and num2 == 0:
                    print("Error: Cannot divide by zero.")
                    continue

                break

            except ValueError:
                print("Error: Please enter a valid number.")

        # Calculation
        result = {
                 (operation == "+"): num1 + num2,
                 (operation == "-"): num1 - num2,
                 (operation == "*"): num1 * num2,
                 (operation == "/"): num1 / num2,
                 (operation == "**"): num1 ** num2
                }[True]

    print(f"\nResult: {result}")


def financial_calculator():

    # Fixed annual interest rate for loan calculations
    annual_interest_rate = 0.12

    while True:

        print("\nFINANCIAL CALCULATOR")
        print()
        print("Choose operation:")
        print()
        print("1. Loan Monthly Payment")
        print("2. Future Value")
        print("3. Present Value")
        print("4. Compound Interest")
        print("5. Investment Return (CAGR)")
        print("0. Back to Main Menu")

        operation = input("\nChoose operation: ")

        # Back to Main Menu
        if operation == "0":
            return

        # --------------------------------
        # 1. Loan Monthly Payment
        # --------------------------------

        elif operation == "1":

            while True:
                try:
                    loan_amount = float(input("Enter loan amount: "))

                    if loan_amount <= 0:
                        print("Error: Loan amount must be greater than zero.")
                        continue

                    break

                except ValueError:
                    print("Error: Please enter a valid number.")

            while True:
                try:
                    years = int(input("Enter loan period in years: "))

                    if years <= 0:
                        print("Error: Number of years must be greater than zero.")
                        continue

                    break

                except ValueError:
                    print("Error: Please enter a valid whole number.")

            monthly_interest_rate = annual_interest_rate / 12

            number_of_payments = years * 12

            monthly_payment = (
                loan_amount
                * monthly_interest_rate
                * (1 + monthly_interest_rate) ** number_of_payments
                / ((1 + monthly_interest_rate) ** number_of_payments - 1)
            )

            print(f"\nAnnual interest rate: {annual_interest_rate * 100}%")
            print(f"Monthly payment: {monthly_payment:.2f}")

        # --------------------------------
        # 2. Future Value
        # --------------------------------

        elif operation == "2":

            while True:
                try:
                    present_value = float(input("Enter present value: "))
                    interest_rate = float(
                        input("Enter annual interest rate (%): ")
                    )
                    years = int(input("Enter number of years: "))

                    if present_value < 0 or interest_rate < 0 or years <= 0:
                        print("Error: Please enter positive values.")
                        continue

                    break

                except ValueError:
                    print("Error: Please enter valid numbers.")

            rate = interest_rate / 100

            future_value = present_value * (1 + rate) ** years

            print(f"\nFuture Value: {future_value:.2f}")

        # --------------------------------
        # 3. Present Value
        # --------------------------------

        elif operation == "3":

            while True:
                try:
                    future_value = float(input("Enter future value: "))
                    interest_rate = float(
                        input("Enter annual discount rate (%): ")
                    )
                    years = int(input("Enter number of years: "))

                    if future_value < 0 or interest_rate < 0 or years <= 0:
                        print("Error: Please enter positive values.")
                        continue

                    break

                except ValueError:
                    print("Error: Please enter valid numbers.")

            rate = interest_rate / 100

            present_value = future_value / (1 + rate) ** years

            print(f"\nPresent Value: {present_value:.2f}")

        # --------------------------------
        # 4. Compound Interest
        # --------------------------------

        elif operation == "4":

            while True:
                try:
                    principal = float(input("Enter initial amount: "))

                    interest_rate = float(
                        input("Enter annual interest rate (%): ")
                    )

                    years = int(input("Enter number of years: "))

                    compounds_per_year = int(
                        input("Enter number of compounding periods per year: ")
                    )

                    if (
                        principal < 0
                        or interest_rate < 0
                        or years <= 0
                        or compounds_per_year <= 0
                    ):
                        print("Error: Please enter positive values.")
                        continue

                    break

                except ValueError:
                    print("Error: Please enter valid numbers.")

            rate = interest_rate / 100

            final_amount = principal * (
                1 + rate / compounds_per_year
            ) ** (compounds_per_year * years)

            interest_earned = final_amount - principal

            print(f"\nFinal Amount: {final_amount:.2f}")
            print(f"Interest Earned: {interest_earned:.2f}")

        # --------------------------------
        # 5. Investment Return (CAGR)
        # --------------------------------

        elif operation == "5":

            while True:
                try:
                    beginning_value = float(
                        input("Enter beginning investment value: ")
                    )

                    ending_value = float(
                        input("Enter ending investment value: ")
                    )

                    years = int(input("Enter number of years: "))

                    if beginning_value <= 0 or ending_value < 0 or years <= 0:
                        print("Error: Please enter valid positive values.")
                        continue

                    break

                except ValueError:
                    print("Error: Please enter valid numbers.")

            cagr = (
                (ending_value / beginning_value) ** (1 / years)
                - 1
            )

            print(f"\nCAGR: {cagr * 100:.2f}%")

        else:
            print("Error: Invalid operation. Please choose 0-5.")


def calculator():

    while True:

        print("\nMAIN MENU")
        print()
        print("1. General Calculator")
        print("2. Financial Calculator")
        print("0. Exit")

        choice = input("\nChoose calculator: ")

        if choice == "1":
            general_calculator()

        elif choice == "2":
            financial_calculator()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Error: Invalid choice. Please enter 0, 1, or 2.")


if __name__ == "__main__":
    calculator()