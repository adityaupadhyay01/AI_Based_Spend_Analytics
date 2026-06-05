import sqlite3
from analysis import show_summary
from charts import show_chart


def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food/Travel/Shopping/etc): ")
    amount = float(input("Enter amount: "))

    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO expenses(date, category, amount) VALUES (?, ?, ?)",
        (date, category, amount)
    )

    conn.commit()
    conn.close()

    print("Expense added successfully!")


def view_expenses():

    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()

    print("\n---- All Expenses ----")

    for row in rows:
        print(row)

    conn.close()


def main():

    while True:

        print("\n====== AI Spend Analytics ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Category Analysis")
        print("4. Show Chart")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            show_summary()

        elif choice == "4":
            show_chart()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()