import tkinter as tk
from tkinter import messagebox
from tkinter import ttk 
import database

database.init_db()

root = tk.Tk()
root.title("Revenue and Exoendutyre System")
root.geometry("800x500")

# 統計功能
lbl_total = tk.Label(root, text="Total Output: $0", font=("Arial", 12, "bold"), fg="red")
lbl_total.pack(pady=10)

def update_ui():
    total = database.get_total_amount()
    if total >= 0:
        display_color = "green"
    else:
        display_color = "red"

    lbl_total.config(text=f"Total Output: ${total:.2f}", fg = display_color)

    for i in tree.get_children():
        tree.delete(i)
    for row in database.get_all_records():
        tree.insert("", tk.END, values=row)

# 輸入區域 
frame_input = tk.Frame(root)
frame_input.pack(pady=10)

tk.Label(frame_input, text="Item:").grid(row=0, column=0)
entry_item = tk.Entry(frame_input, width=10)
entry_item.grid(row=0, column=1, padx=5)

tk.Label(frame_input, text="Money:").grid(row=0, column=2)
entry_amount = tk.Entry(frame_input, width=10)
entry_amount.grid(row=0, column=3, padx=5)

tk.Label(frame_input, text="Type:").grid(row=0, column=4)
combo_type = ttk.Combobox(frame_input, values=["Income", "Output"], width=7, state="readonly")
combo_type.current(0)
combo_type.grid(row=0, column=5, padx=5)

def save_data():
    item = entry_item.get()
    amount = entry_amount.get()
    record_type = combo_type.get()

    if item and amount:
        try:
            database.add_record(item, amount, record_type)
            messagebox.showinfo("Success", f"saved{record_type}: {item}")
            entry_item.delete(0, tk.END)
            entry_amount.delete(0, tk.END)
            update_ui()
        except ValueError:
            messagebox.showerror("Error", "Please enter Number at 'Money' ")
    else:
        messagebox.showwarning("Warning", "Please Enter Correct Information")

def delete_data():
    #獲取表格中被選中的項目
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Warning", "Please select the record you want to delete")
        return

    record_values = tree.item(selected_item)['values']
    record_id = record_values[0]
    item_name = record_values[1]
    
    # 彈出確認視窗，避免誤刪
    if messagebox.askyesno("Comfirm delete", f"Are you sure to delete the {item_name} record?"):
        try:
            database.delete_record(record_id)
            messagebox.showinfo("Success", "Record deleted successfully")
            update_ui()
        except Exception as e:
            messagebox.showerror("Error", f"Delete Failed: {e}")

btn_save = tk.Button(root, text="Save record", command=save_data, bg="lightblue")
btn_save.pack(pady=5)
btn_delete = tk.Button(root, text="Delete record", command=delete_data, bg="#B93232", fg="white")
btn_delete.pack(pady=5)

# 紀錄列表
columns = ("ID", "Item", "Money", "Type", "Date")
tree = ttk.Treeview(root, columns=columns, show="headings", height=10)

# 設定標題
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

tree.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
update_ui()

root.mainloop()