import tkinter as tk
from tkinter import Listbox, END, messagebox

def create_race_panel(notebook):
    race_page = tk.Frame(notebook)
    notebook.add(race_page, text="Race")

    # Variables for races and runner times
    races_list = ["Race 1", "Race 2", "Race 3"]  # Replace with your actual list of races
    selected_race_details = {}

    # Function to display selected race details
    def display_race_details(selected_race):
        if selected_race in selected_race_details:
            race_details = selected_race_details[selected_race]
            header = f"{'Runner Name': <20}{'Time': <15}\n{'-'*35}\n"
            details = "\n".join([f"{runner: <20}{time: <15}" for runner, time in race_details.items()])
            race_text.config(state=tk.NORMAL)
            race_text.delete("1.0", tk.END)
            race_text.insert(tk.END, f"Selected Race: {selected_race}\n\n{header}{details}")
            race_text.config(state=tk.DISABLED)

    # Function to add a runner to the selected race
    def add_runner_to_race():
        selected_index = races_listbox.curselection()
        if selected_index:
            selected_race = races_listbox.get(selected_index)
            new_runner = new_runner_entry.get()
            new_runner_time = new_runner_time_entry.get()
            if new_runner and new_runner_time:
                # Add the new runner to the selected race with the specified time
                if selected_race in selected_race_details:
                    selected_race_details[selected_race][new_runner] = new_runner_time
                else:
                    selected_race_details[selected_race] = {new_runner: new_runner_time}
                display_race_details(selected_race)
                new_runner_entry.delete(0, tk.END)  # Clear the entry after adding a new runner
                new_runner_time_entry.delete(0, tk.END)  # Clear the entry after adding a new runner
            else:
                messagebox.showwarning("Add Runner", "Please enter both runner's name and time.")

    # Left listbox to display races
    races_listbox = tk.Listbox(race_page, selectmode=tk.SINGLE, font=("Helvetica", 14))
    races_listbox.grid(row=0, column=0, rowspan=5, sticky="ns", padx=10)
    races_listbox.insert(tk.END, *races_list)

    # Bind the display_race_details function to the listbox selection event
    races_listbox.bind("<ButtonRelease-1>", lambda event: display_race_details(races_listbox.get(races_listbox.curselection())))

    # Entry boxes to add a new runner and time
    tk.Label(race_page, text="Runner Name", font=("Helvetica", 14)).grid(row=0, column=1, pady=10)
    new_runner_entry = tk.Entry(race_page, font=("Helvetica", 14))
    new_runner_entry.grid(row=0, column=2, pady=10)

    tk.Label(race_page, text="Runner Time (00:00:00)", font=("Helvetica", 14)).grid(row=0, column=3, pady=10)
    new_runner_time_entry = tk.Entry(race_page, font=("Helvetica", 14))
    new_runner_time_entry.grid(row=0, column=4, pady=10)

    # Button to add runner to selected race
    tk.Button(race_page, text="Add Runner to Selected Race", command=add_runner_to_race, font=("Helvetica", 14)).grid(row=1, column=2, columnspan=3, pady=10)

    # Display area for selected race details
    race_label = tk.Label(race_page, text="Selected Race Details", font=("Helvetica", 16, "bold"))
    race_label.grid(row=2, column=2, columnspan=3, pady=10)

    # Create a text widget to display the selected race details
    race_text = tk.Text(race_page, wrap="word", width=60, height=15, font=("Helvetica", 14))
    race_text.grid(row=3, column=2, columnspan=3, pady=10)

    # Function to clear the selected race details
    def clear_race_text():
        race_text.config(state=tk.NORMAL)
        race_text.delete("1.0", tk.END)
        race_text.config(state=tk.DISABLED)

    # Bind the clear_race_text function to the listbox selection event
    races_listbox.bind("<ButtonRelease-1>", lambda event: clear_race_text())

    return race_page
