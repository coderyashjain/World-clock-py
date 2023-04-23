from tkinter import *
from datetime import datetime
from PIL import ImageTk,Image
import pytz
import time


root=Tk()
root.title("Universal TIME")
root.geometry("1000x1000")

print("code initiated")

maps_in=ImageTk.PhotoImage(Image.open("indiamap.jpg"))
maps_us=ImageTk.PhotoImage(Image.open("usamap.jpg"))
maps_au=ImageTk.PhotoImage(Image.open("australiamap.jpeg"))
maps_ja=ImageTk.PhotoImage(Image.open("japanmap.jpg"))




#-----gui-----#

label_in=Label(root,text="India")
label_in.place(relx=0.1,rely=0.05,anchor=CENTER)
label_us=Label(root,text="USA")
label_us.place(relx=0.7,rely=0.05, anchor=CENTER)
label_au=Label(root,text="Australia")
label_au.place(relx=0.1,rely=0.6,anchor=CENTER)
label_ja=Label(root,text="Japan")
label_ja.place(relx=0.7,rely=0.6,anchor=CENTER)


la_in_im=Label(root)
la_in_im['image']=maps_in
la_in_im.place(relx=0.2, rely=0.2, anchor=CENTER)
la_im_us=Label(root)
la_im_us['image']=maps_us
la_im_us.place(relx=0.8, rely=0.2, anchor=CENTER)
la_im_au=Label(root)
la_im_au['image']=maps_au
la_im_au.place(relx=0.2, rely=0.8,anchor=CENTER)
la_im_ja=Label(root)
la_im_ja['image']=maps_ja
la_im_ja.place(relx=0.8, rely=0.8,anchor=CENTER)

time_in=Label(root)
time_in.place(relx=0.2, rely=0.5, anchor=CENTER)
time_us=Label(root)
time_us.place(relx=0.8, rely=0.5, anchor=CENTER)
time_au=Label(root)
time_au.place(relx=0.2, rely=0.99, anchor=CENTER)
time_ja=Label(root)
time_ja.place(relx=0.8, rely=0.99, anchor=CENTER)

class India():
    def times(self):
        home=pytz.timezone("Asia/Kolkata")
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        time_in["text"]=current_time
        time_in.after(200,self.times)
class USA():
    def times(self):
        home=pytz.timezone("US/Central")
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        time_us["text"]=current_time
        time_us.after(200,self.times)     
class australia():
    def times(self):
        home=pytz.timezone("Australia/ACT")
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        time_au["text"]=current_time
        time_au.after(200,self.times)          
        
class japan():
    def times(self):
        home=pytz.timezone("Japan")
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        time_ja["text"]=current_time
        time_ja.after(200,self.times)
        
obj_ja=japan()      
obj_in=India()
obj_us=USA()
obj_au=australia()

button_in=Button(root,text="Show Time",command=obj_in.times)
button_in.place(relx=0.3,rely=0.05,anchor=CENTER)
button_ja=Button(root,text="Show time",command=obj_ja.times)   
button_ja.place(relx=0.8,rely=0.599,anchor=CENTER)
button_au=Button(root,text="Show time",command=obj_au.times)   
button_au.place(relx=0.2,rely=0.6,anchor=CENTER)
button_us=Button(root,text="Show time",command=obj_us.times)   
button_us.place(relx=0.8,rely=0.05,anchor=CENTER)        
        
root.mainloop()