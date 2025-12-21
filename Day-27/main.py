from tkinter import *

# -------------------- Window Setup -------------------- #
window = Tk()
window.title("Distance Converter")
window.minsize(width=240, height=170)
window.config(padx=30, pady=30)

# -------------------- State -------------------- #
is_km_to_miles = True  # Conversion direction

# -------------------- Functions -------------------- #
def toggle_direction():
    global is_km_to_miles
    is_km_to_miles = not is_km_to_miles

    if is_km_to_miles:
        direction_button.config(text="Km → Miles")
        input_label.config(text="Km")
        output_label_name.config(text="Miles")
    else:
        direction_button.config(text="Miles → Km")
        input_label.config(text="Miles")
        output_label_name.config(text="Km")

    reset_fields()

def convert_distance():
    value = input_entry.get()
    if not value:
        return

    value = float(value)

    if is_km_to_miles:
        result = value * 0.62137
    else:
        result = value / 0.62137

    output_value_label.config(text=f"{round(result, 4)}")

def reset_fields():
    input_entry.delete(0, END)
    output_value_label.config(text="0")

# -------------------- Direction Button (Top) -------------------- #
direction_button = Button(
    text="Km → Miles",
    width=20,
    bg="#2196F3",
    fg="white",
    activebackground="#1976D2",
    relief="raised",
    command=toggle_direction
)
direction_button.grid(column=0, row=0, columnspan=3, pady=(0, 15))

# -------------------- Labels -------------------- #
input_label = Label(text="Km", font=("Arial", 10, "bold"))
input_label.grid(column=0, row=1, padx=5, pady=5)

output_label_name = Label(text="Miles", font=("Arial", 10, "bold"))
output_label_name.grid(column=0, row=3, padx=5, pady=5)

output_value_label = Label(text="0", font=("Arial", 10, "bold"))
output_value_label.grid(column=1, row=3, padx=5, pady=5)

# -------------------- Input -------------------- #
input_entry = Entry(width=12)
input_entry.grid(column=1, row=1, padx=5, pady=5)

# -------------------- Buttons -------------------- #
convert_button = Button(
    text="Convert",
    width=10,
    bg="#4CAF50",
    fg="white",
    activebackground="#45a049",
    command=convert_distance
)
convert_button.grid(column=1, row=2, pady=10)

reset_button = Button(
    text="Reset",
    width=10,
    bg="#f44336",
    fg="white",
    activebackground="#d32f2f",
    command=reset_fields
)
reset_button.grid(column=0, row=2, pady=10)

window.mainloop()
