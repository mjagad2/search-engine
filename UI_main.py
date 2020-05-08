#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 17:18:05 2020

@author: meghanajagadish
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 16:53:15 2020

@author: meghanajagadish
"""

import tkinter as tk
import p2 as p2

HEIGHT = 550
WIDTH = 600
global entry1
entry1=0
def format_response(strt,end,val,ranklist):
    global entry1
    final_str=""
    try:
        if len(ranklist)==0:
             final_str +='No RESULTS TO SHOW,\n enter new query'
             entry1=0
             return final_str
        for ele in ranklist[strt:end]:
            final_str+='\n'+ele
        if(val==1):
            final_str +='\n No MORE RESULTS TO SHOW'
            ranklist.clear()
    except:
        final_str +='No MORE RESULTS TO SHOW'
        ranklist.clear()
    
    return final_str

def get_op(rl):
    global start
    global end
    global val
    global ranklist
    global entry1
    if entry1!=1:
        label['text'] ="PLEASE ENTER QUERY FIRST!!" 
    elif entry1==1:
        if(rl.lower()=='n'):
            ranklist.clear()
            label['text'] ="  "
            entry1=0
        elif(rl.lower()=='y'):
            if (end+10)==(len(ranklist)-1) or (end+10)>(len(ranklist)-1):
                start = start+10
                end =(len(ranklist))
                val=1
                label['text'] =format_response(start,end,val,ranklist) 
            else:
                start = start+10
                end=end+10
                label['text'] =format_response(start,end,val,ranklist) 
        else:
            label['text'] ="INVALID INPUT"

def clicked(query_):
    global entry1
    global start
    global end
    global val
    global ranklist
    ranklist=[]
    ranklist.clear()
    ranklist = p2.get_output(query_)
    entry1=1
    end=10
    val=0
    start=0
    print(ranklist)
    label['text']=format_response(start,end,val,ranklist) 
    
root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()
#########
background_image = tk.PhotoImage(file='bgimg.png')
background_label = tk.Label(root,image=background_image)
background_label.place(relwidth=1, relheight=1)

frame1 = tk.Frame(root, bg='#80c13f', bd=5)
frame1.place(relx=0.5, rely=0.05, relwidth=0.75, relheight=0.05, anchor='n')

label1 = tk.Label(frame1,font=50,text="ENTER SEARCH QUERY BELOW")
label1.place(relwidth=1, relheight=1)
###############
#bg='#80c1ff'
upper_frame = tk.Frame(root, bd=5)
upper_frame.place(relx=0.5, rely=0.11, relwidth=0.75, relheight=0.1, anchor='n')

entry_q = tk.Entry(upper_frame, font=40)
entry_q.place(relwidth=0.65, relheight=1)

button = tk.Button(upper_frame, text="Search", font=40, command=lambda: clicked(entry_q.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)
###########
frame2 = tk.Frame(root, bg='#80c1ff', bd=5)
frame2.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.06, anchor='n')

label2 = tk.Label(frame2,font=40,text="DO YOU WANT TO LOAD MORE RESULTS??? Y or N")
label2.place(relwidth=1, relheight=1)
#############
frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.3, relwidth=0.75, relheight=0.07, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="submit", font=40, command=lambda: get_op(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.4, relwidth=0.75, relheight=0.57, anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

root.mainloop()