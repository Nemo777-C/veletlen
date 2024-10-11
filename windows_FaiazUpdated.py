import sqlite3
from tkinter import *
from tkinter import messagebox
import db  # Importing db.py to handle the database connection

import sqlite3
from tkinter import *
from tkinter import messagebox, ttk

# Function to add a new row to the specified table
def add_new_row(table_name, columns, values):
    conn = sqlite3.connect('warehouse.db')
    c = conn.cursor()
    column_string = ', '.join(columns)
    placeholders = ', '.join(['?'] * len(values))
    query = f"INSERT INTO {table_name} ({column_string}) VALUES ({placeholders})"
    c.execute(query, values)
    conn.commit()
    conn.close()

# Function to read data from a table
def list_rows(table_name):
    conn = sqlite3.connect('warehouse.db')
    c = conn.cursor()
    c.execute(f"SELECT * FROM {table_name}")
    rows = c.fetchall()
    conn.close()
    return rows

# Function to update a row in the specified table
def update_row(table_name, row_id, updates):
    conn = sqlite3.connect('warehouse.db')
    c = conn.cursor()
    update_string = ', '.join([f"{col} = ?" for col in updates.keys()])
    values = list(updates.values()) + [row_id]
    c.execute(f"UPDATE {table_name} SET {update_string} WHERE {table_name[:-1]}_id = ?", values)
    conn.commit()
    conn.close()

# Function to delete a row from the specified table
def delete_row(table_name, row_id):
    conn = sqlite3.connect('warehouse.db')
    c = conn.cursor()
    c.execute(f"DELETE FROM {table_name} WHERE {table_name[:-1]}_id = ?", (row_id,))
    conn.commit()
    conn.close()

# Main GUI Application
def main_window():
    root = Tk()
    root.title('Warehouse Management System')
    root.geometry('600x400')
    root.configure(bg='lightgray')

    welcome_label = Label(root, text="Welcome to the Warehouse Management System", font=("Arial", 16), bg='lightgray')
    welcome_label.pack(pady=20)

    def open_table_management(table_name, columns):
        # Subwindow for table management
        sub_window_table = Toplevel(root)
        sub_window_table.title(f"{table_name} Management")
        sub_window_table.geometry('400x400')

        # Add Row Functionality
        def submit_row():
            add_row_sub = Toplevel(sub_window_table)
            add_row_sub.title("Add Row")
            add_row_sub.geometry('300x300')

            entry_fields = {}
            for col in columns:
                Label(add_row_sub, text=col.replace('_', ' ').capitalize()).pack()
                entry = Entry(add_row_sub)
                entry.pack()
                entry_fields[col] = entry

            def submit_new_row():
                values = [entry_fields[col].get() for col in columns]
                # Convert types as necessary for specific columns (e.g., float, int)
                if 'unit_price' in columns:
                    values[columns.index('unit_price')] = float(values[columns.index('unit_price')])
                if 'quantity_in_stock' in columns:
                    values[columns.index('quantity_in_stock')] = int(values[columns.index('quantity_in_stock')])
                if 'reorder_level' in columns:
                    values[columns.index('reorder_level')] = int(values[columns.index('reorder_level')])
                if 'supplier_id' in columns:
                    values[columns.index('supplier_id')] = int(values[columns.index('supplier_id')])
                add_new_row(table_name, columns, values)
                add_row_sub.destroy()  # Close the subwindow after submission
                messagebox.showinfo('Success', f'New {table_name[:-1]} added successfully!')

            Button(add_row_sub, text="Submit", command=submit_new_row).pack()

        Button(sub_window_table, text="Add Row", command=submit_row).pack(pady=10)

        # Delete Row Functionality
        def submit_delete():
            delete_row_sub = Toplevel(sub_window_table)
            delete_row_sub.title("Delete Row")
            delete_row_sub.geometry('300x200')

            Label(delete_row_sub, text="Enter ID of the row to delete:").pack()
            entry_id = Entry(delete_row_sub)
            entry_id.pack()

            def delete_row_entry():
                row_id = entry_id.get()
                delete_row(table_name, row_id)
                delete_row_sub.destroy()  # Close the subwindow after deletion
                messagebox.showinfo('Success', f'Row deleted successfully!')

            Button(delete_row_sub, text="Delete", command=delete_row_entry).pack()

        Button(sub_window_table, text="Delete", command=submit_delete).pack(pady=10)

        # Update Row Functionality
        def submit_update_row():
            update_row_sub = Toplevel(sub_window_table)
            update_row_sub.title("Update Row")
            update_row_sub.geometry('300x300')

            Label(update_row_sub, text="Enter ID of the row to update:").pack()
            entry_id_update = Entry(update_row_sub)
            entry_id_update.pack()

            entry_fields = {}
            for col in columns:
                Label(update_row_sub, text=f"New {col.replace('_', ' ').capitalize()}:").pack()
                entry = Entry(update_row_sub)
                entry.pack()
                entry_fields[col] = entry

            def update_entry():
                row_id = entry_id_update.get()
                updates = {col: entry_fields[col].get() for col in columns if entry_fields[col].get()}
                update_row(table_name, row_id, updates)
                update_row_sub.destroy()  # Close the subwindow after submission
                messagebox.showinfo('Success', f'Row updated successfully!')

            Button(update_row_sub, text="Update", command=update_entry).pack()

        Button(sub_window_table, text="Update", command=submit_update_row).pack(pady=10)

        # List Rows Functionality
        def open_list_window():
            rows = list_rows(table_name)
            sub_window_list = Toplevel(root)
            sub_window_list.title(f"Contents of {table_name}")

            # Create a treeview for better display of rows
            tree = ttk.Treeview(sub_window_list, columns=columns, show='headings')
            for col in columns:
                tree.heading(col, text=col.replace('_', ' ').capitalize())
            tree.pack(fill=BOTH, expand=True)

            for row in rows:
                tree.insert('', 'end', values=row)

            # Add a scrollbar
            scrollbar = Scrollbar(sub_window_list, orient='vertical', command=tree.yview)
            tree.configure(yscroll=scrollbar.set)
            scrollbar.pack(side='right', fill='y')

        Button(sub_window_table, text=f"List {table_name}", command=open_list_window).pack(pady=10)

    # Define column names for each table
    columns_dict = {
        'Products': ['product_id', 'product_name', 'sku', 'description', 'category', 'unit_price', 'quantity_in_stock', 'reorder_level', 'supplier_id'],
        'Suppliers': ['supplier_id', 'supplier_name', 'contact_name', 'phone', 'email', 'address'],
        'Customers': ['customer_id', 'customer_name', 'contact_name', 'phone', 'email', 'address'],
        'Orders': ['order_id', 'order_date', 'order_status', 'customer_id', 'product_id', 'total_amount', 'shipped_date']
    }

    # Buttons to open CRUD windows for each table
    for table_name in columns_dict.keys():
        Button(root, text=f"Manage {table_name}", command=lambda tn=table_name: open_table_management(tn, columns_dict[tn])).pack(pady=10)

    root.mainloop()

# Launch the main window
main_window()
