from deep_translator import GoogleTranslator
import tkinter as tk
from tkinter import ttk, messagebox

# Function to translate text
def translate_text():
    text = input_text.get("1.0", tk.END).strip()
    source = source_lang.get()
    target = target_lang.get()

    if not text:
        messagebox.showwarning("Warning", "Please enter some text!")
        return

    try:
        translated = GoogleTranslator(source=source, target=target).translate(text)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create window
root = tk.Tk()
root.title("Language Translation Tool")
root.geometry("600x500")

# Language list
languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Tamil": "ta",
    "Telugu": "te",
    "Kannada": "kn",
    "Malayalam": "ml"
}

# Source Language
tk.Label(root, text="Source Language").pack()
source_lang = ttk.Combobox(root, values=list(languages.keys()))
source_lang.set("English")
source_lang.pack()

# Target Language
tk.Label(root, text="Target Language").pack()
target_lang = ttk.Combobox(root, values=list(languages.keys()))
target_lang.set("Hindi")
target_lang.pack()

# Input Text
tk.Label(root, text="Enter Text").pack()
input_text = tk.Text(root, height=6, width=60)
input_text.pack()

# Translate Button
def translate():
    source = languages[source_lang.get()]
    target = languages[target_lang.get()]
    text = input_text.get("1.0", tk.END).strip()

    if text:
        translated = GoogleTranslator(source=source, target=target).translate(text)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated)

tk.Button(root, text="Translate", command=translate).pack(pady=10)

# Output Text
tk.Label(root, text="Translated Text").pack()
output_text = tk.Text(root, height=6, width=60)
output_text.pack()

root.mainloop()