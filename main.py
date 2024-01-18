import tkinter as tk
from tkinter import ttk
from view.raceDesign import create_race_panel
from view.rosterDesign import create_roster_page
from view.runnersDesign import create_runners_page
from view.reportsDesign import create_report_panel

def main():
    root = tk.Tk()
    root.title("Jones County High School Cross Country")

    school_name_label = tk.Label(root, text="Jones County High School Track", font=("Helvetica", 24, "bold"), padx=20,
                                 pady=10)
    school_name_label.pack()

    # Full-screen configuration
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry(f"{width}x{height}+0+0")

    # Configure style for larger tabs
    style = ttk.Style()
    style.configure("TNotebook.Tab", font=("Helvetica", 14))

    # Notebook for page navigation
    notebook = ttk.Notebook(root)

    # Create pages
    create_runners_page(notebook)
    create_roster_page(notebook)
    create_race_panel(notebook)
    create_report_panel(notebook)

    # Pack notebook to fill the entire window
    notebook.pack(expand=True, fill='both')

    root.mainloop()

if __name__ == "__main__":
    main()
