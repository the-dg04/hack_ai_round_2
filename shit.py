import tkinter as tk
from tkinter import filedialog

def generate_output():
    file1 = file1_entry.get()
    file2 = file2_entry.get()
    # Perform the necessary operations with the selected files here
    # For example, you can print their paths for demonstration
    print("File 1:", file1)
    print("File 2:", file2)
    # Add your logic here to generate output using the selected files

def select_file1():
    file1 = filedialog.askopenfilename()
    file1_entry.delete(0, tk.END)
    file1_entry.insert(tk.END, file1)

def select_file2():
    file2 = filedialog.askopenfilename()
    file2_entry.delete(0, tk.END)
    file2_entry.insert(tk.END, file2)

# Create the main window
root = tk.Tk()
root.title("File Selector")

# File 1
file1_label = tk.Label(root, text="Select File 1:")
file1_label.pack()

file1_entry = tk.Entry(root, width=50)
file1_entry.pack()

file1_button = tk.Button(root, text="Browse", command=select_file1)
file1_button.pack()

# File 2
file2_label = tk.Label(root, text="Select File 2:")
file2_label.pack()

file2_entry = tk.Entry(root, width=50)
file2_entry.pack()

file2_button = tk.Button(root, text="Browse", command=select_file2)
file2_button.pack()

# Generate Button
generate_button = tk.Button(root, text="Generate", command=generate_output)
generate_button.pack()

root.mainloop()
