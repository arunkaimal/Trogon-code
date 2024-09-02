import tkinter as tk
from tkinter import messagebox

# Function to add item to the list
def add_item():
    item = entry.get()
    if item:
        listbox.insert(tk.END, item)
        entry.delete(0, tk.END)
        feedback_label.config(text="Item added!")
    else:
        messagebox.showerror("Error", "Entry field is empty. Please enter an item.")

# Function to remove selected items
def remove_item():
    selected_items = listbox.curselection()
    if selected_items:
        for index in selected_items[::-1]:  # Remove items
            listbox.delete(index)
        feedback_label.config(text="Selected item(s) removed!")
    else:
        messagebox.showwarning(
            "Warning", "No item selected. Please select an item to remove."
        )

# Function to edit selected item
def edit_item():
    selected_items = listbox.curselection()
    if selected_items:
        index = selected_items[0]
        item = listbox.get(index)
        entry.delete(0, tk.END)
        entry.insert(0, item)
        listbox.delete(index)
        feedback_label.config(text="Editing item: " + item)
    else:
        messagebox.showwarning(
            "Warning", "No item selected. Please select an item to edit."
        )

# Function to clear the entire list
def clear_list():
    if listbox.size() > 0:
        listbox.delete(0, tk.END)
        feedback_label.config(text="List cleared!")
    else:
        messagebox.showwarning("Warning", "List is already empty.")

# Main window
root = tk.Tk()
root.title("Shopping List")

# Entry item input
entry = tk.Entry(root, width=35)
entry.grid(row=0, column=0, padx=10, pady=10)

# Add item button
add_button = tk.Button(root, text="Add Item", command=add_item, width=15, bg="green")
add_button.grid(row=0, column=1, padx=10)

# Listbox to display shopping list
listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50, height=15)
listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Edit button
edit_button = tk.Button(root, text="Edit Selected", command=edit_item, width=15, bg="yellow")
edit_button.grid(row=2, column=0, padx=10, pady=5)

# Remove button
remove_button = tk.Button(root, text="Remove Selected", command=remove_item, width=15, bg="red")
remove_button.grid(row=2, column=1, padx=10, pady=5)

# Clear button
clear_button = tk.Button(root, text="Clear List", command=clear_list, width=15, bg="white")
clear_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# Display messages like "item added", "item removed", etc.
feedback_label = tk.Label(root, text="", fg="green")
feedback_label.grid(row=4, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
