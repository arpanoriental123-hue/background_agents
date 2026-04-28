# Personal Expense Tracker (Python + Tkinter + SQLite)

A clean and beginner-friendly **Personal Expense Tracker** desktop application built using **Python**, with a graphical interface powered by **Tkinter**, a local **SQLite3 database**, and category-wise **bar charts using Matplotlib**.

This app allows users to **record daily expenses**, view them in a **scrollable table**, and **visualize their spending habits** with just one click — all offline, no internet required!

---

## Features

-  **Add Expense**: Input amount, category, date, and description  
-  **View Expenses**: Scrollable table using `ttk.Treeview`  
-  **Visualize Expenses**: Category-wise bar chart (via `matplotlib`)  
-  **Local Storage**: Uses `SQLite` to store all data in a `.db` file  
-  **Tabbed UI**: Clean interface with `ttk.Notebook` tabs  
-  **Safe Input Handling**: Shows alerts for invalid or incomplete inputs  
-  **Lightweight & Offline**: No login, no setup, just run the file!

---

##  Screenshots

- Add Expense Tab
   ![Screenshot 2025-07-10 103542](https://github.com/user-attachments/assets/fc0893f7-bcb0-4540-92fa-4795f0bad56e)

- View Table Tab
  ![Screenshot 2025-07-10 103553](https://github.com/user-attachments/assets/56e06d93-1fd4-4d3d-a546-4236ff8d5b47)
 
- Chart Visualization Tab
  ![Screenshot 2025-07-10 103604](https://github.com/user-attachments/assets/e012aa2a-abfa-433b-bade-3a88b930af18)
 

---

## Technologies Used

| Tool/Library      | Purpose                        |
|-------------------|--------------------------------|
| Python 3          | Core programming language      |
| Tkinter           | GUI elements                   |
| ttk (Themed Tk)   | Stylish widgets like tabs, table |
| SQLite3           | Local database for expense data |
| Matplotlib        | Drawing expense bar charts     |

---

# How to Run

##  Install required library:

pip install matplotlib

tkinter and sqlite3 are pre-installed with Python, no need to install them separately.

## Run the application:

python app.py

The GUI window will open. You can start adding and viewing your expenses.

## Project Structure

expense-tracker/
│
├── app.py             # Main application file
├── expenses.db        # Auto-created SQLite database
├── requirements.txt   # Required Python packages
└── README.md          # This documentation

## Learnings
This project teaches you:

GUI programming using Tkinter

Working with local databases (SQLite)

Displaying data in tables (ttk.Treeview)

Using Matplotlib for charts

Building multi-tabbed desktop apps

## Future Scope
 Add Edit/Delete functionality

 Export data to CSV or Excel

 Add pie chart and date filters

 Add login system for multi-user usage

## Author
Deepanshu 
📧 deepkrajput87611@gmail.com
📍 Baghpat, Uttar Pradesh, India
🔗 LinkedIn Profile

## Usage
This project is free to use for learning, educational, and personal purposes.
No license restrictions — just give credit if you share or modify it.
