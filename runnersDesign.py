import tkinter as tk
from tkinter import ttk, Listbox, END, messagebox

def create_runners_page(notebook):
    runners_page = ttk.Frame(notebook)
    notebook.add(runners_page, text="Runners")

    # Variables for input fields
    first_name_var = tk.StringVar()
    last_name_var = tk.StringVar()
    graduation_year_var = tk.StringVar()
    grade_var = tk.StringVar()
    milesplit_url_var = tk.StringVar()

    # Function to add a runner
    def add_runner():
        first_name = first_name_var.get()
        last_name = last_name_var.get()
        graduation_year = graduation_year_var.get()
        grade = grade_var.get()
        milesplit_url = milesplit_url_var.get()

        # Add your logic here to handle adding a runner (e.g., store in a data structure)
        messagebox.showinfo("Add Runner", f"Runner added:\nFirst Name: {first_name}\nLast Name: {last_name}\nGraduation Year: {graduation_year}\nGrade: {grade}\nMilesplit URL: {milesplit_url}")

    # Function to update a runner
    def update_runner():
        # Add your logic here to handle updating a runner
        messagebox.showinfo("Update Runner", "Runner updated")

    # Function to delete a runner
    def delete_runner():
        # Add your logic here to handle deleting a runner
        messagebox.showinfo("Delete Runner", "Runner deleted")

    # Function to populate input fields when a runner is selected
    def on_runner_select(event):
        selected_index = runners_listbox.curselection()
        if selected_index:
            selected_runner = runners_listbox.get(selected_index)
            # Add your logic here to retrieve and display information for the selected runner
            # For now, let's just display the selected runner's name in the messagebox
            messagebox.showinfo("Selected Runner", f"Selected Runner: {selected_runner}")

    # Labels and entry widgets for runner details
    tk.Label(runners_page, text="First Name:", font=("Helvetica", 14)).grid(row=0, column=1, sticky="w", pady=10)
    tk.Entry(runners_page, textvariable=first_name_var, font=("Helvetica", 14)).grid(row=0, column=2, pady=10)

    tk.Label(runners_page, text="Last Name:", font=("Helvetica", 14)).grid(row=1, column=1, sticky="w", pady=10)
    tk.Entry(runners_page, textvariable=last_name_var, font=("Helvetica", 14)).grid(row=1, column=2, pady=10)

    tk.Label(runners_page, text="Graduation Year:", font=("Helvetica", 14)).grid(row=2, column=1, sticky="w", pady=10)
    tk.Entry(runners_page, textvariable=graduation_year_var, font=("Helvetica", 14)).grid(row=2, column=2, pady=10)

    tk.Label(runners_page, text="Grade (9th-12th):", font=("Helvetica", 14)).grid(row=3, column=1, sticky="w", pady=10)
    tk.Entry(runners_page, textvariable=grade_var, font=("Helvetica", 14)).grid(row=3, column=2, pady=10)

    tk.Label(runners_page, text="Milesplit URL:", font=("Helvetica", 14)).grid(row=4, column=1, sticky="w", pady=10)
    tk.Entry(runners_page, textvariable=milesplit_url_var, font=("Helvetica", 14)).grid(row=4, column=2, pady=10)

    # Listbox to display runner names
    runners_listbox = tk.Listbox(runners_page, selectmode=tk.SINGLE, font=("Helvetica", 14))
    runners_listbox.grid(row=0, column=0, rowspan=5, sticky="ns", padx=10)
    runners_listbox.insert(tk.END, "Runner 1", "Runner 2", "Runner 3")  # You can populate the list with actual runner names

    # Bind the on_runner_select function to the listbox selection event
    runners_listbox.bind("<<ListboxSelect>>", on_runner_select)

    # Buttons for add, update, delete
    tk.Button(runners_page, text="Add", command=add_runner, font=("Helvetica", 14)).grid(row=5, column=1, pady=20)
    tk.Button(runners_page, text="Update", command=update_runner, font=("Helvetica", 14)).grid(row=5, column=2, pady=20)
    tk.Button(runners_page, text="Delete", command=delete_runner, font=("Helvetica", 14)).grid(row=5, column=3, pady=20)
