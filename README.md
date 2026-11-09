# Stock Portfolio Tracker

A simple, beginner-friendly Python project built for the **CodeAlpha Python Internship**.

The program lets you enter the stocks you own and how many shares you have. It then calculates the total value of your investment, shows a clear breakdown, and saves the summary to files.

## Features

- Hardcoded dictionary of stock prices (AAPL, TSLA, GOOG, MSFT, AMZN)
- Enter as many stocks and quantities as you like
- Handles invalid stock symbols (e.g. `XYZ`)
- Handles invalid quantities (letters, decimals, zero, negative numbers)
- Entering the same stock twice adds the quantities together
- Clear table showing stock, quantity, price and total value
- Calculates the total investment value
- Saves the summary to `portfolio_summary.txt` and `portfolio_summary.csv`

## Stock Prices Used

| Symbol | Price (USD) |
|--------|-------------|
| AAPL   | 180.00      |
| TSLA   | 250.00      |
| GOOG   | 140.00      |
| MSFT   | 370.00      |
| AMZN   | 145.00      |

These are example prices stored in the `STOCK_PRICES` dictionary in `main.py`. You can edit them or add more stocks.

## Project Structure

```
stock-portfolio-tracker/
├── main.py            # The program
├── README.md          # This file
└── requirements.txt   # No external libraries needed
```

## How to Run in VS Code

1. **Install Python** from https://www.python.org/downloads/ (tick "Add Python to PATH" during installation on Windows).
2. **Install VS Code** from https://code.visualstudio.com/ and add the **Python extension** (open the Extensions tab with `Ctrl+Shift+X`, search "Python", click Install).
3. **Open the project folder**: go to `File > Open Folder...` and select `stock-portfolio-tracker`.
4. **Open `main.py`** from the Explorer panel on the left.
5. **Run it** using either method:
   - Click the **Run (▶)** button at the top-right of the editor, or
   - Open the terminal with `` Ctrl+` `` and type:
     ```
     python main.py
     ```
     (On Mac/Linux you may need `python3 main.py`.)
6. Follow the prompts in the terminal.

No `pip install` is needed because the project uses no external libraries.

## Example Run

```
Enter stock symbol (or 'done'): aapl
Enter quantity of AAPL: 10
  Added 10 share(s) of AAPL.

Enter stock symbol (or 'done'): tsla
Enter quantity of TSLA: 5
  Added 5 share(s) of TSLA.

Enter stock symbol (or 'done'): done

====================================================
            STOCK PORTFOLIO SUMMARY
====================================================
Stock     Quantity         Price     Total Value
----------------------------------------------------
AAPL            10       $180.00       $1,800.00
TSLA             5       $250.00       $1,250.00
----------------------------------------------------
TOTAL INVESTMENT VALUE:                    $3,050.00
====================================================
```

## Output Files

After the program finishes, two files appear in the project folder:

- `portfolio_summary.txt`: the formatted report with the date and time
- `portfolio_summary.csv`: the same data, which you can open in Excel or Google Sheets

## Python Concepts Used

- Dictionaries (stock prices and the portfolio)
- `while` and `for` loops
- `input()` and `print()`
- `try` / `except` for input validation
- Basic arithmetic (price × quantity)
- File handling with `open()` and `with`
- Functions to keep the code organized

## Ideas to Extend the Project

- Add more stocks to the dictionary
- Let the user remove or edit a stock
- Fetch live prices using an API (this would need an external library)
- Show the percentage share of each stock in the portfolio

## Author

Created by *(your name)* for the CodeAlpha Python Internship.
