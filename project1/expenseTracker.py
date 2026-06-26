import sqlite3

class ExpenseTracker:
    def __init__(self):
        self.conn = sqlite3.connect("expenses.db")
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_name TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                unit_price REAL NOT NULL,
                total_price REAL NOT NULL
            )
        """)
        self.conn.commit()

    def add_expenses(self):
        item_name = input("Enter Item Name : ")
        quantity = int(input("Enter Quantity : "))
        unit_price = float(input("Enter Unit Price : "))
        total_price = quantity * unit_price
        
        self.cursor.execute("""
            INSERT INTO expenses(item_name, quantity, unit_price, total_price)
            VALUES (?, ?, ?, ?)
        """, (item_name, quantity, unit_price, total_price))
        self.conn.commit()
        print("Expense added successfully!\n")

    def view_expenses(self):
        self.cursor.execute("SELECT * FROM expenses")
        records = self.cursor.fetchall()
        
        if not records:
            print("No records found\n")
            return
            
        print("\n Expense List ")
        for row in records:
            print(
                f"ID: {row[0]} | "
                f"Item: {row[1]} | "
                f"Quantity: {row[2]} | "
                f"Unit Price: Rs.{row[3]:.2f} | "
                f"Total Price: Rs.{row[4]:.2f}"
            )
        print("\n")

    def update_expenses(self):
        expense_id = int(input("Enter Expense ID to Update : "))
        quantity = int(input("Enter New Quantity : "))
        unit_price = float(input("Enter New Unit Price : "))
        total_price = quantity * unit_price
        
        self.cursor.execute("""
            UPDATE expenses 
            SET quantity=?, unit_price=?, total_price=? 
            WHERE id=?
        """, (quantity, unit_price, total_price, expense_id))
        self.conn.commit()
        print("Expense updated successfully!\n")

    def delete_expenses(self):
        expense_id = int(input("Enter Expense ID to delete : "))
        # Note the trailing comma in (expense_id,) to create a valid tuple
        self.cursor.execute("DELETE FROM expenses WHERE id=?", (expense_id,))
        self.conn.commit()
        print("Expense deleted successfully!\n")

    def close_connection(self):
        self.conn.close()
        print("Database connection closed. Goodbye!")

def main():
    tracker = ExpenseTracker()
    while True:
        print("Expenses Tracker")
        print("1) Add Expenses")
        print("2) View Expenses")
        print("3) Update Expenses")
        print("4) Delete Expenses")
        print("5) Exit")
        
        choice = input("Enter Your Choice (1-5): ")
        
        if choice == "1":
            tracker.add_expenses()
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            tracker.update_expenses() # Fixed order here
        elif choice == "4":
            tracker.delete_expenses() # Fixed order here
        elif choice == "5":
            tracker.close_connection()
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.\n")


main()
