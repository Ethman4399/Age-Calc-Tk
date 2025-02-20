#IMPORTS
#Date and time modules
from datetime import date
#Tkniter window imports.
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
# ___________________ FUNCTIONS _______________________
def validation():
#gets the three entries (Date, Month and year)
#From get_age() function kept these inputs as strings to validate rather than converting
    d= e_date.get()
    y= e_year.get()
    m = month_chosen.current()
    msg = ''

    if len(d) == 0 or len (y) == 0:
      msg = 'day, month and year can\'t be empty'
    else: 
        try:
            if any (ch.isdigit() for ch in d) == False:
                msg = 'day must be a NUMBER'
            elif m == 0:
                msg = 'choose an appropriate MONTH'
            elif any(ch.isdigit() for ch in y) == False:
                msg = 'year must be a NUMBER'
            else:
                msg = 'Here is your calculated age!'
                day = int(d)
                month = m #month us already in number form list pos
                year = int(y)
                calc_age = find_age(day, month, year)
                display_calc_age(calc_age)

        except Exception as ep:
            messagebox.showerror('error', ep)
    if msg != '':
            messagebox.showinfo('message', msg)

def find_age(d, m, y):
    #find the age (difference between current and date of birth)
    age = today.year-y-((today.month, today.day)<(m,d))
    return age

def display_calc_age(age):
    tbox_age.config(state='normal')
    #age calculated is inserted into the text box after clearing the previous info in the textbox
    tbox_age.delete('1.0', tk.END)
    tbox_age.insert(tk.END,age)
    tbox_age.config(state='disabled')

def exit():
    window.destroy()

# ___________________  MAIN ________________________
#Setting up the window
window = tk.Tk()
window.geometry("400x300")
window.config(bg="#F7DC6F")
window.resizable(width=True,height=True)
window.title('The Age Calculator!')
window.state('zoomed')
print(window.state())

#Create a objext which stores today's whole date
today = date.today()

#Labels for Heading and Subheading of GUI
lb_heading = tk.Label(window,text="The Age Calculator!",font=("Arial",20),fg="black", bg="#F7DC6F")
lb_subheading = tk.Label(window,font=("Arial",12),text="Enter your birthday which includes the day-month-year.",fg="black",bg="#F7DC6F")
lb_resize = tk.Label(window,font=("Times New Roman",12),text="Make this window full screen to see the Calculator!",fg="black",bg="#F7DC6F")

#labels for date, month and year
lb_date = tk.Label(window,text = "Date: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#F7DC6F")
lb_month = tk.Label(window,text = "Month: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#F7DC6F")
lb_year = tk.Label(window,text = "Year: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#F7DC6F")

#Input boxes for the date, month and year.
e_date = tk.Entry(window,width=5)
e_year = tk.Entry(window,width=5)

#combobox
n = tk.StringVar()
month_chosen = ttk.Combobox(window, textvariable = n, width=12)

#adding combobox drop down menu
month_chosen['values'] = ('Select a date...',
                            'January',
                            'February',
                            'March',
                            'April',
                            'May',
                            'June',
                            'July',
                            'August',
                            'September',
                            'October',
                            'November',
                            'December')

#Button to calculate age
btn_calculate_age = tk.Button(window,text="Calculate Age!",font=("Arial",13), command=validation)
lb_calculated_age = tk.Label(window,text="The Calculated Age",font=('Arial',12,"bold"),fg="darkgreen",bg="#F7DC6F")
tbox_age=tk.Text(window,width=10,height=1,state="disabled", bg="white",fg="black")
btn_exit = tk.Button(window,text="Exit Application!",font=("Arial",13),command=exit)

#This code places everything in the tk window using .place()
lb_heading.place(x=450,y=30)
lb_subheading.place(x=450, y=80)
lb_resize.place(x=10,y=30)
lb_date.place(x=450, y=100)
lb_month.place(x=450, y=120)
lb_year.place(x=450, y=140)
e_date.place(x=510, y=100)
month_chosen.place(x=510, y=120)
e_year.place(x=510, y=140)
btn_calculate_age.place(x=450,y=165)
lb_calculated_age.place(x=400,y=200)
tbox_age.place(x=570,y=200)
btn_exit.place(x=500,y=230)

window.mainloop()