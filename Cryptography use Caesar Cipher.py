import tkinter as tk
from tkinter import messagebox

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + -shift) % 26 + base)
        else:
            result += char
    return result

def encrypt_text():
    try:
        shift = int(shift_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Shift harus berupa angka!")
        return
    text = input_text.get("1.0", tk.END).strip()
    if text:
        result = caesar_encrypt(text, shift)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result)
    else:
        messagebox.showwarning("Warning", "Kolom input tidak boleh kosong!")

def decrypt_text():
    try:
        shift = int(shift_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Shift harus berupa angka!")
        return
    text = input_text.get("1.0", tk.END).strip()
    if text:
        result = caesar_decrypt(text, shift)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result)
    else:
        messagebox.showwarning("Warning", "Kolom input tidak boleh kosong!")

def copy_text():
    text = output_text.get("1.0", tk.END).strip()
    if text:
        root.clipboard_clear() 
        root.clipboard_append(text)
        root.update()
        messagebox.showinfo("Info", "Teks berhasil disalin!")
    else:
        messagebox.showwarning("Warning", "Kolom output tidak ada teks untuk disalin!")

def paste_text():
    text = root.clipboard_get() 
    input_text.delete("1.0", tk.END)
    input_text.insert(tk.END, text) 

def clear_text():
    input_text.delete("1.0", tk.END)
    shift_entry.delete("0", tk.END)
    output_text.delete("1.0", tk.END)
    
root = tk.Tk()
root.title("Caesar Cryptography")
root.geometry("450x350")
root.resizable(True, True)
root.configure(background='blue')

frame_input = tk.Frame(root, bg="blue")
frame_input.pack(pady=10)

tk.Label(frame_input, text="Input Text:", bg="blue", fg="white", font=("Arial", 10)).grid(row=0, column=0, sticky="w")
input_text = tk.Text(frame_input, height=3, width=50, bg="dark gray", font=("Arial", 10))
input_text.grid(row=1, column=0, columnspan=2, pady=5)

tk.Label(frame_input, text="Shift:", bg="blue", fg="white", font=("Arial", 10)).grid(row=2, column=0, sticky="e")
shift_entry = tk.Entry(frame_input, width=5, justify="center", bg="dark gray", font=("Arial", 10))
shift_entry.grid(row=2, column=1, sticky="w", padx=5)

paste_button = tk.Button(frame_input, text="Paste", bg="#2196F3", fg="white", font=("Arial", 10), command=paste_text)
paste_button.grid(row=3, column=0, sticky="e", columnspan=2, pady=5)

frame_buttons = tk.Frame(root, bg="blue")
frame_buttons.pack(pady=10)

encrypt_button = tk.Button(frame_buttons, text="Encrypt", bg="#2196F3", fg="white", font=("Arial", 10), command=encrypt_text)
encrypt_button.grid(row=0, column=0, padx=10)

decrypt_button = tk.Button(frame_buttons, text="Decrypt", bg="#2196F3", fg="white", font=("Arial", 10), command=decrypt_text)
decrypt_button.grid(row=0, column=1, padx=10)

frame_output = tk.Frame(root, bg="blue")
frame_output.pack(pady=10)

tk.Label(frame_output, text="Output Text:", bg="blue", fg="white", font=("Arial", 10)).grid(row=0, column=0, sticky="w")
output_text = tk.Text(frame_output, height=3, width=50, bg="dark gray", font=("Arial", 10))
output_text.grid(row=1, column=0, columnspan=2, pady=5)

clear_button = tk.Button(frame_buttons, text="Clear", bg="#2196F3", fg="white", font=("Arial", 10), command=clear_text)
clear_button.grid(row=0, column=2, padx=10)

copy_button = tk.Button(frame_output, text="Copy", bg="#2196F3", fg="white", font=("Arial", 10), command=copy_text)
copy_button.grid(row=2, column=0, sticky="e", columnspan=2, pady=5)

root.mainloop()