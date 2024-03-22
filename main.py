from tkinter import *

root = Tk()
root.title("Course Tracker")
root.config(padx=45, pady=20)

# Label
unit7_label = Label(text = "UNIT 7 - Data Analysis And Design").grid(row=0, column=0)
unit9_label = Label(text = "UNIT 9 - Product Development").grid(row=1, column=0)
unit10_label = Label(text = "UNIT 10 - Business Computing").grid(row=2, column=0)
unit12_label = Label(text = "UNIT 12 - Mobile Technology").grid(row=3, column=0)
unit22_label = Label(text = "UNIT 22 - Big Data Analytics ").grid(row=4, column=0)
unit23_label = Label(text = "UNIT 23 - Cognitive Computing").grid(row=5, column=0)
unit24_label = Label(text = "UNIT 24 - Enterprise Computing").grid(row=6, column=0)

# Tasks
unit7_tasks = ["P1", "P2", "P3", "P4", "P5", "P6", "M1", "M2", "M3", "D1", "D2"]
unit10_tasks = ["P1", "P2", "P3", "P4", "P5","M1", "M2", "M3", "D1", "D2"]
unit23_tasks = ["P1", "P2", "P3", "M1", "M2", "D1"]

# Function
def create_checkbox(unit_list:list = [], column_val:int = 1, row_val:int = 0, new_list:list = []) -> list:
    for task in unit_list:
        unit_check = Checkbutton(text = task).grid(row=row_val, column=column_val)
        new_list.append(unit_check)
        column_val += 1 
    
    return new_list

# Checkbox
unit7 = create_checkbox(unit_list = unit7_tasks, column_val=1, row_val=0)
unit9 = create_checkbox(unit_list = unit7_tasks, column_val=1, row_val=1)
unit10 = create_checkbox(unit_list = unit10_tasks, column_val=1, row_val=2)
unit12 = create_checkbox(unit_list = unit7_tasks, column_val=1, row_val=3)
unit22 = create_checkbox(unit_list = unit7_tasks, column_val=1, row_val=4)
unit23 = create_checkbox(unit_list = unit23_tasks, column_val=1, row_val=5)
unit24 = create_checkbox(unit_list = unit10_tasks, column_val=1, row_val=6)

root.mainloop()