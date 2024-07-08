from tkinter import *

# Function to convert miles to kilometers
def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.60934
    kilometer_result_label.config(text=f"{km:.2f}")

# Set up the main window
window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

# Create and place widgets in the window using grid layout

# Miles input
miles_input = Entry(window, width=10)
miles_input.grid(column=1, row=0)

# Miles label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# Equal label
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

# Kilometer result label (initially set to 0)
kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

# Kilometer label
kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

# Calculate button
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

# Start the main event loop
window.mainloop()
