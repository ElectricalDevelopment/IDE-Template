from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess

compiler = Tk()
compiler.title('My Fantastic IDE')
path_for_file = ''


def set_file_path(path):
    global path_for_file
    path_for_file = path


def open_file():
    path = askopenfilename(filetypes=[('Python Files', '*.py')])
    with open(path, 'r') as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        set_file_path(path)


def save_as():
    if path_for_file == '':
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    else:
        path = path_for_file
    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path(path)


def run():
    if path_for_file == '':
        save_prompt = Toplevel()
        text = Label(save_prompt, text='Please save your code')
        text.pack()
        return
    command = f'python {path_for_file}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    output_for_code.insert('1.0', output)
    output_for_code.insert('1.0',  error)


menu_bar = Menu(compiler)

path_for_file = Menu(menu_bar, tearoff=0)
path_for_file.add_command(label='Open', command=open_file)
path_for_file.add_command(label='Save', command=save_as)
path_for_file.add_command(label='Save As', command=save_as)
path_for_file.add_command(label='Exit', command=exit)
menu_bar.add_cascade(label='File', menu=path_for_file)

run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label='Run', command=run)
menu_bar.add_cascade(label='Run', menu=run_bar)

compiler.config(menu=menu_bar)

editor = Text()
editor.pack()

output_of_code = Text(height=10)
output_for_code.pack()

compiler.mainloop()
