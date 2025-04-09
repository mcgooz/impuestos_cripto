# Import Binance generated Excel files and calculate taxes for the Declaración de la Renta.

import csv

from scripts.tax_calculator import TaxCalculator


def options():
    options = {
        "1.": "Income gains", 
        "2.": "Capital gains",
        "3.": "Quit",
    }
    for option in options:
        print(f"{option} {options[option]}")

def main():
    while True:
        options()
        start = input("Please choose an option: ")
        if start.strip() == "1":
            income_gains()
        elif start.strip() == "2":
            capital_gains()
        elif start.strip() == "3":
            break

def income_gains():
    print("\nIncome Gains Calculation")
    while True:
        filename = input("Please enter the path and name of the file (e.g., csv_files/incomegains24.csv ): ")
        try:
            calculator = TaxCalculator(filename)
            calculator.income_gains()
            break
        except (FileNotFoundError, TypeError, ValueError):
            print("Error: The file could not be found. Please enter a valid filename.")
            next = input("Press 1 to try again or 0 to go back: ")
            if next == "0":
                break
        except (KeyError, csv.Error):
            print("Error: The file couldnot be read. Please ensure it is a valid CSV file.")
            next = input("Press 1 to try again or 0 to go back: ")
            if next == "0":
                break


def capital_gains():
    print("\nCapital Gains Calculation")
    while True:
        filename = input("Please enter the path and name of the file (e.g., csv_files/captialgains24.csv ): ")
        try:
            calculator = TaxCalculator(filename)
            calculator.capital_gains()
            break
        except (FileNotFoundError, TypeError, ValueError):
            print("Error: The file could not be found. Please enter a valid filename.")
            next = input("Press 1 to try again or 0 to go back: ")
            if next.strip() == "0":
                break
        except (KeyError, csv.Error):
            print("Error: The file couldnot be read. Please ensure it is a valid CSV file.")
            next = input("Press 1 to try again or 0 to go back: ")
            if next.strip() == "0":
                break


if __name__ == "__main__":
    main()

# columns = ["Date", "Asset", "Amount", "Price per unit (EUR)", "Value (EUR)", "Transaction Type", "Label"]