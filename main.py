import os
from tkinter import *

CHECKMARK = "✓"

root = Tk()
root.title("Course Tracker")
root.config(padx=45, pady=20, background="red")

# Label
label_list = ["UNIT 7 - Data Analysis And Design","UNIT 9 - Product Development","UNIT 10 - Business Computing","UNIT 12 - Mobile Technology",
              "UNIT 22 - Big Data Analytics","UNIT 23 - Cognitive Computing","UNIT 24 - Enterprise Computing"]

count = 0
for i in label_list:
    unit_label = Label(text = i, fg = "black", bg="red").grid(row=count, column=0)
    count+=1

total_label = Label(text = "Total: 0", background="red", fg="black")
total_label.grid(column=14, row=7)

# Tasks
unit7_tasks = ["P1", "P2", "P3", "P4", "P5", "P6", "M1", "M2", "M3", "D1", "D2"]
unit10_tasks = ["P1", "P2", "P3", "P4", "P5","M1", "M2", "M3", "D1", "D2"]
unit23_tasks = ["P1", "P2", "P3", "M1", "M2", "D1"]

# Checkbox
def create_checkbox(unit_list:list = [], column_val:int = 1, row_val:int = 0) -> list:
    new_list = []
    for index, task in enumerate(unit_list):
        new_list.append(IntVar())
        button = Checkbutton(text = task, offvalue = 0, onvalue = 1, variable=new_list[index], 
                             background="red", fg = "black", selectcolor="red", activebackground="red", activeforeground="green")
        button.grid(row=row_val, column=column_val, sticky="ew")
        column_val += 1 
    
    return new_list

unit7 = create_checkbox(unit_list = unit7_tasks, column_val=1, row_val=0)
unit9 = create_checkbox(unit_list = unit7_tasks, column_val=1, row_val=1)
unit10 = create_checkbox(unit_list = unit10_tasks, column_val=1, row_val=2)
unit12 = create_checkbox(unit_list = unit7_tasks, column_val=1, row_val=3)
unit22 = create_checkbox(unit_list = unit7_tasks, column_val=1, row_val=4)
unit23 = create_checkbox(unit_list = unit23_tasks, column_val=1, row_val=5)
unit24 = create_checkbox(unit_list = unit10_tasks, column_val=1, row_val=6)
all_work = unit7 + unit9 + unit10 + unit12 + unit22 + unit23 + unit24

# Check if row is finished
def check_mark():
    row_num = 0
    for unit in [unit7, unit9, unit10, unit12, unit22, unit23, unit24]:
        print(len(unit))
        if len(unit) == len([count for count in unit if count.get()]):
            Label(text=CHECKMARK, background = "red", fg = "green").grid(column=len(unit) + 1, row=row_num)
        
        row_num += 1
  

# Load checkbutton states
if os.path.isfile("coursework.txt"):
    with open("coursework.txt") as f:
        data = f.read().split(",")
        del data[-1]   
        
        for index, var in enumerate(data):
            all_work[index].set(int(var))

# Button
def update_total():
    total = 0

    if os.path.isfile("coursework.txt"):
        with open("coursework.txt", "w") as f:
            pass

    for unit in all_work:
        with open("coursework.txt", "a") as f:
            f.write(f"{unit.get()},")
        
        if unit.get():
            total+=1

    total_label.config(text = f"Total: {total}/{len(all_work)}")
    check_mark()
    
done_button = Button(text = "Calculate Total", command=update_total, background="red", activebackground="red").grid(row=7, column = 13)
root.mainloop()