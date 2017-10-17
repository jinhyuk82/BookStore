from tkinter import *
import backend

def selected_listbox(event):
    global selected_book
    try:
        index=lb.curselection()[0]
        selected_book=lb.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_book[1])
        e2.delete(0, END)
        e2.insert(END, selected_book[2])
        e3.delete(0, END)
        e3.insert(END, selected_book[3])
        e4.delete(0, END)
        e4.insert(END, selected_book[4])
    except IndexError:
        pass

def command_view():
    lb.delete(0, END)
    for rows in backend.view():
        lb.insert(END, rows)

def command_search():
    lb.delete(0, END)
    for rows in backend.search(text_title.get(), text_author.get(), text_year.get(), text_isbn.get()):
        lb.insert(END, rows)

def command_add():
    backend.insert(text_title.get(), text_author.get(), text_year.get(), text_isbn.get())
    command_view()

def command_update():
    backend.update(selected_book[0], text_title.get(), text_author.get(), text_year.get(), text_isbn.get())
    command_view()

def command_delete():
    backend.delete(selected_book[0])
    command_view()

window=Tk()

window.wm_title("Book Store")

l1=Label(window, text="Title")
l1.grid(row=0, column=0)

l2=Label(window, text="Author")
l2.grid(row=0, column=2)

l3=Label(window, text="Year")
l3.grid(row=1, column=0)

l4=Label(window, text="ISBN")
l4.grid(row=1, column=2)

text_title=StringVar()
e1=Entry(window, textvariable=text_title)
e1.grid(row=0, column=1)

text_author=StringVar()
e2=Entry(window, textvariable=text_author)
e2.grid(row=0, column=3)

text_year=StringVar()
e3=Entry(window, textvariable=text_year)
e3.grid(row=1, column=1)

text_isbn=StringVar()
e4=Entry(window, textvariable=text_isbn)
e4.grid(row=1, column=3)

sb=Scrollbar(window)
sb.grid(row=2, column=2, rowspan=6)

lb=Listbox(window, height=15, width=27, yscrollcommand=sb.set)
lb.grid(row=2, column=0, rowspan=6, columnspan=2)
lb.bind('<<ListboxSelect>>', selected_listbox)

#lb.configure(yscrollcommand=sb.set)
sb.config(command=lb.yview)

b1=Button(window, text="View All", width=18, command=command_view)
b1.grid(row=2, column=3)

b2=Button(window, text="Search Entry", width=18, command=command_search)
b2.grid(row=3, column=3)

b3=Button(window, text="Add Entry", width=18, command=command_add)
b3.grid(row=4, column=3)

b4=Button(window, text="Update", width=18, command=command_update)
b4.grid(row=5, column=3)

b5=Button(window, text="Delete", width=18, command=command_delete)
b5.grid(row=6, column=3)

b6=Button(window, text="Close", width=18, command=window.destroy)
b6.grid(row=7, column=3)

command_view()

window.mainloop()
