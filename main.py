"""
Stock Portfolio Tracker
CodeAlpha Python Internship Project

What this program does:
1. Shows a list of available stocks and their (hardcoded) prices.
2. Asks the user to enter stock symbols and quantities.
3. Calculates the total investment value.
4. Displays a clear breakdown of the portfolio.
5. Saves the summary to a TXT file and a CSV file.
"""

from datetime import datetime

# ---------------------------------------------------------------
# Hardcoded stock prices (in US dollars per share)
# ---------------------------------------------------------------
STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "GOOG": 140.00,
    "MSFT": 370.00,
    "AMZN": 145.00,
}

TXT_FILE = "portfolio_summary.txt"
CSV_FILE = "portfolio_summary.csv"


def show_available_stocks():
    """Print the list of stocks the user can choose from."""
    print("\nAvailable stocks:")
    print("-" * 24)
    for symbol, price in STOCK_PRICES.items():
        print(f"{symbol:<6} ${price:>8.2f}")
    print("-" * 24)


def get_quantity(symbol):
    """Keep asking until the user enters a valid whole number above 0."""
    while True:
        text = input(f"Enter quantity of {symbol}: ").strip()
        try:
            quantity = int(text)
        except ValueError:
            print("  Invalid quantity. Please enter a whole number (e.g. 5).")
            continue

        if quantity <= 0:
            print("  Quantity must be greater than 0.")
            continue

        return quantity


def collect_portfolio():
    """
    Ask the user for stocks and quantities.
    Returns a dictionary like {"AAPL": 10, "TSLA": 5}.
    """
    portfolio = {}

    print("\nEnter the stocks you own. Type 'done' when you are finished.")

    while True:
        symbol = input("\nEnter stock symbol (or 'done'): ").strip().upper()

        if symbol == "DONE":
            if len(portfolio) == 0:
                print("  You have not added any stocks yet. Add at least one.")
                continue
            break

        if symbol not in STOCK_PRICES:
            print(f"  '{symbol}' is not a valid stock symbol.")
            print("  Choose from: " + ", ".join(STOCK_PRICES.keys()))
            continue

        quantity = get_quantity(symbol)

        # If the stock was already entered, add to the existing quantity
        if symbol in portfolio:
            portfolio[symbol] += quantity
        else:
            portfolio[symbol] = quantity

        print(f"  Added {quantity} share(s) of {symbol}.")

    return portfolio


def calculate_portfolio(portfolio):
    """
    Work out the value of each holding and the grand total.
    Returns a list of rows and the total investment value.
    """
    rows = []
    total = 0.0

    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * quantity
        rows.append((symbol, quantity, price, value))
        total += value

    return rows, total


def build_report(rows, total):
    """Create the summary as a list of text lines (used for screen and file)."""
    lines = []
    lines.append("=" * 52)
    lines.append("            STOCK PORTFOLIO SUMMARY")
    lines.append("=" * 52)
    lines.append(f"{'Stock':<8}{'Quantity':>10}{'Price':>14}{'Total Value':>16}")
    lines.append("-" * 52)

    for symbol, quantity, price, value in rows:
        lines.append(f"{symbol:<8}{quantity:>10}{'$' + format(price, ',.2f'):>14}{'$' + format(value, ',.2f'):>16}")

    lines.append("-" * 52)
    lines.append(f"{'TOTAL INVESTMENT VALUE:':<32}{'$' + format(total, ',.2f'):>20}")
    lines.append("=" * 52)
    return lines


def save_txt(report_lines):
    """Save the report to a TXT file."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(TXT_FILE, "w", encoding="utf-8") as file:
        file.write(f"Generated on: {now}\n\n")
        for line in report_lines:
            file.write(line + "\n")


def save_csv(rows, total):
    """Save the portfolio to a CSV file (opens nicely in Excel)."""
    with open(CSV_FILE, "w", encoding="utf-8") as file:
        file.write("Stock,Quantity,Price,Total Value\n")
        for symbol, quantity, price, value in rows:
            file.write(f"{symbol},{quantity},{price:.2f},{value:.2f}\n")
        file.write(f"TOTAL,,,{total:.2f}\n")


def main():
    print("=" * 52)
    print("          WELCOME TO STOCK PORTFOLIO TRACKER")
    print("=" * 52)

    show_available_stocks()
    portfolio = collect_portfolio()

    rows, total = calculate_portfolio(portfolio)
    report_lines = build_report(rows, total)

    print()
    for line in report_lines:
        print(line)

    # Save to files (with simple error handling)
    try:
        save_txt(report_lines)
        save_csv(rows, total)
        print(f"\nSummary saved to '{TXT_FILE}' and '{CSV_FILE}'.")
    except OSError as error:
        print(f"\nSorry, the files could not be saved: {error}")

    print("Thank you for using Stock Portfolio Tracker!")


if __name__ == "__main__":
    main()
