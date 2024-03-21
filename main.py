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

# Spinbox
unit7_label = Spinbox(text = "UNIT 7 - Data Analysis And Design").grid(row=0, column=1)
# unit9_label = Label(text = "UNIT 9 - Product Development").grid(row=1, column=0)
# unit10_label = Label(text = "UNIT 10 - Business Computing").grid(row=2, column=0)
# unit12_label = Label(text = "UNIT 12 - Mobile Technology").grid(row=3, column=0)
# unit22_label = Label(text = "UNIT 22 - Big Data Analytics ").grid(row=4, column=0)
# unit23_label = Label(text = "UNIT 23 - Cognitive Computing").grid(row=5, column=0)
# unit24_label = Label(text = "UNIT 24 - Enterprise Computing").grid(row=6, column=0)




root.mainloop()