import csv

class TaxCalculator:

    def __init__(self, filename):
        self.filename = filename
        self.data = self._load_data()

    def _load_data(self):
        with open(f"{self.filename}", newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)
            return data

    def income_gains(self):
        aggregated_data = {}
        
        for row in self.data:
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
            if total_value < 0:
                print(f"Asset: {asset}, Total value: -€{abs(total_value):.8f}\n")
            else:
                print(f"Asset: {asset}, Total value: €{total_value:.8f}\n")

        overall_value = sum(aggregated_data.values())
        print(f"Total value: €{overall_value:.8f}\n")


    def capital_gains(self):
        aggregated_data = {}

        for row in self.data:
            coin = row["Currency name"]
            cost = float(row["Cost basis (EUR)"])
            sale = float(row["Proceeds (EUR)"])
            gains = float(row["Gains (EUR)"])
            type = row["Transaction type"]
            # F - moneda de curso legal, N - otra moneda virtual, O - otro activo virtual, B - bienes o servicios
            if type == "Trade":
                type += " (N - otra moneda virtual)"
            elif type == "Sell":
                type += " (F - moneda de curso legal)"
            elif type == "Send":
                type += " (B - bienes o servicios)"
            elif type == "Fee":
                type += " (Gastos)"          

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
                if total_gains < 0:
                    print(f"Transaction Type: {type}\nTotal Cost (Valor de adquisición): €{total_cost:.8f}\nTotal Sale (Valor de transmisión): €{total_sale:.8f}\nGains: -€{abs(total_gains):.8f}\n")
                else:
                    print(f"Transaction Type: {type}\nTotal Cost (Valor de adquisición): €{total_cost:.8f}\nTotal Sale (Valor de transmisión): €{total_sale:.8f}\nGains: €{total_gains:.8f}\n")