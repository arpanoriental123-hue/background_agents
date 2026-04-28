import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Database setup
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL,
    category TEXT,
    date TEXT,
    description TEXT
)
""")
conn.commit()

# Add expense function
def add_expense():
    amount = amount_entry.get()
    category = category_combobox.get()
    date = date_entry.get()
    description = desc_entry.get()

    if not amount or not category or not date:
        messagebox.showwarning("Input Error", "Please fill all required fields.")
        return

    try:
        cursor.execute("INSERT INTO expenses (amount, category, date, description) VALUES (?, ?, ?, ?)",
                       (float(amount), category, date, description))
        conn.commit()
        messagebox.showinfo("Success", "Expense added successfully!")
        amount_entry.delete(0, tk.END)
        date_entry.delete(0, tk.END)
        desc_entry.delete(0, tk.END)
        load_expenses()
    except ValueError:
        messagebox.showerror("Error", "Amount must be a number.")

# Load expenses to treeview
def load_expenses():
    for row in tree.get_children():
        tree.delete(row)
    cursor.execute("SELECT id, amount, category, date, description FROM expenses")
    for row in cursor.fetchall():
        tree.insert("", tk.END, values=row)

# Show chart
def show_chart():
    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    data = cursor.fetchall()
    categories = [row[0] for row in data]
    amounts = [row[1] for row in data]

    fig, ax = plt.subplots(figsize=(6,4))
    ax.bar(categories, amounts, color='skyblue')
    ax.set_title("Expenses by Category")
    ax.set_ylabel("Total Amount (₹)")
    ax.set_xlabel("Category")

    for widget in chart_tab.winfo_children():
        widget.destroy()

    canvas = FigureCanvasTkAgg(fig, master=chart_tab)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Main window
root = tk.Tk()
root.title("Personal Expense Tracker")
root.geometry("850x600")

# Notebook tabs
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# ----- Tab 1: Add Expense -----
add_tab = ttk.Frame(notebook, padding=20)
notebook.add(add_tab, text="➕ Add Expense")

ttk.Label(add_tab, text="Amount (₹):", font=("Segoe UI", 11)).grid(row=0, column=0, sticky="e", pady=5)
amount_entry = ttk.Entry(add_tab, font=("Segoe UI", 11))
amount_entry.grid(row=0, column=1, pady=5, padx=10)

ttk.Label(add_tab, text="Category:", font=("Segoe UI", 11)).grid(row=1, column=0, sticky="e", pady=5)
category_combobox = ttk.Combobox(add_tab, values=["Food", "Travel", "Bills", "Shopping", "Other"], font=("Segoe UI", 11), state="readonly")
category_combobox.grid(row=1, column=1, pady=5, padx=10)
category_combobox.set("Food")

ttk.Label(add_tab, text="Date (YYYY-MM-DD):", font=("Segoe UI", 11)).grid(row=2, column=0, sticky="e", pady=5)
date_entry = ttk.Entry(add_tab, font=("Segoe UI", 11))
date_entry.grid(row=2, column=1, pady=5, padx=10)

ttk.Label(add_tab, text="Description:", font=("Segoe UI", 11)).grid(row=3, column=0, sticky="e", pady=5)
desc_entry = ttk.Entry(add_tab, font=("Segoe UI", 11), width=40)
desc_entry.grid(row=3, column=1, pady=5, padx=10)

ttk.Button(add_tab, text="Add Expense", command=add_expense).grid(row=4, column=1, pady=20)

# ----- Tab 2: View Expenses -----
view_tab = ttk.Frame(notebook, padding=10)
notebook.add(view_tab, text="📋 View Expenses")

tree = ttk.Treeview(view_tab, columns=("ID", "Amount", "Category", "Date", "Description"), show="headings", height=15)
tree.heading("ID", text="ID")
tree.heading("Amount", text="Amount (₹)")
tree.heading("Category", text="Category")
tree.heading("Date", text="Date")
tree.heading("Description", text="Description")
tree.column("ID", width=40)
tree.column("Amount", width=100)
tree.column("Category", width=100)
tree.column("Date", width=100)
tree.column("Description", width=250)
tree.pack(fill="both", expand=True)

ttk.Button(view_tab, text="🔄 Refresh", command=load_expenses).pack(pady=10)

# ----- Tab 3: Chart -----
chart_tab = ttk.Frame(notebook, padding=10)
notebook.add(chart_tab, text="📊 Charts")
ttk.Button(chart_tab, text="📈 Show Chart", command=show_chart).pack(pady=20)

load_expenses()
root.mainloop()
