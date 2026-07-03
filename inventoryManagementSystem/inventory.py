import sqlite3

def connect_db():
    """Establishes connection to the local database file."""
    return sqlite3.connect('inventory.db')

def create_tables():
    """Creates the essential tables if they do not exist already."""
    conn = connect_db()
    cursor = conn.cursor()
    # Core products configuration table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT,
            price REAL NOT NULL,
            stock_quantity INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_product(name, category, price, quantity):
    """Inserts a brand-new retail item into the stock table."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO products (name, category, price, stock_quantity) 
        VALUES (?, ?, ?, ?)
    ''', (name, category, price, quantity))
    conn.commit()
    conn.close()
    print(f"\n Product {name} added successfully!")

def view_all_products():
    """Fetches and reads all valid data entries sequentially."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    items = cursor.fetchall()
    conn.close()
    return items

def update_stock(product_id, new_quantity):
    """Modifies the active available units metric for a item."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE products 
        SET stock_quantity = ? 
        WHERE product_id = ?
    ''', (new_quantity, product_id))
    conn.commit()
    changes = cursor.rowcount
    conn.close()
    return changes > 0

def delete_product(product_id):
    """Permanently drops an entry out of the table by its index key."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM products WHERE product_id = ?', (product_id,))
    conn.commit()
    changes = cursor.rowcount
    conn.close()
    return changes > 0

def display_menu():
    print("\n========= WAREHOUSE INVENTORY MANAGEMENT =========")
    print("1. Add New Product Line")
    print("2. Display All Available Stock")
    print("3. Modify Existing Item Stock Level")
    print("4. Remove Product Records")
    print("5. Terminate Application")
    print("==================================================")

def main():
    # Make sure tables exist right at runtime launch
    create_tables()
    print("Database tables initialized successfully.")
    
    while True:
        display_menu()
        choice = input("Enter choice (1-5): ").strip()
        
        if choice == '1':
            name = input("Enter product title name: ")
            category = input("Enter sub-category tier: ")
            price = float(input("Enter purchase price value: $"))
            quantity = int(input("Enter initial warehouse unit quantity count: "))
            add_product(name, category, price, quantity)
            
        elif choice == '2':
            items = view_all_products()
            if not items:
                print("\n The inventory log is currently empty.")
            else:
                print(f"\n{'ID':<5} | {'Product Name':<20} | {'Category':<15} | {'Price':<8} | {'Stock':<6}")
                print("-" * 65)
                for item in items:
                    print(f"{item[0]:<5} | {item[1]:<20} | {item[2]:<15} | ${item[3]:<7.2f} | {item[4]:<6}")
                    
        elif choice == '3':
            prod_id = int(input("Enter unique Target Product ID: "))
            new_qty = int(input("Enter newly updated physical asset unit count: "))
            if update_stock(prod_id, new_qty):
                print("\n Target inventory level adjusted successfully.")
            else:
                print("\n Failed: Product ID record match not found.")
                
        elif choice == '4':
            prod_id = int(input("Enter Product ID to permanently wipe: "))
            confirm = input(f"Are you sure you want to delete Product #{prod_id}? (y/n): ").lower()
            if confirm == 'y':
                if delete_product(prod_id):
                    print("\n Product row eliminated cleanly from logs.")
                else:
                    print("\n Failed: Product ID record match not found.")
                    
        elif choice == '5':
            print("\nShutting down software instance safely... Goodbye!")
            break
            
        else:
            print("\n Invalid choice layout pattern selection. Try again.")

if __name__ == "__main__":
    main()
