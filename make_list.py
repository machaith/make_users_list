#!/usr/bin/env python
import string
import tkMessageBox
import tkFileDialog
from Tkinter import *

global file_m
file_m = '' 
global file_f
file_f = ''
global choice
choice = 0

def make_list_F_L(file_m,file_f):
    #Will make a firstname.lastname file
        with open(file_m,'r') as file:
                names = file.readlines()
                with open('out.txt','w') as out_file:
                        for first_name in names:
                                for last_name in names:
                                        out_file.write(first_name.rstrip()+'.'+last_name) 
        with open('female.txt','r') as female_file:
                namesf = female_file.readlines()
        with open('out.txt','a') as out_file:
                for first_name in namesf:
                        for last_name in names:
                                out_file.write(first_name.rstrip()+'.'+last_name)                                        
      
def make_list_FI_L(file_m,file_f):
        #Will make a first initial and last name file
        initials = string.ascii_lowercase
        with open(file_m,'r') as file:
            names = file.readlines()
            with open('out.txt','w') as out_file:
                for name in names:
                        for l in initials:
                                out_file.write(l+'.'+name+'\n')                 
                                
def make_list_L_FI(file_m,file_f):
        #Will make a last name and first initial file
        initials = string.ascii_lowercase
        with open(file_m,'r') as file:
            names = file.readlines()
            with open('out.txt','w') as out_file:
                for l in initials:
                        for name in names:
                                out_file.write(name.rstrip()+'.'+l+'\n')

def make_list_L_FI_n(file_m,file_f):
        #Will make a last name and first initial file without a dot
        initials = string.ascii_lowercase
        with open(file_m,'r') as file:
            names = file.readlines()
            with open('out.txt','w') as out_file:
                for l in initials:
                        for name in names:
                                out_file.write(name.rstrip()+l+'\n')

def sel():
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)
   global choice
   choice = var.get()
   


def get_file_m():
        global file_m
        file_m = tkFileDialog.askopenfilename(filetypes=[("Text files","*.txt")])
        with open(file_m,'r') as file:
                sum_m =  sum(1 for _ in file_m)
                label_m.config(text = "Male names file contains: %d names"% sum_m)
                
        

                              
def get_file_f():
        global file_f
        file_f = tkFileDialog.askopenfilename(filetypes=[("Text files","*.txt")])
        with open(file_f,'r') as file:
                sum_f = sum(1 for _ in file_f)
                label_f.config(text = "Female names file contains: %d names"% sum_f)
                
def execute_choice():
        if(choice == 0):
                tkMessageBox.showinfo( "Error", "You have to select an option")
                exit()
        if(file_m == ''):
                tkMessageBox.showinfo( "Error", "You have to select a file")
                exit()

        
        
        if choice == 1:
                
                make_list_F_L(file_m,file_f)
        elif choice == 2:
                
                make_list_FI_L(file_m,file_f)
        elif choice == 3:
                
                make_list_L_FI(file_m,file_f)
        elif choice == 4:
                
                make_list_L_FI_n(file_m,file_f)
        tkMessageBox.showinfo( "Execution Complete", "Done, Please chek the file output.txt")

def exit_program():
        exit()

top = Tk()

filename = ''


labelframe = LabelFrame(top, text="Creat a user list from files containing names")
labelframe.pack(fill="both", expand="yes")

left = Label(labelframe, text="The method used is based on you choices.")
left.pack()

left = Label(labelframe, text="Choose a number from the list below")
left.pack()



B = Button(top, text ="Choose Male names file", command = get_file_m )

B.pack()

B = Button(top, text ="Choose Female names file", command = get_file_f )

B.pack()

var = IntVar()

R1 = Radiobutton(top, text="1 - First name.Last name", variable=var, value=1,
                  command=sel)
R1.pack( anchor = W )

R2 = Radiobutton(top, text="2 - First Initial.Last name", variable=var, value=2,
                  command=sel)
R2.pack( anchor = W )

R3 = Radiobutton(top, text="3 - Last name.First Initial", variable=var, value=3,
                  command=sel)
R3.pack( anchor = W)

R4 = Radiobutton(top, text="4 - Last name First Initial", variable=var, value=4,
                  command=sel)
R4.pack( anchor = W )
label = Label(top)
label.pack()

label_m = Label(top)
label_m.pack()

label_f = Label(top)
label_f.pack()

B = Button(top, text ="Make File", command = execute_choice )

B.pack()

B = Button(top, text ="Exit", command = exit_program )

B.pack()

top.mainloop()

if __name__ == '__main__':
    app.run()
