import customtkinter as tk

tk.set_appearance_mode('System') # Modes: 'System (default)', 'Dark', 'Light'
tk.set_default_color_theme('blue') # Themes: 'blue (default)', 'dark-blue'

app = tk.CTk() # create CTk window like you do with Tk window
app.geometry('400x400') # set geometry

def button_function():
    print('Button clicked')

# Use the CTk instead of tkinter Button
button = tk.CTkButton(master=app, text='CTkButton', command=button_function)
button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


# Run the app
app.mainloop()