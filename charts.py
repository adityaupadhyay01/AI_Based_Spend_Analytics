import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


def show_chart():

    conn = sqlite3.connect("expenses.db")

    df = pd.read_sql_query("SELECT * FROM expenses", conn)

    conn.close()

    if df.empty:
        print("No expenses available to visualize.")
        return

    # category wise total
    category_sum = df.groupby("category")["amount"].sum()

    # Pie Chart
    plt.figure()
    category_sum.plot(kind="pie", autopct="%1.1f%%")

    plt.title("Expense Distribution by Category")

    plt.ylabel("")

    plt.show()

    # Bar Chart
    plt.figure()

    category_sum.plot(kind="bar")

    plt.title("Category Wise Spending")

    plt.xlabel("Category")

    plt.ylabel("Amount")

    plt.show()