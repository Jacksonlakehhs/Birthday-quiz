"""
birthday.py
Author: Jackson Lake
Credit: HHS page, talking with desk partner
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = datetime.today().day
month = month_name[todaymonth]

q1 = input("Hello, what is your name? ")
name = str(q1)
q2 = input("Hi {0}, what was the name of the month you were born in? ".format(name))
q3 = input("And what year were you born in, {0}? ".format(name))
q4 = input("And the day? ")

q1 = q1.lower()
q2 = q2.lower()
q3 = q3.lower()
q4 = q4.lower()

if q2 == "october" and q4 == "31":
    print("You were born on Halloween!")

elif q2 == month.lower() and int(q4) == todaydate:
    print("Happy birthday!")

elif q2 == "june" or q2 == "july" or q2 == "august":
    if int(q3) <= 1980:
        old = "Stone Age"
    if int(q3) >= 1980 and int(q3) <= 1990:
        old = "eighties"
    if int(q3) >= 1990 and int(q3) <= 2000:
        old = "nineties"
    if int(q3) >= 2000 and int(q3) <= 2018:
        old = "two thousands"
    print("Hi {0}, you are a summer baby of the {1}.".format(name, old)) 

elif q2 == "december" or q2 == "january" or q2 == "february":
    if int(q3) <= 1980:
        old = "Stone Age"
    if int(q3) >= 1980 and int(q3) <= 1990:
        old = "eighties"
    if int(q3) >= 1990 and int(q3) <= 2000:
        old = "nineties"
    if int(q3) >= 2000 and int(q3) <= 2018:
        old = "two thousands"
    print("Hi {0}, you are a winter baby of the {1}.".format(name, old)) 

elif q2 == "march" or q2 == "april" or q2 == "may":
    if int(q3) <= 1980:
        old = "Stone Age"
    if int(q3) >= 1980 and int(q3) <= 1990:
        old = "eighties"
    if int(q3) >= 1990 and int(q3) <= 2000:
        old = "nineties"
    if int(q3) >= 2000 and int(q3) <= 2018:
        old = "two thousands"
    print("Hi {0}, you are a spring baby of the {1}.".format(name, old)) 

elif q2 == "september" or q2 == "october" or q2 == "november":
    if int(q3) <= 1980:
        old = "Stone Age"
    if int(q3) >= 1980 and int(q3) <= 1990:
        old = "eighties"
    if int(q3) >= 1990 and int(q3) <= 2000:
        old = "nineties"
    if int(q3) >= 2000 and int(q3) <= 2018:
        old = "two thousands"
    print("Hi {0}, you are a fall baby of the {1}.".format(name, old)) 
