# Personal-Finance-Managemnet-System

A professional Python-based desktop application for tracking daily income and expenses. This project demonstrates core software engineering principles including data persistence, dynamic UI feedback, and modular architecture.

Key Features:
Dynamic Data Portability: Uses Python's "os" module to automatically detect the project directory, ensuring the SQLite database ("finance.db") works on any PC without manual path configuration.

Full CRUD Operations: 
Create: Add records with item names and amounts.
Read: Real-time history list view using "ttk.Treeview".
Delete: Remove specific entries with a secure confirmation prompt.

Smart Financial Logic:
Income/Expense Toggle: Automatically handles positive/negative values based on entry type.
Auto-Calculating Balance: Real-time summation of all records.

Advanced UI Feedback:
Color Coding: Balance text turns "Green" for savings and "Red"for debt.

Technical Stack
Language: Python 3.10+
GUI: Tkinter & ttk (for modern table rendering)
Database: SQLite3 (Relational database with localized storage)
Design Pattern: Logic-Data Separation (Modular design between "main.py" and "database.py")
