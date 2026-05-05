from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox

# ---------- Image Processing ----------
def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path).convert("RGB")
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (
                (r ^ key) % 256,
                (g ^ key) % 256,
                (b ^ key) % 256
            )

    img.save(output_path)


def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path).convert("RGB")
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (
                (r ^ key) % 256,
                (g ^ key) % 256,
                (b ^ key) % 256
            )

    img.save(output_path)


# ---------- GUI Actions ----------
def select_image():
    global file_path
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.jpg *.png *.jpeg")]
    )

    if file_path:
        filename = file_path.split("/")[-1]
        path_label.config(text=f"Selected: {filename}", fg="#00E676")


def validate_key():
    try:
        key = int(key_entry.get())
        if 0 <= key <= 255:
            return key
        else:
            messagebox.showerror("Invalid Key", "Key must be between 0 and 255")
            return None
    except ValueError:
        messagebox.showerror("Invalid Input", "Enter a valid integer")
        return None


def encrypt_action():
    if not file_path:
        messagebox.showerror("Error", "Please select an image first")
        return

    key = validate_key()
    if key is None:
        return

    try:
        encrypt_image(file_path, "cipher_output.png", key)
        status_label.config(
            text="Encryption Done (saved as cipher_output.png)",
            fg="#00E676"
        )
    except Exception as e:
        messagebox.showerror("Error", str(e))


def decrypt_action():
    if not file_path:
        messagebox.showerror("Error", "Please select an image first")
        return

    key = validate_key()
    if key is None:
        return

    try:
        decrypt_image(file_path, "original_output.png", key)
        status_label.config(
            text="Decryption Done (saved as original_output.png)",
            fg="#00E676"
        )
    except Exception as e:
        messagebox.showerror("Error", str(e))


# ---------- GUI Layout ----------
root = tk.Tk()
root.title("Image Cipher Tool")
root.geometry("430x330")
root.configure(bg="#121212")
root.resizable(False, False)

file_path = ""

# Title
title = tk.Label(
    root,
    text="Image Cipher Tool",
    font=("Segoe UI", 16, "bold"),
    bg="#121212",
    fg="white"
)
title.pack(pady=15)

# Select Button
select_btn = tk.Button(
    root,
    text="Choose Image",
    command=select_image,
    bg="#4CAF50",
    fg="white",
    width=15
)
select_btn.pack(pady=5)

# Path Label
path_label = tk.Label(
    root,
    text="No image selected",
    bg="#121212",
    fg="#AAAAAA"
)
path_label.pack(pady=5)

# Key Label
key_label = tk.Label(
    root,
    text="Enter Key (0–255)",
    bg="#121212",
    fg="white"
)
key_label.pack(pady=5)

# Key Entry
key_entry = tk.Entry(root, justify="center")
key_entry.pack(pady=5)

# Buttons Frame
btn_frame = tk.Frame(root, bg="#121212")
btn_frame.pack(pady=10)

encrypt_btn = tk.Button(
    btn_frame,
    text="Encrypt",
    command=encrypt_action,
    bg="#1976D2",
    fg="white",
    width=12
)
encrypt_btn.grid(row=0, column=0, padx=10)

decrypt_btn = tk.Button(
    btn_frame,
    text="Decrypt",
    command=decrypt_action,
    bg="#D32F2F",
    fg="white",
    width=12
)
decrypt_btn.grid(row=0, column=1, padx=10)

# Status Label
status_label = tk.Label(
    root,
    text="",
    bg="#121212",
    fg="#00E676"
)
status_label.pack(pady=15)

# Run GUI
root.mainloop()
