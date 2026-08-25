# Python Assignment: Personal Income & Expense Tracker

Create a **console-based Personal Income and Expense Tracker in Python**.

The purpose of this assignment is to practice **functions, lists, dictionaries, CSV files, loops, conditions, exception handling, and dates**.

## 1. CSV File

Use a file named `expenses.csv` to store all transactions.

The CSV must have these columns:

```text
date,type,category,description,amount
```

Example:

```text
2026-08-21,Income,Salary,August Salary,50000
2026-08-21,Expense,Food,Lunch,250
```

When the program starts, load existing data from the CSV file. If the file does not exist, start with an empty list.

## 2. Main Menu

Display a menu like:

```text
1. Add Expense
2. Add Income
3. View Transactions
4. Reports
5. Save
6. Save & Exit
```

Keep showing the menu until the user chooses **Save & Exit**.

## 3. Add Expense / Income

Allow the user to enter:

* Category
* Description
* Amount

The program should automatically add the current date.

The transaction type should be either `Expense` or `Income`.

The amount must be:

* A valid number
* Greater than zero

Invalid input should not crash the program. Ask the user again.

## 4. View Transactions

Display all transactions in a readable table containing:

* Number
* Date
* Type
* Category
* Description
* Amount

If there are no transactions, display an appropriate message.

## 5. Reports

Create a Reports menu with:

```text
1. Financial Summary
2. Expense by Category
3. Monthly Report
4. Transaction History
5. Back to Main Menu
```

### Financial Summary

Display:

```text
Total Income
Total Expense
Balance
```

Calculate:

```text
Balance = Total Income - Total Expense
```

### Expense by Category

Show the total expense for each category.

For example:

```text
Food          2500.00
Travel        1800.00
Shopping      1200.00
```

Show categories from highest expense to lowest.

### Monthly Report

Group transactions by month and display:

```text
2026-08
  Income  : 50000.00
  Expense : 12500.00
  Balance : 37500.00
```

## 6. Save

When the user selects **Save**, write all transactions back to `expenses.csv`.

When the user selects **Save & Exit**, save the data first and then exit.

## 7. Program Structure

Use separate functions for major tasks, such as:

* Loading data
* Saving data
* Adding transactions
* Displaying transactions
* Financial summary
* Category report
* Monthly report
* Reports menu
* Main program

Do not put the complete program inside one large function.

## 8. Error Handling

The program should handle:

* Invalid menu choices
* Invalid amount input
* Zero or negative amounts
* Missing CSV file

The program should not crash because of normal user mistakes.

## 9. Testing

Test at least these cases:

1. Start when the CSV file does not exist.
2. Add income.
3. Add expense.
4. Enter an invalid amount.
5. Enter a negative amount.
6. Check the financial summary.
7. Check category totals.
8. Check the monthly report.
9. Save and restart the program to confirm that data is loaded.

## 10. Submission

Submit:

* `expense_tracker.py`
* `expenses.csv`
* A short explanation of the program and its main functions.

### Optional Extra Features

For extra practice, you may add:

* Edit transaction
* Delete transaction
* Search transactions
* Filter by month
* Show highest expense
* Set category budgets

**Important:** Complete all required features before attempting the optional features.
