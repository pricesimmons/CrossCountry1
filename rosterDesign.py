import tkinter as tk
from tkinter import ttk, Listbox, END, messagebox

def create_roster_page(notebook):
    roster_page = ttk.Frame(notebook)
    notebook.add(roster_page, text="Roster")

    # Variables for main list and male/female categories
    runners_list = ["Runner 1", "Runner 2", "Runner 3"]  # Replace with your actual list of runners
    male_runners = []
    female_runners = []

    # Function to create roster
    def create_roster():
        # Add your logic here to handle creating the roster
        messagebox.showinfo("Create Roster", f"Roster created:\nMale: {male_runners}\nFemale: {female_runners}")

    # Function to update categories when a runner is dragged
    def update_categories(event, category_listbox, category_list):
        selected_index = category_listbox.nearest(event.y)
        if selected_index != -1:
            selected_runner = category_listbox.get(selected_index)
            # Add your logic here to update the categories based on the selected runner
            # For now, let's just move the runner to the corresponding category
            if selected_runner in category_list:
                category_listbox.delete(selected_index)
                category_list.remove(selected_runner)
                main_listbox.insert(END, selected_runner)

    # Function to determine gender (replace this with your actual logic)
    def determine_gender(runner):
        # Add your logic to determine the gender of the runner
        # For now, let's randomly assign gender based on the length of the runner's name
        return "Male" if len(runner) % 2 == 0 else "Female"

    # Main listbox to display all runners
    main_listbox = Listbox(roster_page, selectmode=tk.SINGLE, font=("Helvetica", 14))
    main_listbox.grid(row=0, column=0, rowspan=5, sticky="ns", padx=10)
    main_listbox.insert(END, *runners_list)

    # Bind the update_categories function to the listbox selection event
    main_listbox.bind("<B1-Motion>", lambda event: update_categories(event, main_listbox, runners_list))

    # Male category listbox
    male_listbox = Listbox(roster_page, selectmode=tk.SINGLE, font=("Helvetica", 14))
    male_listbox.grid(row=0, column=1, sticky="ns", padx=10)
    tk.Label(roster_page, text="Male", font=("Helvetica", 14)).grid(row=0, column=1, pady=10)

    # Bind the update_categories function to the listbox selection event
    male_listbox.bind("<B1-Motion>", lambda event: update_categories(event, male_listbox, male_runners))

    # Female category listbox
    female_listbox = Listbox(roster_page, selectmode=tk.SINGLE, font=("Helvetica", 14))
    female_listbox.grid(row=0, column=2, sticky="ns", padx=10)
    tk.Label(roster_page, text="Female", font=("Helvetica", 14)).grid(row=0, column=2, pady=10)

    # Bind the update_categories function to the listbox selection event
    female_listbox.bind("<B1-Motion>", lambda event: update_categories(event, female_listbox, female_runners))

    # Create Roster button
    tk.Button(roster_page, text="Create Roster", command=create_roster, font=("Helvetica", 14)).grid(row=2, column=1, columnspan=2, pady=20)