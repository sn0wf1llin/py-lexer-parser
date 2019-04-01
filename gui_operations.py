from tkinter import END, CENTER, filedialog, Tk, Label, PhotoImage
from main import run, read_file
import tkinter
from PIL import ImageTk, Image

HELP_MSG = "(!!!) You need to load .py code via click on [ Browse ... ] \nbutton or write your own python code in the " \
           "main TextBox to get results.\n\n\n[ Analyze ]    button -- Starts code analyzing process\nFile -> Open " \
           "-- Opens FileDialog window to help you \nselect a file and loads the .py code " \
           "file\n\nFile -> Exit ... close the main program window and exit\n\nHelp -> About ... shows program's About " \
           "window\n\nHelp -> Help ... shows Help window with the usage of this program "

ABOUT_MSG = "Lexer & Parser Program for Python language\n\n(!!!)\n\n* for .py files only\n\n"
ABOUT_MSG += "v0.1 supports simple .py code \nwith !NO! functions, decorators or any other hard constructions\n"
ABOUT_FOOTER = "Author: N. Shynkevich\n\nFor OKPO, task 3 (Lexer & Parser)\n\nAll rights reserved"


def browse_files(code_place, master):
    try:
        file = filedialog.askopenfile(
            filetypes=[('Files with python code only', '.py')],
            parent=master,
            title="Select .py code file to analyze")

        code = read_file(file.name)
        code_place.delete('1.0', END)
        code_place.insert(END, code)
    except AttributeError:
        pass


def analyze_code(field_get_code_from, field_insert_result_tokens_to, field_insert_result_tree_to, master):
    code = field_get_code_from.get(1.0, END)
    if len(code) <= 1:
        show_alert("Your code is too short to analyze it effectively", master=master)
    else:
        tokens, syntax_tree = run(code=code, fname=None)

        field_insert_result_tokens_to.delete('1.0', END)
        field_insert_result_tokens_to.insert(END, tokens)

        field_insert_result_tree_to.delete('1.0', END)
        field_insert_result_tree_to.insert(END, syntax_tree)


def show_help(master):
    h = tkinter.Toplevel(master)
    h.wm_title("Help")
    h.geometry('600x300')
    h.configure(background='white')
    h.resizable(False, False)

    help_label = Label(h,
                       font=("Helvetica", 12),
                       bg='white',
                       fg="black",
                       text=HELP_MSG,
                       justify=CENTER)

    help_label.pack()


def show_alert(msg, master):
    a = tkinter.Toplevel(master)
    a.wm_title("ALERT!")
    a.geometry('600x300')
    a.configure(background='white')
    a.resizable(False, False)

    alert_label = Label(a,
                        font=("Helvetica", 12),
                        fg="black", bg='white',
                        text=msg,
                        justify=CENTER)

    alert_label.place(x=130, y=12)

    img = Image.open('alert.png')
    img = ImageTk.PhotoImage(img)
    img_label = Label(a, image=img, bg='white')
    img_label.image = img
    img_label.place(x=12, y=35, relwidth=1, relheight=1)

def show_about(master):
    a = tkinter.Toplevel(master)
    a.wm_title("About this program")
    a.geometry('600x300')
    a.configure(background='white')
    a.resizable(False, False)

    about_label = Label(a,
                        font=("Helvetica", 12),
                        bg='white',
                        fg="black",
                        text=ABOUT_MSG,
                        justify=CENTER)
    about_label.pack()
    about_footer_label = Label(a,
                               font=("Helvetica", 12),
                               bg='white',
                               fg="black",
                               text=ABOUT_FOOTER,
                               justify=CENTER)
    about_footer_label.pack()
