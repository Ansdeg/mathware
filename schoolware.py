from tkinter import *
root = Tk()
root.title('Ethiope Technologies. Coding for all...')
root.geometry('1350x800')
note = Toplevel(root, bg='red')
note.withdraw()
master = Tk()
master.geometry('1350x800')

availability = ['free']
#final_ans = []
my_callbacks = ['placeholder']
entered_values = []


task_frame = Frame(root, height=613, bd=8, bg='lightblue', padx=8, pady=8)   #frame for all the tasks 
task_frame.pack(side= LEFT, anchor = CENTER)
#task_frame.pack_propagate(0)

my_frame = Frame(root, height=500, width=600, bd=8, bg='lightblue', padx=8, pady=8)   #mainframe 
my_frame.pack(side = RIGHT)
my_frame.pack_propagate(0)


#CREATING TASK BUTTONS
addition_bttn = Button(task_frame, height = 2, bd= 2, text = 'Add numbers', bg = 'green',\
fg = 'white', padx = 2, command = None, font= 16) #first task, addition task
addition_bttn.pack(side = TOP)#button, heading,

number_base = Button(task_frame, height = 2, bd= 2, text = 'Number Base', bg = 'green',\
fg = 'white', padx = 2, command = None, font= 16) #first task, addition task
number_base.pack(side = TOP)


#FRONT END WIDGETS
title_label = Label(my_frame, height = 2, width = 30, bd= 2, bg = 'white',\
                    font = ('Arial', 20, 'bold'), text = ' Click On Any Task ') #title
title_label.pack(side = TOP, anchor=CENTER, pady =15)

exit_bttn = Button(my_frame, bg = 'red', fg = 'white', height =2, padx =2, width = 10, \
text = 'Exit task', bd= 2, command = None, font= 16)
exit_bttn.pack(side = BOTTOM, anchor=W, pady =15)

answer_label = Label(my_frame, bg = 'white', font = ('Arial', 20, 'bold'), width = 30, fg = 'green')


#EXECUTION STAGE WIDGETS
entry = Entry(my_frame,  bd= 10,)
label = Label(my_frame, height = 2, bd= 10, bg= 'blue',fg= 'white',)
button = Button(my_frame, height = 2, bd= 10, bg = 'green', fg= 'white', text = 'Click to continue',)
        
def callbacks ():
    if my_callbacks[0] == 'addition':
        button.config(command = addition_callback)
    elif my_callbacks[0] == 'numberbase':
        button.config(command = numberbase_callback)

def addition_task():
    my_callbacks.clear()
    my_callbacks.append('addition')
    callbacks ()
    if availability[0] == 'free':
        availability[0] = 'busy'
        entry.pack(side = TOP, anchor=CENTER,)         
        label.pack(side = TOP, anchor=CENTER,) 
        button.pack(side = TOP, anchor=CENTER,)
        entry.config(state = 'normal')
        global n
        n = 0
        
        global all_values
        all_values = ['first number', 'second number']        
        title_label.config(text = 'Add Numbers')
        label.config(text = f' Enter {all_values[n]}')
def addition_callback ():    
    #try:
        my_value = entry.get()
        if my_value == "" or type(int(my_value)) == str: #questionable code needs to be reviewed
            pass
        else:
            entered_values.append(my_value)            
            if len(entered_values) < len(all_values): 
                k = n + 1
            else:
                k = n
            entry.delete(0, END)

            label.config(text = f' Enter {all_values[k]}')
            if len(entered_values) == len(all_values): 
                c = int(entered_values[0]) + int(entered_values[1])
                ans = f'The sum of {entered_values[0]} and {entered_values[1]} is {c}'
                answer_label.config(text = ans,)
                answer_label.pack(side = BOTTOM, anchor=CENTER, pady =15)
                entry.config(state = 'disabled')


def numberbase_task():
    my_callbacks.clear()
    my_callbacks.append('numberbase')
    callbacks ()
    if availability[0] == 'free':
        availability[0] = 'busy'
        entry.pack(side = TOP, anchor=CENTER,)         
        label.pack(side = TOP, anchor=CENTER,) 
        button.pack(side = TOP, anchor=CENTER,)
        entry.config(state = 'normal')
        global n
        n = 0

        global all_values
        all_values = ['Number']
        title_label.config(text = 'Convert base 10 number to base 2')
        label.config(text = f' Enter {all_values[n]}')
def numberbase_callback ():
    #try:
        my_value = entry.get()
        if my_value == "" or type(int(my_value)) == str: #questionable code needs to be reviewed
            pass
        else:
            entered_values.append(my_value)            
            if len(entered_values) < len(all_values): 
                k = n + 1
            else:
                k = n
            entry.delete(0, END)

            label.config(text = f' Enter {all_values[k]}')
            
            if len(entered_values) == len(all_values): 
                number = entered_values[0]
                number = int(number)                
                rek = ''
                k = []
                while 2 <= number:
                    k.append (number%2)
                    number = number//2
                k.append(number)
                for i in k:
                    rek =  str(i) + rek 
                ans = f'{entered_values[0]} converted to base two is {rek}'
                answer_label.config(text = ans,)
                answer_label.pack(side = BOTTOM, anchor=CENTER, pady =15)
                entry.config(state = 'disabled')

def exit_callback ():
    availability[0] = 'free'
    title_label.config(text = ' Click On Any Task ')    
    button.pack_forget()
    label.pack_forget()
    entry.pack_forget()
    answer_label.pack_forget()
    entry.delete(0, END)
    entered_values.clear()
    my_callbacks.clear()
    n = 0
    answer_label.config(text = "") 
    answer_label.pack_forget() 

def close_app():
    #destroy all widget
    root.destroy


addition_bttn.config(command = addition_task)
number_base.config(command = numberbase_task)
exit_bttn.config(command = exit_callback)
my_frame.pack(side= LEFT, anchor = CENTER)
my_frame.pack_propagate(0)
root.mainloop()



        











