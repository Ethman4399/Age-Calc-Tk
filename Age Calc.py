import tkinter as tk
#Setting up the window
window = tk.Tk()
window.geometry("400x300")
window.config(bg="#F7DC6F")
window.resizable(width=True,height=True)
window.title('The Age Calculator!')
window.state('zoomed')
print(window.state())

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
e_month = tk.Entry(window,width=5)
e_year = tk.Entry(window,width=5)

#Button to calculate age
btn_calculate_age = tk.Button(window,text="Calculate Age!",font=("Arial",13), command='get_age')
lb_calculated_age = tk.Label(window,text="The Calculated Age is: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#0047ab")
tbox_age=tk.Text(window,width=5,height=0,state="disabled")
btn_exit = tk.Button(window,text="Exit Application!",font=("Arial",13),command=exit)

lb_heading.place(x=400,y=30)
lb_subheading.place(x=400, y=80)
lb_resize.place(x=10,y=30)
lb_date.place(x=400, y=100)
lb_month.place(x=400, y=120)
lb_year.place(x=400, y=140)
e_date.place(x=450, y=100)
e_month.place(x=450, y=120)
e_year.place(x=450, y=140)
window.mainloop()