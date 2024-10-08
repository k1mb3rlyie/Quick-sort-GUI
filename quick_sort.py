# To sort all types of values in GUI

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox


ctk.set_appearance_mode("light")  # or "dark"


def quick_sort(values, reverse=False):
    if len(values) <= 1:
        return values
    else:
        pivot = values[0]
        less_than_pivot = [
            x for x in values[1:] if (x <= pivot if not reverse else x >= pivot)
        ]
        greater_than_pivot = [
            x for x in values[1:] if (x > pivot if not reverse else x < pivot)
        ]
        return (
            quick_sort(less_than_pivot, reverse)
            + [pivot]
            + quick_sort(greater_than_pivot, reverse)
        )


# Functionlogic based on user input
def sort_values():
    input_values = entry.get().strip()
    # Split input by commas and remove empty values
    input_list = [item.strip() for item in input_values.split(",") if item.strip()]

    if not input_list:
        messagebox.showerror(
            "Input Error", "Please enter valid comma-separated values."
        )
        return

    try:
        # converting all input values to floats for numerical sorting
        converted_list = [
            float(item) if item.replace(".", "", 1).isdigit() else item
            for item in input_list
        ]
    except ValueError:
        messagebox.showerror(
            "Conversion Error", "Please make sure all values are correctly formatted."
        )
        return

    # Sort numbers first then letters if there are any strings so that works for all types of values
    num_list = [item for item in converted_list if isinstance(item, (int, float))]
    str_list = [item for item in converted_list if isinstance(item, str)]

    # user selection (ascending or descending)
    sorted_num = quick_sort(num_list, reverse=sort_order.get() == "Descending")
    sorted_str = quick_sort(str_list, reverse=sort_order.get() == "Descending")

    # Combine sorted numbers and strings i think nnumbers should come first)
    sorted_list = sorted_num + sorted_str

    # function to clear previous results from the text widget
    result_text.delete(1.0, tk.END)

    for item in sorted_list:
        result_text.insert(tk.END, str(item) + "\n")

    # Dynamicality
    window_height = min(400 + len(sorted_list) * 20, 800)
    root.geometry(f"600x{window_height}")


# refresh
def refresh():
    entry.delete(0, tk.END)
    result_text.delete(1.0, tk.END)
    root.geometry("600x400")


####
####

# Initialize CustomTkinter GUI window
root = ctk.CTk()
root.title("Sorting Algorithm GUI")
root.geometry("800x500")

# casue people do be having eye issues lowkey
custom_font = ("Courier New", 14)

# comma-separated values
entry_label = ctk.CTkLabel(root, text="Enter values (CSV):", font=custom_font)
entry_label.pack(pady=10)
entry = ctk.CTkEntry(root, width=300, font=custom_font)
entry.pack()

# Dropdown menu to for sort order Ascending/Descending
sort_order = ctk.StringVar()
sort_order.set("Ascending")
sort_menu = ctk.CTkComboBox(
    root, values=["Ascending", "Descending"], font=custom_font, variable=sort_order
)
sort_menu.pack(pady=10)

sort_button = ctk.CTkButton(
    root, text="Sort your elements", command=sort_values, corner_radius=20
)
sort_button.pack(pady=10)  # Button

result_text = tk.Text(
    root, height=10, width=50, font=custom_font, fg="#AA336A", bg="pink"
)
result_text.pack(pady=10)

refresh_button = ctk.CTkButton(root, text="Refresh", command=refresh, corner_radius=20)
refresh_button.pack(pady=10)


# Start the Tkinter main loop
root.mainloop()
