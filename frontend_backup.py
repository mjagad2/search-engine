#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 18:18:48 2020

@author: meghanajagadish
"""
import string,sys
import tkinter as tk
import p2 as p2


window = tk.Tk()
window.title("Welcome to UIC SEARCH ENGINE!!")
window.geometry('850x600')
#text = tk.Text(window)

#rankList=[]
def print_results(strt,end,val,ranklist):
    opt=tk.StringVar()
    op=""
    for ele in ranklist[strt:end]:
        op=op+'\n'+ele
    #opt.set(str(op))
    lbl3= tk.Label(window ,text=op, height= 11)
    lbl3.grid(column=1, row=3)
    if(val==1):
        lbl4= tk.Label(window, text="NO MORE RESULTS TO SHOW")
        lbl4.grid(column=0, row=25)
    return
    
def call_print(ranklist,start,end,val):
    
    print("here")
    print(end)
    lbl2= tk.Label(window, text="Load more result Y ,N")     
    lbl2.grid(column=0, row=15)
    txt2 = tk.Entry(window,width=40)
    txt2.grid(column=1, row=20)
            
    def clicked2():
        rl = txt2.get()
        next_step(ranklist,start,end,val,rl)
            
    btn2 = tk.Button(window, text="enter", command=clicked2)
    btn2.grid(column=2, row=20)
            
    def next_step(ranklist,start,end,val,rl):
        if(rl.lower()=='n'):
            print(rl)
            sys.exit()
        elif(rl.lower()=='y'):
            if (end+10)==(len(ranklist)-1) or (end+10)>(len(ranklist)-1):
                start = start+10
                end =(len(ranklist))
                val=1
                print_results(start,end,val,ranklist) 
                sys.exit()
            else:
                start = start+10
                end=end+10
                print_results(start,end,val,ranklist) 
               # call_print(ranklist,start,end,val)
        else:
                print("INVALID INPUT")
            
    return end
            
        



#Code to add widgets will go here...

lbl = tk.Label(window, text="Enter you search query")
lbl.grid(column=0, row=0)

txt = tk.Entry(window,width=40)

txt.grid(column=1, row=0)

def clicked():
    ranklist=[]
    query_ = txt.get()
    print(query_)
    ranklist = p2.get_output(query_)
    end=10
    val=0
    start=0
    if(len(ranklist)< 10):
        print("rrr:", ranklist)
        print("There are only ", len(ranklist), "results for the entered query!!!")
        end = (len(ranklist))
        val=1
        print_results(start,end,val,ranklist) 
    else:
        print_results(start,end,val,ranklist) 
        call_print(ranklist,start,end,val)
        
    

btn = tk.Button(window, text="SEARCH", command=clicked)

btn.grid(column=2, row=0)


window.mainloop()

