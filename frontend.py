from tkinter import *
from backend import Database

database=Database("books.db")

class Window(object):

    def __init__(self, window):

        window.wm_title("Book Store")

        l1=Label(window, text="Title")
        l1.grid(row=0, column=0)

        l2=Label(window, text="Author")
        l2.grid(row=0, column=2)

        l3=Label(window, text="Year")
        l3.grid(row=1, column=0)

        l4=Label(window, text="ISBN")
        l4.grid(row=1, column=2)

        self.text_title=StringVar()
        self.e1=Entry(window, textvariable=self.text_title)
        self.e1.grid(row=0, column=1)

        self.text_author=StringVar()
        self.e2=Entry(window, textvariable=self.text_author)
        self.e2.grid(row=0, column=3)

        self.text_year=StringVar()
        self.e3=Entry(window, textvariable=self.text_year)
        self.e3.grid(row=1, column=1)

        self.text_isbn=StringVar()
        self.e4=Entry(window, textvariable=self.text_isbn)
        self.e4.grid(row=1, column=3)

        self.lb=Listbox(window, height=15, width=27)
        self.lb.grid(row=2, column=0, rowspan=6, columnspan=2)

        sb=Scrollbar(window)
        sb.grid(row=2, column=2, rowspan=6)

        self.lb.config(yscrollcommand=sb.set)
        sb.config(command=self.lb.yview)

        self.lb.bind('<<ListboxSelect>>', self.selected_listbox)

        b1=Button(window, text="View All", width=18, command=self.command_view)
        b1.grid(row=2, column=3)

        b2=Button(window, text="Search Entry", width=18, command=self.command_search)
        b2.grid(row=3, column=3)

        b3=Button(window, text="Add Entry", width=18, command=self.command_add)
        b3.grid(row=4, column=3)

        b4=Button(window, text="Update", width=18, command=self.command_update)
        b4.grid(row=5, column=3)

        b5=Button(window, text="Delete", width=18, command=self.command_delete)
        b5.grid(row=6, column=3)

        b6=Button(window, text="Close", width=18, command=window.destroy)
        b6.grid(row=7, column=3)


    def selected_listbox(self, event):
        global selected_book
        try:
            index=self.lb.curselection()[0]
            selected_book=self.lb.get(index)
            self.e1.delete(0, END)
            self.e1.insert(END, selected_book[1])
            self.e2.delete(0, END)
            self.e2.insert(END, selected_book[2])
            self.e3.delete(0, END)
            self.e3.insert(END, selected_book[3])
            self.e4.delete(0, END)
            self.e4.insert(END, selected_book[4])
        except IndexError:
            pass

    def command_view(self):
        self.lb.delete(0, END)
        for rows in database.view():
            self.lb.insert(END, rows)

    def command_search(self):
        self.lb.delete(0, END)
        for rows in database.search(self.text_title.get(), self.text_author.get(), self.text_year.get(), self.text_isbn.get()):
            self.lb.insert(END, rows)

    def command_add(self):
        database.insert(self.text_title.get(), self.text_author.get(), self.text_year.get(), self.text_isbn.get())
        self.command_view()

    def command_update(self):
        database.update(selected_book[0], self.text_title.get(), self.text_author.get(), self.text_year.get(), self.text_isbn.get())
        self.command_view()

    def command_delete(self):
        database.delete(selected_book[0])
        self.command_view()

window=Tk()
Window(window)
window.mainloop()
