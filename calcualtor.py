#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *


# In[2]:


def click(event):
    global svalue
    text = event.widget.cget("text")
    print("text")
    if text == "=":
        if svalue.get().isdigit():
            value = int(svalue.get())
        else:
            value = eval(screen.get())
        svalue.set(value)
        screen.update()
    elif text == "C":
        svalue.set("")
        screen.update()
    else:
        svalue.set(svalue.get()+text)
        screen.update()
root = Tk()
root.configure(bg="light gray")


# In[3]:


svalue = StringVar ()
svalue.set("")
screen = Entry(root,textvar=svalue,font="Lucida 20 bold" )
screen.pack(fill=X,pady=12,padx=20,ipadx=22,ipady=12)


# In[4]:


f= Frame(root) 
b= Button(f,text="9",padx=35,pady=12, font="Lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>", click)
b= Button(f,text="8",padx=35,pady=12, font="Lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>", click)
b= Button(f,text="+",padx=35,pady=12, font="Lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>", click)
f.pack()


# In[5]:


f= Frame(root) 
b= Button(f,text="7",padx=35,pady=12, font="Lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>", click)
b= Button(f,text="6",padx=35,pady=12, font="Lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>", click)
b= Button(f,text="-",padx=35,pady=12, font="Lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>", click)
f.pack()


# In[6]:


f= Frame(root) 
b= Button(f,text="5",padx=35,pady=12, font="Lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>", click)
b= Button(f,text="4",padx=35,pady=12, font="Lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>", click)
b= Button(f,text="*",padx=35,pady=12, font="Lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>", click)
f.pack()


# In[7]:


f= Frame(root) 
b= Button(f,text="3",padx=35,pady=12, font="Lucida 25 bold")
b.pack(side=LEFT,padx=11,pady=10)
b.bind("<Button-1>", click)
b= Button(f,text="2",padx=35,pady=12, font="Lucida 25 bold")
b.pack(side=LEFT,padx=11,pady=10)
b.bind("<Button-1>", click)
b= Button(f,text="/",padx=35,pady=12, font="Lucida 25 bold")
b.pack(side=LEFT,padx=11,pady=10)
b.bind("<Button-1>", click)
f.pack()


# In[8]:


f= Frame(root) 
b= Button(f,text="1",padx=35,pady=8, font="Lucida 25 bold")
b.pack(side=LEFT,padx=11,pady=10)
b.bind("<Button-1>", click)
b= Button(f,text="0",padx=35,pady=8, font="Lucida 25 bold")
b.pack(side=LEFT,padx=11,pady=10)
b.bind("<Button-1>", click)
b= Button(f,text="=",padx=35,pady=8, font="Lucida 25 bold")
b.pack(side=LEFT,padx=11,pady=10)
b.bind("<Button-1>", click)
f.pack()


# In[9]:


f= Frame(root) 
b= Button(f,text="C",padx=35,pady=12, font="Lucida 23 bold")
b.pack(side=LEFT,padx=11,pady=10)
b.bind("<Button-1>", click)
b= Button(f,text=".",padx=35,pady=12, font="Lucida 23 bold")
b.pack(side=LEFT,padx=11,pady=10)
b.bind("<Button-1>", click)
b= Button(f,text="%",padx=35,pady=12, font="Lucida 23 bold")
b.pack(side=LEFT,padx=11,pady=10)
b.bind("<Button-1>", click)
f.pack()


# In[ ]:


root.geometry("420x680")
root.mainloop()

