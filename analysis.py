import sqlite3
import pandas as pd


def show_summary():

    conn = sqlite3.connect("expenses.db")

    # database se data pandas dataframe me load
    df = pd.read_sql_query("SELECT * FROM expenses", conn)

    conn.close()

    if df.empty:
        print("No expenses found.")
        return

    print("\n===== Category Wise Summary =====")

    category_summary = df.groupby("category")["amount"].sum()

    print(category_summary)

    total_expense = df["amount"].sum()

    print("\nTotal Expense:", total_expense)