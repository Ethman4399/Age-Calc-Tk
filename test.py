import time
import tkinter as tk
#Setting up the window
window = tk.Tk()
window.geometry("400x300")
window.config(bg="#ff13f0")
window.resizable(width=True,height=True)
window.title('The Age Calculator!')
window.state('zoomed')


lb_heading = tk.Label(window,text="The Age Calculator!",font=("Arial",20),fg="white", bg="#0007ab")
lb_subheading = tk.Label(window,font=("Arial",12),text="Enter your birthday which includes the day-month-year.",fg="white",bg="#0047ab")
#This creates the text that lets the user know to open the window to full screen
lb_resize = tk.Label(window,font=("Times New Roman",12),text="Make this window full screen to see the Calculator!",fg="white",bg="#ff13f0")
#This places everything in the window.
lb_heading.place(x=400,y=30)
lb_subheading.place(x=400, y=80)
lb_resize.place(x=5,y=30)
if window.state() == 'zoomed':
    lb_resize = tk.Label(window,font=("Times New Roman",12),text="Make this window full screen to see the Calculator!",fg="#ff13f0")
window.mainloop()
