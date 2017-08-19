from Tkinter import *
import time
import datetime


root = Tk()
root.title("School Widget")
root.geometry('450x450')

now = datetime.datetime.now()

yr = str(now.year)
mn = str(now.month)
day = str(now.day)

now_month = datetime.date.today().strftime("%B")
now_day = datetime.date.today().strftime("%A")

weekday_now = now_day

#Subjects
subM = 'Maths'
subW = 'Wood'
subBreak = 'Break'
subT = 'Tech Graph'
subE = 'English'
subI = 'Irish'
subLunch = 'Lunch'
subS = 'Science'
subB = 'Business'
subH = 'History'
subR = 'Religion'
subCSPE = 'CSPE'
subG = 'Geography'
subSPHE ='SPHE'
subPE = 'P.E'
subHOME = 'Hometime'

#Teachers
teach1 = 'Mr.Brady'
teach2 = 'Mr.Dolan'
teach3 = 'friends'
teach4 = 'Mr.Howley'
teach5 = 'Mr.Daly'
teach6 = 'Ms.Gordon'
teach7 = 'Ms.Robson'
teach8 = 'Mr.Dockery'
teach9 = 'Mr.Brett'
teach10 = 'Mr.Maye'
teach11 = 'Ms.McCann'
teach12 = 'Ms.Fallon'
Me = 'family'

#Class starts at...
class_start1 = '9:15'
class_start2 = '10:00'
class_start3 = '10:40'
class_start4 = '10:55'
class_start5 = '11:35'
class_start6 = '12:15'
class_start7 = '12:55'
class_start8 = '13:30'
class_start9 = '14:05'
class_start10 = '14:40'
class_start11 = '15:15'
class_start12 = '15:50'

#Class function for school (fixed (I think) )
def next_class():
    timestamp = datetime.datetime.now().time()
    else_loading = 'Loading classes, please wait...'
    sub = 'sub'
    subAre = 'are'
    teacher = 'teacher'
    teach_never = 'loading...'
    class_start = '9:00'
    intro = 'Get ready for'
    new_intro = 'Classes'
    space = ' '
    with_it = ' with '
    at = 'at'
    
    
#   The numbers between the brackets on the second 'if' statement represent the time (24 hour clock)
#   This part is not fully completed, enough to know what's happening though
    now_class = intro + space + sub + with_it + teacher + space + at + space + class_start
    if now_day == 'Saturday':
        if datetime.time(9) <= timestamp <= datetime.time(9, 08):
            now_class = new_intro + space + subAre + space + teach_never
            return now_class
        if datetime.time(20, 07) <= timestamp <= datetime.time(20, 10):
            now_class = intro + space + subM + with_it + teach1 + space + at + space + class_start1
            return now_class
        elif datetime.time(20, 10) <= timestamp <= datetime.time(20, 13):
            now_class = intro + space + subW + with_it + teach2 + space + at + space + class_start2
            return now_class


#So we don't get any errors, cause for some reason it causes one
next_class()

func_class = next_class()

#Random string needed (not really)
of = ' of '

#Somehow makes it work, uses 'st' for every date (broken)
def fixit():
    st = 'st'
    nd = 'nd'
    rd = 'rd'
    th = 'th'
    if day == '1' or '21':
        return st
    elif day == '2' or '22':
        return nd
    elif day == '3' or '23':
        return rd
    elif day == '4' or '5' or '6' or '7' or '8' or '9' or '10' or '11' or '12' or '13' or '14' or '15' or '16' or '17' or '18' or '19' or '20' or '24' or '25' or '26' or '27' or '28' or '29' or '30':
        return th
    elif day == '31':
        return st

#Probably don't need it
choice = fixit()

#Don't remove
space = ' '

#Year, month, day. Prints the latter
ymd = day + choice + of + now_month + space + yr

#label for date
dateforme = Label(root, font=('times', 40, 'bold'), bg='white', text=ymd)
dateforme.pack(fill=BOTH)

#Label for classes (broken)
classvar = ''
classtime = Label(root, font=('times', 15), bg='white', text=func_class)
classtime.pack(fill=BOTH)

#Code for the clock I'm using
time2 = ''
clock = Label(root, font=('times', 40, 'bold'), bg='white')
clock.pack(fill=BOTH)

#For the string of the day
strDay = Label(root, font=('times', 40, 'bold'), bg='white', text=now_day)
strDay.pack(fill=BOTH)

#Refreshes time
def tick():
    global time2
    time3 = time.strftime('%H:%M:%S')
    if time3 != time2:
        time2 = time3
        clock.config(text=time3)
    clock.after(200, tick)

tick()

#Refreshes class label (broken)
def class_school():
    global classvar
    if func_class != classvar:
        classvar = func_class
        classtime.config(text=func_class)
    classtime.after(200, class_school)

class_school()

#Refreshes date (might not work)
def Refresh():
    global dateforme
    dateforme.configure(text=ymd)
    root.after(1000, Refresh)

#Refreshes clock
def Refresh2():
    global clock
    clock.configure(text=tick())
    root.after(1000, Refresh2)

#Supposed to refresh classes (broken)
def Refresh4():
    global classtime
    classtime.configure(text=class_school())
    root.after(1000, Refresh4)

#Refreshes day, not sure if it works
def Refresh3():
    global strDay
    strDay.configure(text=now_day)
    root.after(1000, Refresh3)

#Refreshes things...
Refresh()
Refresh2()
Refresh3()
Refresh4()

#Keeps all of it together
root.mainloop()
