from tkinter import *
from tkinter.filedialog import asksaveasfilename , askopenfilename
from tkinter import colorchooser
from tkinter import messagebox
import subprocess



compiler = Tk()
compiler.title("Lazy Python")
compiler.iconbitmap(r'web_programming_XSI_icon.ico')



file_path = ''
def set_file_path(path):
    global  file_path
    file_path = path


def color_me():
    clr = colorchooser.askcolor(title="select color")
    editor.config(background =clr[1])

def open_file():
    path = askopenfilename(filetypes = [('Python Files','*.PY')])
    with open(path,'r') as file:
        code = file.read()
        editor.delete('1.0',END)
        editor.insert('1.0',code)
        set_file_path(path)

"""def find():
    text.tag_remove('found','1.0',END)
    s = edit.get()
    if s:
        idx = '1.0'
        while 1:
            idx = text.search(s,idx,nocase=1,stopindex=END)
            if not idx:break
            lastidx = '%s+%dc' %(idx,len(s))
            text.tag_add('found',idx,lastidx)
            idx = lastidx
        text.tag_config('found',foreground='red')
    edit.focus_set()
butt.config(command=find)"""


def save_as():
    if file_path=='':
        path = asksaveasfilename(filetypes = [('Python Files','*.PY')])
    else:
        path = file_path
    with open(path,'w') as file:
        code = editor.get('1.0',END)
        file.write(code)
        set_file_path(path)

def run():
    if file_path=='':
        text = messagebox.showwarning("","first save your file!")
        text.pack()

        return

    command = f'python {file_path}'
    process = subprocess.Popen(command, stdout = subprocess.PIPE , stderr = subprocess.PIPE, shell=True)
    output , error = process.communicate()
    code_output.insert(END, output)
    code_output.insert(END,error)





menu_bar = Menu(compiler)



file_menu = Menu(menu_bar,tearoff = 0)
file_menu.add_command(label = 'open',command = open_file)
file_menu.add_command(label = 'save',command = save_as)
file_menu.add_command(label = 'save as',command =save_as)
file_menu.add_command(label = 'Exit',command = exit)
menu_bar.add_cascade(label = 'File' , menu= file_menu)

run_bar = Menu(menu_bar,tearoff = 0)
run_bar.add_command(label = 'Run' ,command = run )
menu_bar.add_cascade(label = 'Run',menu= run_bar)

edit_menu = Menu(menu_bar,tearoff = 0)
edit_menu.add_command(label = 'Replace',command =exit)
edit_menu.add_command(label = 'Redo',command =exit)
edit_menu.add_command(label = 'Undo',command =exit)
edit_menu.add_command(label = 'Copy',command = exit)
edit_menu.add_command(label = 'Paste',command =save_as)
menu_bar.add_cascade(label = 'Edit' , menu= edit_menu)

setting_menu = Menu(menu_bar,tearoff = 0)
setting_menu.add_command(label = 'Change background',command =color_me)
menu_bar.add_cascade(label = 'Setting' , menu= setting_menu)

frame = Frame()
Label(frame,text='text to find').pack(side=LEFT)
edit = Entry(frame)
edit.pack(side=LEFT,fill=BOTH,expand=1)
edit.focus_set()
butt = Button(frame,text='find')
butt.pack(side=RIGHT)
frame.pack(side=TOP)
text= Text(compiler)



compiler.config(menu = menu_bar)





editor = Text(width=800)

editor.pack()


code_output = Text(height =15, width = 800)

code_output.config(background='lightblue')

code_output.pack()


compiler.mainloop()
