# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 320,
    "AMZN": 140
}

portfolio = {}
total_investment = 0

# Number of different stocks
n = int(input("Enter the number of stocks you want to add: "))

# Taking user input
for i in range(n):
    stock_name = input("Enter stock name (AAPL, TSLA, GOOGL, MSFT, AMZN): ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stock_prices:
        portfolio[stock_name] = quantity
    else:
        print("Stock not available!")

# Calculating total investment
print("\n----- Portfolio Summary -----")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_investment += value
    print(f"{stock} : {qty} shares × ${stock_prices[stock]} = ${value}")

print("\nTotal Investment Value = $", total_investment)

# Save result to a text file
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("-------------------------\n")
    for stock, qty in portfolio.items():
        value = stock_prices[stock] * qty
        file.write(f"{stock} : {qty} shares × ${stock_prices[stock]} = ${value}\n")
    file.write(f"\nTotal Investment Value = ${total_investment}")

print("\nPortfolio details saved successfully in 'portfolio.txt'")