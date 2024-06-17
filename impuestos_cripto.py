# Importar exceles de binance y calcular impuestos para la dec de la renta.

# Filter and arrange results of all columns

# Features:
    # select column (Date	Asset	Amount	Price per unit (EUR)	Value (EUR)	Transaction Type	Label)
    # select currency
    # options from the renta:
        # denominación (nombre moneda)
        # Identificación de lo recibido a cambio. Clave tipo de contraprestación (vender a fiat, vender por un servicio otro, cambiar a otra cripto)
            # F - moneda de curso legal, N - otra moneda virtual, O - otro activo virtual, B - bienes o servicios
        # adquisición
        # transmisión

import csv

def file_manager():
    while True:
        try:
            filename = input("Please enter the name of the file you want to read: ")
            with open(f"{filename}", newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                data = list(reader)
                return data
        except (FileNotFoundError, TypeError, ValueError):
            print("Please enter a valid filename")
        continue

def income_gains():
    data = file_manager()
    aggregated_data = {}
    
    for row in data:
        asset = row["Asset"]
        value = float(row["Value (EUR)"])
        label = row["Label"]

        if label == "Reward":
            if asset in aggregated_data:
                aggregated_data[asset] += value
            else:
                aggregated_data[asset] = value

    print("\nValue by asset:")
    for asset, total_value in aggregated_data.items():
        print(f"Asset: {asset}, Total value: €{total_value:.8f}")

    overall_value = sum(aggregated_data.values())
    print(f"\nTotal value: €{overall_value:.8f}")

def capital_gains():
    data = file_manager()
    aggregated_data = {}

    for row in data:
        coin = row["Currency name"]
        cost = float(row["Cost basis (EUR)"])
        sale = float(row["Proceeds (EUR)"])
        gains = float(row["Gains (EUR)"])
        type = row["Transaction type"]

        if coin not in aggregated_data:
            aggregated_data[coin] = {}

        if type not in aggregated_data[coin]:
            aggregated_data[coin][type] = {"Total Cost": 0.0, "Total Sale": 0.0, "Gains": 0.0}

            # Aggregate cost, sale and gains values by coin and transaction type
            aggregated_data[coin][type]["Total Cost"] += cost
            aggregated_data[coin][type]["Total Sale"] += sale
            aggregated_data[coin][type]["Gains"] += gains

    print("Data:")
    for coin, coin_data in aggregated_data.items():
        print(f"Currency: {coin}")
        for type, data in coin_data.items():
            total_cost = data["Total Cost"]
            total_sale = data["Total Sale"]
            total_gains = data["Gains"]
            print(f"Transaction Type: {type}\nTotal Cost: €{total_cost:.8f}\nTotal Sale: €{total_sale:.8f}\nGains: €{total_gains:.8f}\n")


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
        if start == "1":
            income_gains()
        elif start == "2":
            capital_gains()
        elif start == "3":
            break

main()

# columns = ["Date", "Asset", "Amount", "Price per unit (EUR)", "Value (EUR)", "Transaction Type", "Label"]