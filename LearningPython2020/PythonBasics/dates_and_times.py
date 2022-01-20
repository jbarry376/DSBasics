# --------------------------------
# Working with Dates and Times
# using datetime module  
# --------------------------------
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
from datetime import tzinfo, timezone



# date, time, datetime classes 
# display today's date in various formats
def show_today():
  ## DATE OBJECTS
  # Get today's date from the today() method from the date class
  today = date.today()
  print ("Today's date is ", today)
  
  # print out the date's individual components
  print ("Date Components: ", today.day, today.month, today.year)
  
  # retrieve today's weekday (0=Monday, 6=Sunday)
  print ("Today's Weekday #: ", today.weekday())
  days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
  print ("Which is a " + days[today.weekday()])
  
  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  today = datetime.now()
  print  ("The current date and time is ", today)
  
  # Get the current time
  t = datetime.time(datetime.now())
  print ("The current time is ", t)

  # get the current date and time with timezone utc 
  t = datetime.now(timezone.utc)
  print("The current date and time, timezone UTC is: ", t)


# TIMEDELTA
# make basic time delta object
# show how many days until May 4th  
def show_timedelta():
    # basic timedelta 
    print("Basic timedelta: ", timedelta(days = 365, hours = 3, minutes = 12))

    # show the date one week ago 
    t = datetime.now() - timedelta(weeks=1)
    # format datetime object string 
    s = t.strftime("%A, %B %d %Y")
    print(f"One week ago was {s}")

    # show how many days until May 4th 
    today = date.today()
    mf = date(today.year, 5, 4)
    if today == mf:
        print("May the 4th be with you!")
    elif mf < today: 
        print(f"May 4th was {(today - mf).days} days ago")
        mf_next = mf.replace(year = today.year +1)
        print(f"{(mf_next - today).days} days until next May 4th")
    elif mf > today: 
        print(f"May 4th is in {(mf-today).days} days")        

# FORMATTING DATES and TIMES
def show_time_formats():
  # Times and dates can be formatted using a set of predefined string
  # control codes 
  now = datetime.now() # get the current date and time
  
  #### Date Formatting ####
  
  # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
  print (now.strftime("The current year is: %Y")) # full year with century
  print (now.strftime("%a, %d %B, %y")) # abbreviated day, num, full month, abbreviated year
  
  # %c - locale's date and time, %x - locale's date, %X - locale's time
  print (now.strftime("Locale date and time: %c"))
  print (now.strftime("Locale date: %x"))
  print (now.strftime("Locale time: %X"))
  
  #### Time Formatting ####
  
  # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
  print (now.strftime("Current time: %I:%M:%S %p")) # 12-Hour:Minute:Second:AM
  print (now.strftime("24-hour time: %H:%M")) # 24-Hour:Minute

