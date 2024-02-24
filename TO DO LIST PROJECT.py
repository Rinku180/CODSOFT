#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
from tkinter import messagebox

root= Tk()
root.title("TO DO LIST")
root.geometry("520x680+500+200")
root.resizable(0,0)
root.config(bg="#00008B")


# In[2]:


def newTask():
    task=my_Entry.get()
    if task !="":
        listb.insert(END,task)
        my_Entry.delete(0,"end")
    else:
        messagebox.showWarning("Warning","please enter some task")
    


# In[3]:


def deleteTask():
    listb.delete(ANCHOR)


# In[4]:


f1= Frame(root)

f1.pack(pady=20)


# In[5]:


listb= Listbox(f1,width=25,height=10,font=("Arial", 25), selectbackground='#a6a6a6',fg='#464646')
listb.pack(side="left")


# In[6]:


sb = Scrollbar(f1)
sb.pack(side="right")


# In[7]:


listb.config(yscrollcommand=sb.set)
sb.config(command=listb.yview)


# In[8]:


my_List =['BRUSH','MEDITATION','WORKOUT','BREAKFAST','CODING','MEETING','LUNCH','1 HOUR NAP','CODING']
for i in my_List:
    listb.insert(END,i)


# In[9]:


my_Entry = Entry(root,font=("Arial", 25))
my_Entry.pack(pady=10)


# In[10]:


button_frame = Frame(root)
button_frame.pack()


# In[11]:


b1 = Button(button_frame,text="ADD TASK",font=('times 14'),bg='#DC143C',padx=18,pady=18,command=newTask)
b1.pack(side=LEFT)


# In[12]:


b2 = Button(button_frame,text="DELETE TASK",font=('times 14'),bg='#006400',padx=18,pady=18,command=deleteTask)
b2.pack(side=LEFT)


# In[ ]:


mainloop()

