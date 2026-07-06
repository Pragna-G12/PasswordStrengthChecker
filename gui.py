import tkinter as tk
from tkinter import ttk
import random
import string
import pyperclip

from checker import check_password


# -----------------------------
# Show / Hide Password
# -----------------------------
def toggle_password():

    if show_password.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")


# -----------------------------
# Check Password
# -----------------------------
def check():

    password = password_entry.get()

    message, strength, color = check_password(password)

    result_label.config(
        text=message,
        fg=color
    )

    strength_label.config(
        text="Strength : " + strength,
        fg=color
    )

    if strength == "Weak":
        progress["value"] = 30

    elif strength == "Medium":
        progress["value"] = 70

    else:
        progress["value"] = 100


# -----------------------------
# Generate Password
# -----------------------------
def generate_password():

    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    length = length_slider.get()

    password = ""

    for i in range(length):
        password += random.choice(characters)

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

    check()


# -----------------------------
# Copy Password
# -----------------------------
def copy_password():

    pyperclip.copy(password_entry.get())

    result_label.config(
        text="✅ Password copied to clipboard!",
        fg="blue"
    )


# -----------------------------
# Clear
# -----------------------------
def clear():

    password_entry.delete(0, tk.END)

    result_label.config(
        text="",
        fg="black"
    )

    strength_label.config(
        text="Strength : ",
        fg="black"
    )

    progress["value"] = 0


# -----------------------------
# Main Window
# -----------------------------
window = tk.Tk()

window.title("Password Strength Checker")

window.geometry("550x650")

window.resizable(False, False)


# -----------------------------
# Heading
# -----------------------------
heading = tk.Label(
    window,
    text="Password Strength Checker",
    font=("Arial", 20, "bold")
)

heading.pack(pady=15)


# -----------------------------
# Password Label
# -----------------------------
password_label = tk.Label(
    window,
    text="Enter Password",
    font=("Arial", 12)
)

password_label.pack()


# -----------------------------
# Password Entry
# -----------------------------
password_entry = tk.Entry(
    window,
    width=35,
    font=("Arial", 13),
    show="*"
)

password_entry.pack(pady=10)


# Live Checking
password_entry.bind("<KeyRelease>", lambda event: check())


# -----------------------------
# Show Password
# -----------------------------
show_password = tk.BooleanVar()

show_checkbox = tk.Checkbutton(
    window,
    text="Show Password",
    variable=show_password,
    command=toggle_password
)

show_checkbox.pack()


# -----------------------------
# Password Length Slider
# -----------------------------
length_slider = tk.Scale(
    window,
    from_=8,
    to=32,
    orient="horizontal",
    label="Password Length"
)

length_slider.set(12)

length_slider.pack(pady=10)


# -----------------------------
# Check Button
# -----------------------------
check_button = tk.Button(
    window,
    text="Check Password",
    width=20,
    font=("Arial", 12),
    command=check
)

check_button.pack(pady=5)


# -----------------------------
# Generate Button
# -----------------------------
generate_button = tk.Button(
    window,
    text="Generate Password",
    width=20,
    font=("Arial", 12),
    command=generate_password
)

generate_button.pack(pady=5)


# -----------------------------
# Copy Button
# -----------------------------
copy_button = tk.Button(
    window,
    text="Copy Password",
    width=20,
    font=("Arial", 12),
    command=copy_password
)

copy_button.pack(pady=5)


# -----------------------------
# Clear Button
# -----------------------------
clear_button = tk.Button(
    window,
    text="Clear",
    width=20,
    font=("Arial", 12),
    command=clear
)

clear_button.pack(pady=5)


# -----------------------------
# Result
# -----------------------------
result_label = tk.Label(
    window,
    text="",
    justify="left",
    wraplength=500,
    font=("Arial", 11)
)

result_label.pack(pady=20)


# -----------------------------
# Strength
# -----------------------------
strength_label = tk.Label(
    window,
    text="Strength : ",
    font=("Arial", 14, "bold")
)

strength_label.pack()


# -----------------------------
# Progress Bar
# -----------------------------
progress = ttk.Progressbar(
    window,
    orient="horizontal",
    length=350,
    mode="determinate"
)

progress.pack(pady=15)


# -----------------------------
# Run Application
# -----------------------------
window.mainloop()
