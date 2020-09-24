from datetime import datetime , date
from tkinter import *
import calendar

def get_time():

    now = datetime.now()

    currnet_tym = now.strftime("%H Hours and %M Minutes")
    return currnet_tym

def get_hrs():

    now = datetime.now()

    return (now.strftime("%H"))


def get_date():

    return str(date.today())

def show_calender():

    root = Tk()
    root.title("Calender")
    year = 2020
    mycal = calendar.calendar(year)
    cal_year = Label(root,text = mycal, font= "Consolas 10 bold" )
    cal_year.pack()
    root.mainloop()
    

