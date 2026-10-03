# Simple Stock Investment Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 190
}

total_investment = 0

print("===== Stock Investment Tracker =====")
print("\nAvailable Stocks:")

for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

print("\nEnter 'done' when you finish adding stocks.\n")

while True:
    stock_name = input("Enter stock name: ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Stock not available. Please choose from the available stocks.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock_name}: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        price = stock_prices[stock_name]
        investment = price * quantity

        print(f"{stock_name} Price: ${price}")
        print(f"Investment in {stock_name}: ${investment}\n")

        total_investment += investment

    except ValueError:
        print("Please enter a valid quantity.\n")


print("\n===== Investment Summary =====")
print(f"Total Investment Value: ${total_investment}")

# Save result to a text file
with open("investment_result.txt", "w") as file:
    file.write("Stock Investment Tracker\n")
    file.write("========================\n")
    file.write(f"Total Investment Value: ${total_investment}\n")

print("Result saved to investment_result.txt")