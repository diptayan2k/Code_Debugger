import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
import time
import os
import subprocess


root = Tk()
root.state('zoomed')
root.maxsize(1920,800)
# background color
root.config(bg="grey")

Compilation_time1 = 0
Execution_time1 = 0
Compilation_time2 = 0
Execution_time2 = 0



Language1 = StringVar()
Language2 = StringVar()
Language3 = StringVar()
val1 = IntVar()
val2 = IntVar()
val3 = IntVar()
val1.set(1)
val2.set(1)

debug_flag = True

def compare_files(fpath1, fpath2):
    with open(fpath1) as file1, open(fpath2) as file2:
        for linef1, linef2 in zip(file1, file2):
            linef1 = linef1.rstrip()
            linef2 = linef2.rstrip()

            #print(linef1 + " " + linef2 + "n")
            if linef1 != linef2:
                return False
        return next(file1, None) == None and next(file2, None) == None


def codconfig1():
    value = val1.get()
    if value == 0:
        Path1.configure({"background": "white"})
        Path1.configure(state='normal')
        Button1.config(state = 'normal')
        Code1.configure(state='disabled', bg='dim grey')
    elif value == 1:
        Code1.configure(state='normal', bg='white')
        Path1.configure({"background": "dim grey"})
        Path1.configure(state='disabled')
        Button1.config(state='disabled')

def codconfig2():
    value = val2.get()
    if value == 0:
        Path2.configure({"background": "white"})
        Path2.configure(state='normal')
        Button2.config(state='normal')
        Code2.configure(state='disabled', bg='dim grey')
    elif value == 1:
        Code2.configure(state='normal', bg='white')
        Path2.configure({"background": "dim grey"})
        Path2.configure(state='disabled')
        Button2.config(state='disabled')

def configtest():
    value = val3.get()
    if value == 0:
        test.configure(state='normal', bg='white')
        Input_path.configure(state='disabled', bg='dim gray')
        Buttontest.config(state='disabled')
        Random_case.configure(state='disabled', bg='dim gray')
        Buttonrandom.config(state='disabled')
        langg_menu.configure(state='disabled')
    elif value == 1:
        Input_path.configure(state='normal', bg='white')
        Buttontest.config(state='normal')
        test.configure(state='disabled', bg='dim gray')
        Random_case.configure(state='disabled', bg='dim gray')
        Buttonrandom.config(state='disabled')
        langg_menu.configure(state='disabled')
    elif value == 2:
        Random_case.configure(state='normal', bg='white')
        Buttonrandom.config(state='normal')
        langg_menu.configure(state='normal')
        test.configure(state='disabled', bg='dim gray')
        Input_path.configure(state='disabled', bg='dim gray')
        Buttontest.config(state='disabled')

def retrieve_input(textbox):
    inputValue = textbox.get("1.0", "end-1c")
    print(inputValue)

def set_up_working_directory():
    path = filedialog.askdirectory(initialdir="C:\\Users\\DIPTAYAN BISWAS\\Desktop\\Code_Debugger", title='Please select a directory')
    Working_Directory.delete('1.0', END)
    Working_Directory.insert(tk.END, path)

def set_up_path1():
    path = filedialog.askopenfilename(initialdir="C:\\Users\\DIPTAYAN BISWAS\\Desktop\\Code_Debugger", title='Please select a directory')
    Path1.delete('1.0', END)
    Path1.insert(tk.END, path)

def set_up_path2():
    path = filedialog.askopenfilename(initialdir="C:\\Users\\DIPTAYAN BISWAS\\Desktop\\Code_Debugger", title='Please select a directory')
    Path2.delete('1.0', END)
    Path2.insert(tk.END, path)

def set_up_pathtest():
    path = filedialog.askopenfilename(initialdir="C:\\Users\\DIPTAYAN BISWAS\\Desktop\\Code_Debugger", title='Please select a directory', filetype =
        (("text files","*.txt"),("all files","*.*")))
    Input_path.delete('1.0', END)
    Input_path.insert(tk.END, path)

def set_up_pathrandom():
    path = filedialog.askopenfilename(initialdir="C:\\Users\\DIPTAYAN BISWAS\\Desktop\\Code_Debugger", title='Please select a directory')
    Random_case.delete('1.0', END)
    Random_case.insert(tk.END, path)


def clear_all():
    if val1.get()==0:
        Code1.configure(state = 'normal')
    if val2.get()==0:
        Code2.configure(state = 'normal')
    if val1.get()==1:
        Path1.configure(state = 'normal')
    if val2.get()==1:
        Path2.configure(state = 'normal')
    if val3.get() == 0:
        Input_path.configure(state = 'normal')
        Random_case.configure(state='normal')
    if val3.get() == 1:
        Random_case.configure(state = 'normal')
        test.configure(state='normal')
    if val3.get() == 2:
        Input_path.configure(state = 'normal')
        test.configure(state='normal')
    Log1.config(state='normal')
    Log2.config(state = 'normal')


    Path1.delete('1.0', END)
    Path2.delete('1.0', END)
    Input_path.delete('1.0', END)
    Random_case.delete('1.0', END)
    test.delete('1.0', END)
    Code1.delete('1.0', END)
    Code2.delete('1.0', END)
    Log1.delete('1.0', END)
    Log2.delete('1.0', END)
    langg_menu.set("CPP")
    lang_menu1.set("CPP")
    lang_menu2.set("CPP")

    if val1.get()==0:
        Code1.configure(state = 'disabled')
    if val2.get()==0:
        Code2.configure(state = 'disabled')
    if val1.get()==1:
        Path1.configure(state = 'disabled')
    if val2.get()==0:
        Path2.configure(state = 'disabled')
    if val3.get() == 0:
        Input_path.configure(state = 'disabled')
        Random_case.configure(state='disabled')
    if val3.get() == 1:
        Random_case.configure(state = 'disabled')
        test.configure(state='disabled')
    if val3.get() == 2:
        Input_path.configure(state = 'disabled')
        test.configure(state='disabled')





def save_test_case():
    if val3.get() == 0 :
        directory = Working_Directory.get("1.0", "end-1c")
        save_path = directory + "\\test.txt"
        text_file = open(save_path, "w")
        case = test.get("1.0", "end-1c")
        text_file.write(case)
        text_file.close()
        return save_path
    elif val3.get() == 1 :
        return Input_path.get("1.0", "end-1c")


def run_python_code(code_path, input_path, type) :
    global debug_flag
    global Execution_time1
    global Execution_time2

    working_dir = Working_Directory.get("1.0", "end-1c")
    title_string = ""
    if type == "1" : title_string = "Code1"
    if type == "2": title_string = "Code2"
    if type == "test" : title_string = "Random Generator"


    command = "python " + '''"''' + str(code_path) + '''" <"''' + str(input_path) + '''"> "''' + str(working_dir) + "\op" + str(type) + '''.txt"'''

    if type == "test" :

        command = "python " + '''"''' + str(code_path) + '''" > "''' + str(working_dir) + r'''\test.txt"'''
    print(command)

    #op = subprocess.run(command, shell=True, text=True, capture_output=True)
    start = time.time()
    try :
        op = subprocess.check_call(command,shell=True, timeout=7)
        if type == "1":
            Execution_time1 = time.time() - start
        if type == "2":
            Execution_time2 = time.time() - start

    except Exception as e:
        debug_flag = False
        '''lol = subprocess.run("taskkill /IM Python.exe /F", shell=True, capture_output=True)'''

        #print(lol.stderr)
        #pid  =  subprocess.run('''tasklist /fo csv | findstr /i "Python"''', shell=True, text=True, capture_output=True)
        '''
        li = list(map(str,pid.stdout.split('\n')))
        id = int(os.getpid())
        #subprocess.run("taskkill /PID " + str(id) + " /F", shell=True, capture_output=True)
        print(li)
        print(id)
        for i in li :
            li1 = list(map(str,i.split(',')))
            if (len(li1) >= 2) :
                st = li1[1]
                pp = int(st[1:len(st)-1])
                #print(pp)
                if int(pp) != int(id) :
                    print(pp)
                    #lol = subprocess.run("taskkill /PID " + str(pp) + " /F", shell=True, capture_output=True)

        #os.killpg(os.getpgid(op.pid), signal.SIGTERM)
        #copy_path = Working_Directory.get("1.0", "end-1c") + "\\code1.py"
        #shutil.copy(code_path, copy_path)
        #shutil.copy(copy_path, code_path)
        #if copy_path != code_path :
        #    os.remove(copy_path)
        '''
        messagebox.showerror("Error", "Failed to execute " + title_string + ".\nPlease re-check your code.")
        return





def run_cpp_code(code_path, input_path, type) :
    global debug_flag
    global Execution_time1
    global Execution_time2
    global Compilation_time1
    global Compilation_time2

    title_string = ""
    if type == "1": title_string = "Code1"
    if type == "2": title_string = "Code2"
    if type == "test": title_string = "Random Generator"

    working_dir = Working_Directory.get("1.0", "end-1c")
    command1 = "g++ -o" + '''"''' + working_dir + '''\m.exe" "''' + code_path + '''"'''
    command2 =  '''"''' + working_dir + '''\m.exe" <"''' + input_path + '''"> "''' + working_dir + "\op" + type + '''.txt"'''

    if type == "test" :
        command1 = "g++ -o" + '''"''' + working_dir + '''\mm.exe" "''' + code_path + '''"'''
        command2 = '''"''' + working_dir + '''\mm.exe" > "''' + str(working_dir) + r'''\test.txt"'''

    start = time.time()
    op1 = subprocess.run(command1, shell=True, text=True, capture_output=True)
    if type == "1":
        Compilation_time1 = time.time() - start
    if type == "2":
        Compilation_time2 = time.time() - start
    if (op1.returncode > 0):
        if len(op1.stderr) != 0:
            debug_flag = False
            messagebox.showerror("Error","In " + title_string + "\n" + str(op1.stderr))
            return
        else:
            debug_flag = False
            messagebox.showerror("Error", "In " + title_string + "\n" + "Runtime Error")
            return

    start = time.time()
    try :
        op2 = subprocess.call(command2, shell=True, timeout=5)
        if type == "1":
            Execution_time1 = time.time() - start
        if type == "2":
            Execution_time2 = time.time() - start
    except Exception as e:
        debug_flag = False
        lol = subprocess.run("taskkill /IM m.exe /F",shell=True, capture_output=True)
        print(lol)
        messagebox.showerror("Error", "Failed to execute " + title_string + ".\nPlease re-check your code.")
        return



def save_python_code1() :
    if val1.get() == 1:
        directory = Working_Directory.get("1.0", "end-1c")
        save_path = directory + "\code1.py"
        text_file = open(save_path , "w")
        text_file.write(Code1.get("1.0", "end-1c"))
        text_file.close()
        return  save_path
    elif val1.get() == 0 :
        save_path = Path1.get("1.0", "end-1c")
        return save_path

def save_cpp_code1() :
    if val1.get() == 1:
        directory = Working_Directory.get("1.0", "end-1c")
        save_path = directory + "\code1.cpp"
        text_file = open(save_path , "w")
        text_file.write(Code1.get("1.0", "end-1c"))
        text_file.close()
        return  save_path
    elif val1.get() == 0 :
        save_path = Path1.get("1.0", "end-1c")
        return save_path

def save_python_code2() :
    if val2.get() == 1:
        directory = Working_Directory.get("1.0", "end-1c")
        save_path = directory + "\code2.py"
        text_file = open(save_path , "w")
        text_file.write(Code2.get("1.0", "end-1c"))
        text_file.close()
        return  save_path
    elif val2.get() == 0 :
        save_path = Path2.get("1.0", "end-1c")
        return save_path

def save_cpp_code2() :
    if val2.get() == 1:
        directory = Working_Directory.get("1.0", "end-1c")
        save_path = directory + "\code2.cpp"
        text_file = open(save_path , "w")
        text_file.write(Code2.get("1.0", "end-1c"))
        text_file.close()
        return  save_path
    elif val2.get() == 0 :
        save_path = Path2.get("1.0", "end-1c")
        return save_path

def check_validity_of_extension(path, language) :
    reverse_path = path[::-1]
    if language == "Python" :
        if len(path) < 4 : return False
        if reverse_path[0:3] != "yp." : return False
    if language == "CPP":
        if len(path) < 5 : return False
        if reverse_path[0:4] != "ppc.": return False

def compare_outputs():
    if compare_files(Working_Directory.get("1.0", "end-1c") + "\op1.txt", Working_Directory.get("1.0", "end-1c") + "\op2.txt") == False :
        messagebox.showerror("Output Mismatch", "Output of both the codes does not match for the given test case")
    else :
        messagebox.showinfo("Output Match", "Output of both the codes match for the given test case")
        Log1.config(state = 'normal')
        Log1.insert(tk.END, "\t\tLog for Code 1  ")
        Log1.insert(tk.END,"\n\t\t--------------")
        Log1.insert(tk.END,"\n\n\tCompilation Time(s) :\t"+ str(Compilation_time1))
        Log1.insert(tk.END," \n\tExecution Time(s)   :\t" + str(Execution_time1))
        tot = str(Compilation_time1 + Execution_time1)
        Log1.insert(tk.END," \n\tTotal Time(s)\t\t    : "+ str(tot))
        Log1.config(state = 'disable')

        Log2.config(state='normal')
        Log2.insert(tk.END, "\t\tLog for Code 2  ")
        Log2.insert(tk.END, "\n\t\t--------------")
        Log2.insert(tk.END, "\n\n\tCompilation Time(s) :\t" + str(Compilation_time2))
        Log2.insert(tk.END, " \n\tExecution Time(s)   :\t" + str(Execution_time2))
        tot = str(Compilation_time2 + Execution_time2)
        Log2.insert(tk.END, " \n\tTotal Time(s)\t\t    : " + str(tot))
        Log2.config(state='disable')


def Debug():
    #print(os.getpid())

    global debug_flag
    debug_flag = True
    path = Working_Directory.get("1.0", "end-1c")
    isFile = os.path.exists(path)
    if isFile == False:
        messagebox.showinfo("Invalid Directory", "Please enter a valid working directory")
        return

    if len(Language1.get()) == 0 :
        messagebox.showinfo("Invalid Language", "Please enter a valid language for code1")
        return
    if len(Language2.get()) == 0 :
        messagebox.showinfo("Invalid Language", "Please enter a valid language for code2")
        return

    test_path=""
    if val3.get() == 0:
        test_path = save_test_case()
        #print(test_path)
    elif val3.get() == 1:
        test_path = Input_path.get("1.0", "end-1c")
    elif val3.get() == 2:
        if Language3.get() == "Python" and debug_flag == True:
            code_path = Random_case.get("1.0", "end-1c")
            if (check_validity_of_extension(code_path, "Python")) == False:
                messagebox.showerror("Extention-Language Mismatch", "In Random generator extension for Python must be .py")
                return
            run_python_code(code_path,"","test")
            test_path = Working_Directory.get("1.0", "end-1c") + "\\test.txt"

        if Language3.get() == "CPP" and debug_flag == True:
            code_path = Random_case.get("1.0", "end-1c")
            if (check_validity_of_extension(code_path, "CPP")) == False:
                messagebox.showerror("Extention-Language Mismatch", "In Random generator extension for CPP must be .cpp")
                return
            run_cpp_code(code_path,"","test")
            test_path = Working_Directory.get("1.0", "end-1c") + "\\test.txt"

    print(test_path)



    if Language1.get() == "Python"  and debug_flag == True:
        code_path = save_python_code1()
        if (check_validity_of_extension(code_path,"Python")) == False :
            messagebox.showerror("Extention-Language Mismatch", "In Code1 extension for Python must be .py")
            return
        run_python_code(code_path, test_path, "1")

    if Language1.get() == 'CPP' and debug_flag == True:
        code_path = save_cpp_code1()
        if (check_validity_of_extension(code_path,"CPP")) == False :
            messagebox.showerror("Extention-Language Mismatch", "In code1 extension for CPP must be .cpp")
            return


        run_cpp_code(code_path, test_path, "1")

    if Language2.get() == "Python" and debug_flag == True :
        code_path = save_python_code2()
        if (check_validity_of_extension(code_path,"Python")) == False :
            messagebox.showerror("Extention-Language Mismatch", "In code2 extension for Python must be .py")
            return
        run_python_code(code_path, test_path, "2")

    if Language2.get() == 'CPP' and debug_flag == True:
        code_path = save_cpp_code2()
        if (check_validity_of_extension(code_path,"CPP")) == False :
            messagebox.showerror("Extention-Language Mismatch", "In code2 extension for CPP must be .cpp")
            return
        run_cpp_code(code_path, test_path, "2")


    if debug_flag == True :
        compare_outputs()


# frame / base layout
frame0 = Frame(root, width=600, height=1700, bg='grey')
frame0.grid(row=0,column=0, padx=30 ,pady=5, sticky=NW)

frame1 = Frame(root, width=600, height=1700, bg='grey')
frame1.grid(row=2,column=0, padx=30 ,pady=5, sticky=NW)

frame2 = Frame(root, width=600, height=1700, bg='grey')
frame2.grid(row=1,column=0, padx=30 ,pady=5, sticky=NW)

frame3 = Frame(root, width=100, height=1700, bg='grey')
frame3.grid(row=3,column=0, padx=30 ,pady=5)

frame4 = Frame(root, width=100, height=1700, bg='grey')
frame4.grid(row=4,column=0, padx=30 ,pady=5, sticky=NW)

# Creating a photoimage object to use image
photo = PhotoImage(file=r"E:\untitled\browse.png")
# Resizing image to fit on button
photoimage = photo.subsample(15, 15)

# setting up the working directory
Label(frame0, text="Working Directory : ", bg='grey').grid(row=0, column=0, padx=5, pady=0, sticky = W)
Working_Directory = Text(frame0,height = 1,  width=154)
Working_Directory.grid(row=0, column=1, padx=5, pady=5, sticky=E)
Button(frame0, height=1, width=10, text="Browse", command=set_up_working_directory).grid(row=0, column=2, padx=5, pady=5, sticky = W)
Working_Directory.insert(tk.END, "C:\\Users\\DIPTAYAN BISWAS\\Desktop\\Code_Debugger")

# Editor for Code1
Radiobutton(frame1, text="Enter Code1 :", variable=val1, value=1, bg='grey', activebackground='grey', command=codconfig1).grid(row=0, column=0, padx=5, pady=5, sticky=NW)
Code1 = Text(frame1, height=20, width=90, bg='white')
Code1.grid(row=1, column = 0, padx=5, pady=5, sticky=NW)

# path for code 1
Radiobutton(frame2, text="Enter Path1 :", variable=val1, value=0, bg='grey', activebackground='grey', command=codconfig1).grid(row=0, column=0, padx=5, pady=0, sticky = W)
Path1 = Text(frame2, height=1, width=72, state= 'disabled', bg='dim grey')
Path1.grid(row=0, column=1, padx=5, pady=5, sticky=W)
Button1 = Button(frame2, image = photoimage,state = 'disabled', command=set_up_path1)
Button1.grid(row=0, column=2, padx=5, pady=5, sticky = W)
#Path1.insert(tk.END, "C:\\Users\\DIPTAYAN BISWAS\\Desktop\\Code_Debugger")

# Menu for Selecting language
Label(frame1 , text="\t\t\t\t  Select Language : " , bg='grey').grid(row=0, column=0, padx=5, pady=5)
lang_menu1 = ttk.Combobox(frame1, textvariable= Language1, values=['CPP', 'Python', 'Java'])
lang_menu1.grid(row=0, column=0, padx=60, pady=5, sticky=E)
lang_menu1.current(0)

# Editor For Code 2
Radiobutton(frame1, text="Enter Code2 :", variable=val2, value=1, bg='grey', activebackground='grey', command=codconfig2).grid(row=0, column=1, padx=5, pady=5, sticky=NW )
Code2 = Text(frame1, height=20, width=90,bg='white')
Code2.grid(row=1, column = 1, padx=5, pady=5, sticky=NE)
# OK button
#Button(frame1, height=1, width=10, text="OK", command=lambda: retrieve_input(Code2)).grid(row=2, column=1, padx=5, pady=5)

# path for code 2
Radiobutton(frame2, text="Enter Path2 :", variable=val2, value=0, bg='grey', activebackground='grey', command=codconfig2).grid(row=0, column=5, padx=5, pady=0, sticky = W)
Path2 = Text(frame2, height=1, width=72, state= 'disabled', bg='dim grey')
Path2.grid(row=0, column=6, padx=5, pady=5, sticky=W)
Button2 = Button(frame2, image = photoimage,state = 'disabled', command=set_up_path2)
Button2.grid(row=0, column=7, padx=5, pady=5, sticky = W)
#Path1.insert(tk.END, "C:\\Users\\DIPTAYAN BISWAS\\Desktop\\Code_Debugger")

# Menu for Selecting language
Label(frame1 , text="\t\t\t\tSelect Language: " , bg='grey').grid(row=0, column=1, padx=5, pady=5)
lang_menu2 = ttk.Combobox(frame1, textvariable= Language2, values=['CPP', 'Python', 'Java'])
lang_menu2.grid(row=0, column=1, padx=60, pady=5, sticky=E)
lang_menu2.current(0)

# Custom Test Case
Radiobutton(frame3, text="Enter Custom Test: ", variable=val3, value=0, bg='grey', activebackground='grey', command=configtest).grid(row=0, column=0, padx=5, pady=5, sticky=NW)
test = Text(frame3, height=5, width=100)
test.grid(row=1, column = 0, padx=5, pady=5, sticky=NW)

# path for input
Radiobutton(frame3, text="Enter Input file : ", variable=val3, value=1, bg='grey', activebackground='grey', command=configtest).grid(row=0, column=1, padx=5, pady=0, sticky = W)
Input_path = Text(frame3, height=1, width=76, bg='dim gray', state='disabled')
Input_path.grid(row=1, column=1, padx=5, pady=5, sticky=NW)
Buttontest = Button(frame3, image = photoimage,state = 'disabled', command=set_up_pathtest)
Buttontest.grid(row=1, column=2, padx=5, pady=5, sticky = NE)

#Path1.insert(tk.END, "C:\\Users\\DIPTAYAN BISWAS\\Desktop\\Code_Debugger")

# path for random case generator
Radiobutton(frame3, text="Genetate Test File : \t\tSelect Language :", variable=val3, value=2, bg='gray', activebackground='grey', command=configtest).grid(row=1, column=1, padx=5, sticky=W)
Random_case = Text(frame3,height=1,  width=76, bg='dim gray', state='disabled')
Random_case.grid(row=1, column=1, padx=5, pady=5, sticky=SW)
Buttonrandom = Button(frame3, image = photoimage,state = 'disabled', command=set_up_pathrandom)
Buttonrandom.grid(row=1, column=2, padx=5, pady=5, sticky = SE)

# selecting language for random case generator
langg_menu = ttk.Combobox(frame3, textvariable= Language3, values=['CPP', 'Python', 'Java'],state='disabled')
langg_menu.grid(row=1, column=1, padx=150, pady=5, sticky=E)
langg_menu.current(0)

Button(frame3, height=1, width=10, text="Debug", command= Debug).grid(row=2, column=0, padx=100, pady=5,sticky=E)
Button(frame3, height=1, width=10, text="Clear", command=clear_all).grid(row=2, column=1, padx=0, pady=5,sticky=W)

# Showing log
Log1 = Text(frame4,height=8,  width = 91, bg='dim gray')
Log1.grid(row = 4, column = 0, padx = 5, pady = 5)
Log1.config(state = 'disabled')

Log2 = Text(frame4,height=8,  width = 91, bg='dim gray')
Log2.grid(row = 4, column = 1, padx = 5, pady = 5)
Log2.config(state = 'disabled')

root.mainloop()

