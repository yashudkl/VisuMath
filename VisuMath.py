import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Load and store original image
original_img = Image.open("sample.jpg")

# Function to update the image size on window resize
def resize_image(event):
    new_width = event.width - 50
    new_height = int(new_width * original_img.height / original_img.width)
    resized = original_img.resize((new_width, new_height), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(resized)
    img_label.configure(image=photo)
    img_label.image = photo  # Keep reference!

# Function to update main content
def update_content(title, content):
    for widget in content_frame.winfo_children():
        widget.destroy()
    
    label = tk.Label(content_frame, text=title, font=("Helvetica", 18, "bold"), bg="#ffffff", pady=10)
    label.pack()
    
    content_label = tk.Label(content_frame, text=content, font=("Helvetica", 14), bg="#ffffff", wraplength=500, justify="center")
    content_label.pack(pady=10)

# Main window setup
root = tk.Tk()
root.title("Math Topics")
root.geometry("700x600")
root.configure(bg="#f5f5f5")

# Image row
resized_img = original_img.resize((650, 180), Image.Resampling.LANCZOS)
photo = ImageTk.PhotoImage(resized_img)

img_label = tk.Label(root, image=photo, bg="#f5f5f5")
img_label.pack(pady=10)
root.bind("<Configure>", resize_image)

# Buttons
button_frame = tk.Frame(root, bg="#f5f5f5")
button_frame.pack(pady=10)

style = ttk.Style()
style.configure("TButton", font=("Helvetica", 14), padding=10)

ttk.Button(button_frame, text="Multivariable Calculus",
           command=lambda: update_content("Multivariable Calculus", "Here you can study Partial Derivatives, Double Integrals, etc.")).pack(pady=5, fill="x")

ttk.Button(button_frame, text="Vector Functions",
           command=lambda: update_content("Vector Functions", "Explore topics like Vector Fields, Curl, Divergence...")).pack(pady=5, fill="x")

ttk.Button(button_frame, text="Other Stuff",
           command=lambda: update_content("Other Stuff", "This section can include any additional topics.")).pack(pady=5, fill="x")

# Content area
content_frame = tk.Frame(root, bg="#ffffff", width=600, height=250)
content_frame.pack(pady=20, fill="both", expand=True)

# Initial content
update_content("Welcome", "Click on any topic to get started!")

root.mainloop()
