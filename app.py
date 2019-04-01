from tkinter import *
from gui_operations import analyze_code, show_about, browse_files, show_help


root = Tk()
root.geometry('1400x800')
root.title("Lexer & Parser for Python language")

info_label = Label(root,
                   text="Enter your code here ... ",
                   font=("arial", 12, "bold"),
                   fg="black")
info_label.place(x=30, y=30)

code_field = Text(root,
                  width=100,
                  height=25,
                  bg="white")
code_field.place(x=30, y=80)

info_tokens_label = Label(root,
                         text="Tokens:",
                         font=("arial", 12, "bold"),
                         fg="black")
info_tokens_label.place(x=30, y=500)

tokens_field = Text(root,
                  width=100,
                  height=15,
                  bg="white")
tokens_field.place(x=30, y=530)

info_syntax_tree_label = Label(root,
                         text="Syntax tree:",
                         font=("arial", 12, "bold"),
                         fg="black")
info_syntax_tree_label.place(x=760, y=30)

syntax_tree_field = Text(root,
                  width=80,
                  height=40,
                  bg="white")
syntax_tree_field.place(x=760, y=80)

analyze_button = Button(root,
                        text="Analyze",
                        width=11,
                        height=1,
                        bg="#9B9D9C",
                        fg="black",
                        font=("arial", 10, "bold"),
                        command=lambda: analyze_code(code_field, tokens_field, syntax_tree_field, master=root))
analyze_button.place(x=630, y=470)

menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=lambda: browse_files(code_field, master=root))
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About...", command=lambda: show_about(master=root))
helpmenu.add_command(label="Help", command=lambda: show_help(master=root))
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)


root.mainloop()