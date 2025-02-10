import customtkinter as tk


class MyScrollableCheckboxFrame(tk.CTkScrollableFrame):
    def __init__(self, master, title, values):
        super().__init__(master, label_text=title)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.checkboxes = []

        for i, value in enumerate(self.values):
            checkbox = tk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="w")
            self.checkboxes.append(checkbox)
    
    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get():
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes


class MyRadioButtonFrame(tk.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.title = title
        self.values = values
        self.radio_buttons = []
        self.variable = tk.StringVar(value="")

        self.title = tk.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        for i, value in enumerate(values):
            radiobutton = tk.CTkRadioButton(self, text=value, variable=self.variable, value=value)
            radiobutton.grid(row=i+1, column=0, padx=10, pady=(10, 0), sticky="w")
            self.radio_buttons.append(radiobutton)

    def get(self):
        return self.variable.get()
        
    def set(self, value):
        self.variable.set(value)

class MyCheckboxFrame(tk.CTkFrame):

    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.title = title
        self.checkboxes = []

        self.title = tk.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        for i, value in enumerate(values):
            checkbox = tk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i+1, column=0, padx=10, pady=(10, 0), sticky="w")
            self.checkboxes.append(checkbox)
        
    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get():
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes

class App(tk.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("400x220")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        values = ["value 1", "value 2", "value 3", "value 4", "value 5", "value 6"]
        self.scrollable_checkbox_frame = MyScrollableCheckboxFrame(self, title="Values", values=values)
        self.scrollable_checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

        self.button = tk.CTkButton(self, text="my button", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

    def button_callback(self):
        print("checkbox_frame:", self.checkbox_frame.get())
        print("radiobutton_frame:", self.radiobutton_frame.get())

app = App()
app.mainloop()