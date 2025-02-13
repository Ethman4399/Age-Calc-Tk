import tkinter as tk
#Setting up the window
window = tk.Tk()
window.geometry("400x300")
window.config(bg="#F7DC6F")
window.resizable(width=True,height=False)
window.title('The Age Calculator!')
#Labels for Heading and Subheading of GUI
lb_heading = tk.Label(window,text="The Age Calculator!",font=("Arial",20),fg="black", bg="#0047ab")
lb_subheading = tk.Label(window,font=("Arial",12),text="Enter your birthday which includes the day-month-year.",fg="black",bg="#0047ab")

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


window.mainloop