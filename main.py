import json
import tkinter
import datetime
from tkinter import messagebox

now=datetime.datetime.now()
year=now.year
day=now.day
month=now.month

try:
        with open(file="data.json",mode="r") as file:
            read_data=json.load(file)
            current=read_data["current_streak"]
            best=read_data["best_streak"]
            j_day=read_data["day"]
            today=datetime.date(year,month,day)
            last_day=datetime.date(read_data["year"],read_data["month"],read_data["day"])

            if(today-last_day).days>1:
                #  print(day-j_day)
                 read_data["current_streak"]=0
                 with open(file="data.json",mode="w") as file:
                    json.dump(read_data, file, indent=4)
                 current=read_data["current_streak"]
except:
        t={
        "current_streak":0,
        "best_streak":0,
        "day":day-1,
        "month":month,
        "year":year,
    }
        j_day=day-1
        current=t["current_streak"]
        best=t["best_streak"]
        with open(file="data.json",mode="w") as file:
            json.dump(t,file,indent=4)

def streak_increment():
    global j_day
    with open(file="data.json",mode="r") as file:
         d=json.load(file)
         p_day=d["day"]
         current=d["current_streak"]
         best=d["best_streak"]
    # print(p_day)
    if(p_day!=day):
        # global current
        # global best
        current=current+1
        if current>best:
            best=best+1
        e={
                "current_streak":current,
                "best_streak":best,
                "day":day,
                "month":month,
                "year":year,
            }
        with open(file="data.json",mode="w") as file:
            json.dump(e,file,indent=4)
            current_slabel.config(text=f"current streak\n{current}\n\n\n\n\n")
            best_slabel.config(text=f"best streak\n{best}\n\n\n\n\n")
        with open(file="data.json",mode="r") as file:
             z=json.load(file)
             j_day=z["day"]
        c=1
        messagebox.showinfo(title="YAY!",message="Hurray!!!!!!you have successfully completed your work\nyou climbed one more step in building a habit")
        window.destroy()
    else:
         messagebox.showinfo(title="information",message="you have clicked the (YES/NO) button once this day\nyou can only press it once in a day\nthis is how it streak works")

def streak_decrement():
    with open(file="data.json",mode="r") as file:
         d=json.load(file)
         p_day=d["day"]
         current=d["current_streak"]
         best=d["best_streak"]
    print(p_day)
    if p_day!=day:
        print("done")
        # global current
        current=0
        e={
        "current_streak":0,
        "best_streak":best,
        "day":day,
        "month":month,
        "year":year, 
        }
        with open(file="data.json",mode="w") as file:
            data=json.dump(e,file,indent=4)
            current_slabel.config(text=f"current streak\n{current}\n\n\n\n\n")
            best_slabel.config(text=f"best streak\n{best}\n\n\n\n\n")
            messagebox.showinfo(title="NO!!!!!!!",message="i did not expect this could happen like this\nI am so sad😟 for yooooou")
            c=1
            window.destroy()
    else:
         messagebox.showinfo(title="information",message="you have clicked the (YES/NO) button once this day\nyou can only press it once in a day\nthis is how it streak works")


def reset():
     t={
        "current_streak":0,
        "best_streak":0,
        "day":day-1,
        "month":month,
        "year":year,
    }
     current=0
     best=0
     with open(file="data.json",mode="w") as file:
          json.dump(t,file,indent=4)
          current_slabel.config(text=f"current streak\n{current}\n\n\n\n\n")
          best_slabel.config(text=f"best streak\n{best}\n\n\n\n\n")
          print("y")


window=tkinter.Tk()
window.title("🔥🔥🔥streak_counter🔥🔥🔥")

canvas = tkinter.Canvas(window, width=300, height=300, bg="white")
fire_img=tkinter.PhotoImage(file="fire.png")
canvas.create_image(0,0,image=fire_img)
canvas.grid(row=1,column=1)

title=tkinter.Label(text="Streak-It-Up",font=("Georgia",40),foreground="orange")
title.grid(row=0,column=1)

description=tkinter.Label(text="count your streak\na best way to build a habit\nit takes 21 days to build a habit",font=("arial",10))
description.grid(row=2,column=1)

current_slabel=tkinter.Label(text=f"current streak\n{current}\n\n\n\n\n",font=("Comic Sans MS",20),fg="red")
current_slabel.grid(row=1,column=0)

best_slabel=tkinter.Label(text=f"best streak\n{best}\n\n\n\n\n",font=("Comic Sans MS",20),fg="red")
best_slabel.grid(row=1,column=2)

ask=tkinter.Label(text=f"today({day}-{month}-{year})\ndid you complete your work ?",font=("arial",15,"bold"))
ask.grid(row=3,column=1)

emoji_font = ("Segoe UI Emoji", 10)

extra=tkinter.Label(window,text="🟩🟢<---------------->🔴🟥",font=("Segoe UI Emoji", 10))
extra.grid(row=4,column=1)

about=tkinter.Label(text="NOTE : this is a strict streak counter app\n" \
"if you miss the work by 1 day also , then your current streak becomes 0\n" \
"unlike others , which have addvertisement options , it is not like that \n" \
"yse this only if you really really want to build a habit",fg="red")
about.grid(row=5,column=1)

reset_but=tkinter.Button(text="   RESET   ",fg="white",bg="blue",command=reset)
reset_but.grid(row=6,column=1)

reset_info=tkinter.Label(text="If yyou think today is day 1, then-->\n" \
"before you click this , remeber that all your streak progress will be cleared off",fg="blue")
reset_info.grid(row=7,column=1)

yes=tkinter.Button(text="   YES   ",fg="white",bg="orange",command=streak_increment)
yes.grid(row=4,column=0)

no=tkinter.Button(text="   NO   ",fg="white",bg="orange",command=streak_decrement)
no.grid(row=4,column=2)
window.mainloop()