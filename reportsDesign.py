import tkinter as tk
from tkinter import messagebox

def create_report_panel(notebook):
    report_page = tk.Frame(notebook)
    notebook.add(report_page, text="Reports")

    # Variables for races and runner times
    races_list = ["Race 1", "Race 2", "Race 3"]  # Replace with your actual list of races
    runner_times = {
        "Race 1": {"Runner 1": "12:30", "Runner 2": "13:15", "Runner 3": "11:45"},
        "Race 2": {"Runner 1": "11:45", "Runner 2": "14:00", "Runner 3": "12:30"},
        "Race 3": {"Runner 1": "13:00", "Runner 2": "12:45", "Runner 3": "11:15"}
    }

    # Dropdown menu for selecting the report type
    report_options = ["Select Year"] + list(runner_times["Race 1"].keys())
    selected_year_var = tk.StringVar()
    selected_year_var.set(report_options[0])  # Set the default option

    report_dropdown = tk.OptionMenu(report_page, selected_year_var, *report_options)
    report_dropdown.grid(row=0, column=0, pady=10)

    # Button to download Milesplit
    def download_milesplit():
        selected_year = selected_year_var.get()
        if selected_year != "Select Year":
            messagebox.showinfo("Download Milesplit", f"Downloading Milesplit for {selected_year}...")  # Replace with actual download functionality
        else:
            messagebox.showwarning("Download Milesplit", "Please select a valid year.")

    download_button = tk.Button(report_page, text="Download Milesplit", command=download_milesplit, font=("Helvetica", 14))
    download_button.grid(row=0, column=1, padx=10, pady=10)

    return report_page
