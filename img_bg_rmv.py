import tkinter as tk
from tkinter import filedialog
from rembg import remove
from PIL import Image
import io
import os

def remove_background(input_image_path, output_image_path):
    try:
        with open(input_image_path, 'rb') as input_file:
            input_image = input_file.read()

        output_image = remove(input_image)

        img = Image.open(io.BytesIO(output_image)).convert("RGBA")
        img.save(output_image_path)

        print(f"Background removed and saved to {output_image_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def get_user_input():
    root = tk.Tk()
    root.title("Background Remover")
    root.geometry("700x300")
    root.resizable(True, True)

    # Dark mode theme
    root.configure(bg='#0b0b0b')
    tk.Label(root, text="Background Remover", font=("Arial bold", 20), bg='#0b0b0b', fg='white').pack(pady=10)

    input_image_path = ""
    output_image_path = ""

    def select_input_image():
        nonlocal input_image_path
        input_image_path = filedialog.askopenfilename(
            title="Select Input Image",
            filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")]
        )
        input_label.config(text=f"Input Image: {input_image_path}" if input_image_path else "")

    def select_output_path():
        nonlocal output_image_path
        output_image_path = filedialog.asksaveasfilename(
            title="Save Output Image",
            defaultextension=".png",
            filetypes=[("PNG Image", "*.png")]
        )
        output_label.config(text=f"Output Path: {output_image_path}" if output_image_path else "")

    def remove_background_button():
        if input_image_path and output_image_path:
            remove_background(input_image_path, output_image_path)
        else:
            print("Please select both input image and output path.")

    input_label = tk.Label(root, text="Input Image:", bg='#0b0b0b', fg='white',font=("Arial bold", 12))
    input_label.pack(pady=5)
    input_button = tk.Button(root, text="Select", command=select_input_image, width=20, bg='#0b0b0b', fg='white',font=("Arial bold", 12))
    input_button.pack(pady=10)

    output_label = tk.Label(root, text="Output Path:", bg='#0b0b0b', fg='white',font=("Arial bold", 12))
    output_label.pack(pady=5)
    output_button = tk.Button(root, text="Select", command=select_output_path, width=20, bg='#0b0b0b', fg='white',font=("Arial bold", 12))
    output_button.pack(pady=10)

    remove_button = tk.Button(root, text="Remove Background", command=remove_background_button, width=30, bg='#007bff', fg='#ffffff',font=("Arial bold", 12))
    remove_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    print("Welcome to the Background Remover!")
    print("This script will help you remove the background from an image and save it to your desired location.")
    print("Please use the GUI window to select the input image and output path.")

    get_user_input()