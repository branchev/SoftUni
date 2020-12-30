# in ttk lib and tkinter there is a classes which are called by same name as each other. The version of the ttk is
# higher and the import from ttk must be on the top to prevent clashes

from tkinter.ttk import *
from tkinter import *
from tkcalendar import DateEntry
from tkinter.scrolledtext import *
import json

all_tasks_to_write = []


def clear_view(tk):
    # below is forloop which cleans the main buttons (main view) of the app and with the
    # algorithm below creates the new interface of the window for the task form
    for s in tk.grid_slaves():
        s.destroy()


def edit_task(tk):
    clear_view(tk)


# the parameter *args unpacks the given arguments as tuple,
# # the count of expected arguments is not important - it unpacks as tuple everything
# def new_task(*args):
#     print(args)


# kwargs unpacks the arguments as named key-value pairs in dictionary
def new_task(**kwargs):
    all_tasks_to_write.append(kwargs)


# this is a render of the page when you click create task button
def create_task(tk):
    clear_view(tk)
    Label(tk, text="Enter your task name:").grid(row=0, column=0, padx=20, pady=20)
    # the gridding does not returns any value - if the object of the class Entry is gridded on the same line as it is
    # created it will return None and we can't use any method to store or get the information by the entry row in app
    # The solution is to create the object of the class Entry and store it to a variable on the first line and
    # grid it on the second line
    task_name = Entry(tk)
    task_name.grid(row=0, column=1)
    Label(tk, text="Due date: ").grid(row=1, column=0, padx=20, pady=20)
    date = DateEntry(tk)
    date.grid(row=1, column=1)
    Label(tk, text="Description:").grid(row=2, column=0, padx=20, pady=20)
    description = ScrolledText(tk, width=20, height=20)
    description.grid(row=2, column=1)
    Label(tk, text="Priority:").grid(row=3, column=0, padx=20)
    # IntVar is used in GUI - it holds integers, the default value is 0. Also there is StrVar, BoolVar etc
    # radiobuttons refers to the IntVar and changes its value by the chosen option
    selected_priority = IntVar()
    Radiobutton(tk, text='Low', value=1, variable=selected_priority).grid(row=3, column=1)
    Radiobutton(tk, text='Medium', value=2, variable=selected_priority).grid(row=4, column=1)
    Radiobutton(tk, text='High', value=3, variable=selected_priority).grid(row=5, column=1)
    Label(tk, text="Done?").grid(row=6, column=0, padx=20, pady=20)
    is_completed = BooleanVar()
    Checkbutton(tk, text="Check", variable=is_completed).grid(row=6, column=1)
    # the description must be a multiline string that's why below it is defined that it will contains all the characters
    # from the first char to the end - (1.0 - END)
    # lambda is used for referring to a function with given arguments - to call the function by "on click action"
    # if there is not a lambda, we can refer without brackets (), but the function needs arguments to be useful
    Button(
        tk, text="Create task", bg="yellow", fg="red",
        command=lambda: new_task(
            name=task_name.get(),
            date=date.get(),
            description=description.get("1.0", END),
            priority=selected_priority.get(),
            is_completed=is_completed.get()
        )
    ).grid(row=7, column=0, padx=20, pady=20)


def main_view(tk):
    Button(
        tk,
        text="List Tasks", bg="yellow", fg="red",
        command=lambda: edit_task(tk)
    ).grid(row=0, column=0, padx=20, pady=20)

    Button(
        tk,
        text="New Task", bg="yellow", fg="red",
        command=lambda: create_task(tk)
    ).grid(row=0, column=1, padx=20, pady=20)


tk = Tk()
tk.geometry("400x700")

main_view(tk)
tk.mainloop()

# r+ is read and write mode:
with open("db.txt", "r+") as file:
    try:
        existing_tasks = json.load(file)
    except json.decoder.JSONDecodeError:
        existing_tasks = []
    # the seek function means to put the cursor at the chosen point
    file.seek(0)
    # truncate cleans all the contain from the file
    file.truncate()
    all_tasks_to_write.extend(existing_tasks)
    # dump method puts lists, dicts etc. to the database file without parsing it to string.
    json.dump(all_tasks_to_write, file)
