import math
from logger import logger


# Only the chosen operation is evaluated
OPERATIONS = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "**": lambda a, b: a ** b,
    "root": lambda a, b: a ** (1 / b),
    "log": lambda a, b: math.log(a, b),
}


def general_calculator():

    logger.info("General Calculator opened")

    # First number
    while True:
        try:
            num1 = float(input("Enter first number: "))
            break

        except ValueError:
            print("Error: Please enter a valid number.")
            logger.warning("Invalid first number entered in General Calculator")

    # Operation
    while True:
        operation = input(
            "Choose operation (+, -, *, /, **, root, log): "
        )

        if operation in OPERATIONS:
            break
        else:
            print("Error: Invalid operation. Please try again.")
            logger.warning(
                f"Invalid operation entered in General Calculator: {operation}"
            )

    # Second number
    while True:
        try:
            num2 = float(input("Enter second number: "))

            if operation == "/" and num2 == 0:
                print("Error: Cannot divide by zero.")
                logger.warning("Division by zero attempted")
                continue

            if operation == "root" and num2 == 0:
                print("Error: Root degree cannot be zero.")
                logger.warning("Root with degree zero attempted")
                continue

            if operation == "log":

                if num1 <= 0:
                    print("Error: Logarithm value must be greater than zero.")
                    logger.warning(
                        f"Invalid logarithm value entered: {num1}"
                    )
                    continue

                if num2 <= 0 or num2 == 1:
                    print(
                        "Error: Logarithm base must be greater than zero "
                        "and cannot be 1."
                    )
                    logger.warning(
                        f"Invalid logarithm base entered: {num2}"
                    )
                    continue

            break

        except ValueError:
            print("Error: Please enter a valid number.")
            logger.warning(
                "Invalid second number entered in General Calculator"
            )

    # Calculation
    result = OPERATIONS[operation](num1, num2)

    print(f"\nResult: {result}")

    logger.info(
        f"General Calculator: {num1} {operation} {num2} = {result}"
    )


def financial_calculator():

    logger.info("Financial Calculator opened")

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
            logger.info("Returned from Financial Calculator to Main Menu")
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
                        logger.warning(
                            f"Invalid loan amount entered: {loan_amount}"
                        )
                        continue

                    break

                except ValueError:
                    print("Error: Please enter a valid number.")
                    logger.warning("Invalid loan amount entered")

            while True:
                try:
                    years = int(input("Enter loan period in years: "))

                    if years <= 0:
                        print(
                            "Error: Number of years must be greater than zero."
                        )
                        logger.warning(
                            f"Invalid loan period entered: {years}"
                        )
                        continue

                    break

                except ValueError:
                    print("Error: Please enter a valid whole number.")
                    logger.warning("Invalid loan period entered")

            monthly_interest_rate = annual_interest_rate / 12
            number_of_payments = years * 12

            monthly_payment = (
                loan_amount
                * monthly_interest_rate
                * (1 + monthly_interest_rate) ** number_of_payments
                / ((1 + monthly_interest_rate) ** number_of_payments - 1)
            )

            print(
                f"\nAnnual interest rate: "
                f"{annual_interest_rate * 100}%"
            )
            print(f"Monthly payment: {monthly_payment:.2f}")

            logger.info(
                f"Loan Monthly Payment: "
                f"loan={loan_amount}, "
                f"years={years}, "
                f"interest={annual_interest_rate * 100}%, "
                f"monthly_payment={monthly_payment:.2f}"
            )

        # --------------------------------
        # 2. Future Value
        # --------------------------------

        elif operation == "2":

            while True:
                try:
                    present_value = float(
                        input("Enter present value: ")
                    )

                    interest_rate = float(
                        input("Enter annual interest rate (%): ")
                    )

                    years = int(
                        input("Enter number of years: ")
                    )

                    if (
                        present_value < 0
                        or interest_rate < 0
                        or years <= 0
                    ):
                        print("Error: Please enter positive values.")
                        logger.warning(
                            "Invalid values entered for "
                            "Future Value calculation"
                        )
                        continue

                    break

                except ValueError:
                    print("Error: Please enter valid numbers.")
                    logger.warning(
                        "Invalid input entered for "
                        "Future Value calculation"
                    )

            rate = interest_rate / 100

            future_value = present_value * (1 + rate) ** years

            print(f"\nFuture Value: {future_value:.2f}")

            logger.info(
                f"Future Value: "
                f"present_value={present_value}, "
                f"interest_rate={interest_rate}%, "
                f"years={years}, "
                f"future_value={future_value:.2f}"
            )

        # --------------------------------
        # 3. Present Value
        # --------------------------------

        elif operation == "3":

            while True:
                try:
                    future_value = float(
                        input("Enter future value: ")
                    )

                    interest_rate = float(
                        input("Enter annual discount rate (%): ")
                    )

                    years = int(
                        input("Enter number of years: ")
                    )

                    if (
                        future_value < 0
                        or interest_rate < 0
                        or years <= 0
                    ):
                        print("Error: Please enter positive values.")
                        logger.warning(
                            "Invalid values entered for "
                            "Present Value calculation"
                        )
                        continue

                    break

                except ValueError:
                    print("Error: Please enter valid numbers.")
                    logger.warning(
                        "Invalid input entered for "
                        "Present Value calculation"
                    )

            rate = interest_rate / 100

            present_value = future_value / (1 + rate) ** years

            print(f"\nPresent Value: {present_value:.2f}")

            logger.info(
                f"Present Value: "
                f"future_value={future_value}, "
                f"discount_rate={interest_rate}%, "
                f"years={years}, "
                f"present_value={present_value:.2f}"
            )

        # --------------------------------
        # 4. Compound Interest
        # --------------------------------

        elif operation == "4":

            while True:
                try:
                    principal = float(
                        input("Enter initial amount: ")
                    )

                    interest_rate = float(
                        input("Enter annual interest rate (%): ")
                    )

                    years = int(
                        input("Enter number of years: ")
                    )

                    compounds_per_year = int(
                        input(
                            "Enter number of compounding "
                            "periods per year: "
                        )
                    )

                    if (
                        principal < 0
                        or interest_rate < 0
                        or years <= 0
                        or compounds_per_year <= 0
                    ):
                        print("Error: Please enter positive values.")
                        logger.warning(
                            "Invalid values entered for "
                            "Compound Interest calculation"
                        )
                        continue

                    break

                except ValueError:
                    print("Error: Please enter valid numbers.")
                    logger.warning(
                        "Invalid input entered for "
                        "Compound Interest calculation"
                    )

            rate = interest_rate / 100

            final_amount = principal * (
                1 + rate / compounds_per_year
            ) ** (compounds_per_year * years)

            interest_earned = final_amount - principal

            print(f"\nFinal Amount: {final_amount:.2f}")
            print(f"Interest Earned: {interest_earned:.2f}")

            logger.info(
                f"Compound Interest: "
                f"principal={principal}, "
                f"interest_rate={interest_rate}%, "
                f"years={years}, "
                f"compounds_per_year={compounds_per_year}, "
                f"final_amount={final_amount:.2f}, "
                f"interest_earned={interest_earned:.2f}"
            )

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

                    years = int(
                        input("Enter number of years: ")
                    )

                    if (
                        beginning_value <= 0
                        or ending_value < 0
                        or years <= 0
                    ):
                        print(
                            "Error: Please enter valid positive values."
                        )
                        logger.warning(
                            "Invalid values entered for CAGR calculation"
                        )
                        continue

                    break

                except ValueError:
                    print("Error: Please enter valid numbers.")
                    logger.warning(
                        "Invalid input entered for CAGR calculation"
                    )

            cagr = (
                (ending_value / beginning_value) ** (1 / years)
                - 1
            )

            print(f"\nCAGR: {cagr * 100:.2f}%")

            logger.info(
                f"CAGR: "
                f"beginning_value={beginning_value}, "
                f"ending_value={ending_value}, "
                f"years={years}, "
                f"cagr={cagr * 100:.2f}%"
            )

        else:
            print("Error: Invalid operation. Please choose 0-5.")
            logger.warning(
                f"Invalid Financial Calculator menu choice: {operation}"
            )


def calculator():

    logger.info("Calculator application started")

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
            logger.info("Calculator application closed")
            break

        else:
            print(
                "Error: Invalid choice. Please enter 0, 1, or 2."
            )
            logger.warning(
                f"Invalid Main Menu choice: {choice}"
            )


if __name__ == "__main__":
    calculator()