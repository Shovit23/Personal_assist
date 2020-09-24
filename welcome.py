from time_m import get_hrs, get_date
from output_m import output
from database import update_last_seen , get_last_seen
from datetime import date


def greet ():


    prv_date = get_last_seen()

    tday_date = get_date()
    update_last_seen(tday_date)


    if prv_date == tday_date:
        output("Welcome Back , Sir ")

    else:
        hr = int(get_hrs())

        if hr >=3 and hr <12:

            output("Good Morning , Sir")

        elif hr >=12 and hr <16:

            output("Good Afternoon , Sir")

        else:

            output("Good Evening , Sir")

    




