import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from Cookr_Q1_Algo import scrape_food_info

def get_tags():
    food_item = entry_food_name.get()
    food_name, _, tags = scrape_food_info(food_item)
    if tags:
        tag_str = ", ".join(tags)
        text_tags.config(state=tk.NORMAL)
        text_tags.delete(1.0, tk.END)
        text_tags.insert(tk.END, f"Tags: {tag_str}")
        text_tags.config(state=tk.DISABLED)
    else:
        text_tags.config(state=tk.NORMAL)
        text_tags.delete(1.0, tk.END)
        text_tags.insert(tk.END, "Food item not available")
        text_tags.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("Food Tag Finder")

# Define dark theme colors
bg_color = "#2b2b2b"  # Dark background color
fg_color = "#ffffff"  # Light text color
entry_bg_color = "#1f1f1f"  # Dark background color for entry field
entry_fg_color = "#ffffff"  # Light text color for entry field

# Apply dark theme colors
root.configure(bg=bg_color)
root.option_add("*Background", bg_color)
root.option_add("*Foreground", fg_color)
root.option_add("*Font", "Helvetica 12")

# Set window size and position
window_width = 400
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create and pack widgets with dark theme colors and increased padding
label_prompt = tk.Label(root, text="Enter food name:", bg=bg_color, fg=fg_color, padx=10, pady=5)
label_prompt.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

entry_food_name = tk.Entry(root, bg=entry_bg_color, fg=entry_fg_color, font=("Helvetica", 12), bd=2, relief=tk.FLAT)
entry_food_name.place(relx=0.5, rely=0.4, anchor=tk.CENTER, width=200, height=30)

button_get_tags = tk.Button(root, text="Get Tags", command=get_tags, bg=bg_color, fg=fg_color, padx=20, pady=10, bd=0, relief=tk.FLAT, font=("Helvetica", 12))
button_get_tags.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

text_tags = tk.Text(root, bg=entry_bg_color, fg=entry_fg_color, font=("Helvetica", 12), bd=2, relief=tk.FLAT, wrap=tk.WORD)
text_tags.place(relx=0.5, rely=0.7, anchor=tk.CENTER, width=350, height=100)

# Add a scrollbar
scrollbar = ttk.Scrollbar(root, orient="vertical", command=text_tags.yview)
scrollbar.place(relx=0.95, rely=0.7, anchor=tk.CENTER, height=100)

# Configure the Text widget to use the scrollbar
text_tags.config(yscrollcommand=scrollbar.set)

# Run the main loop
root.mainloop()
