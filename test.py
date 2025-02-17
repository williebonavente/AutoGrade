import customtkinter as ctk
import pandas as pd
import random
from tkinter import filedialog, messagebox, simpledialog

# Grading Scale
def calculate_grade(score):
    if score >= 96: return 1.00
    elif score >= 93: return 1.25
    elif score >= 90: return 1.50
    elif score >= 87: return 1.75
    elif score >= 84: return 2.00
    elif score >= 81: return 2.25
    elif score >= 78: return 2.50
    elif score >= 75: return 2.75
    elif score >= 70: return 3.00  # Passing Grade
    elif score >= 65: return 3.25
    elif score >= 60: return 3.50
    elif score >= 55: return 3.75
    elif score >= 50: return 4.00
    elif score >= 40: return 4.25
    elif score >= 30: return 4.50
    elif score >= 20: return 4.75
    else: return 5.00  # Failed

# Function to process the Excel file
def process_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
    if not file_path:
        return

    try:
        df = pd.read_excel(file_path)

        # Check if 'Name' column exists
        if "Name" not in df.columns:
            messagebox.showerror("Error", "No 'Name' column found in the file!")
            return

        # Ask user for the total possible score
        total_score = simpledialog.askinteger("Input", "Enter the total possible score:", minvalue=1, maxvalue=1000)
        if not total_score:
            messagebox.showerror("Error", "Invalid total score!")
            return

        # Generate random raw scores (between 0 and total_score)
        df["Raw Score"] = [random.randint(0, total_score) for _ in range(len(df))]

        # Convert raw scores to 100-point scale
        df["Score (Out of 100)"] = (df["Raw Score"] / total_score) * 100

        # Apply grading system
        df["Grade"] = df["Score (Out of 100)"].apply(calculate_grade)
        df["Status"] = df["Grade"].apply(lambda x: "Pass" if x <= 3.00 else "Fail")

        # Save the new file
        output_file = file_path.replace(".xlsx", "_graded.xlsx")
        df.to_excel(output_file, index=False)

        messagebox.showinfo("Success", f"Graded file saved as:\n{output_file}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# GUI Setup
ctk.set_appearance_mode("Dark")  # Dark mode UI
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Excel Grading System")
root.geometry("500x300")

label = ctk.CTkLabel(root, text="Upload an Excel file with only names", font=("Arial", 16))
label.pack(pady=20)

upload_btn = ctk.CTkButton(root, text="Upload Excel File", command=process_file)
upload_btn.pack(pady=10)

root.mainloop()
