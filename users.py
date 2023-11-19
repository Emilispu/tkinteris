from tkinter import *
from tkinter import ttk
from sqlalchemy import *
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
from sqlite3 import *

from db_classes import Check_user_connection, Users
from tkinter_clases import UserProgram

# from languages import Read_rules
from darbui import Languages_all
from tkinter.ttk import Combobox
from tkinter.scrolledtext import ScrolledText

engine = create_engine('sqlite:///language.db', echo=True)
Base = declarative_base()
metadata = MetaData()
Session = sessionmaker(bind=engine)
session = Session()


class WindowClass():

    def __init__(self, width=450, height=650, title=None, resizible=[False, False]):
        self.root = Tk()
        ttk.Style().configure("TButton", font='helvetica 12', foreground="#004D40", relief="flat", background="#B2DFDB",
                              height=5)
        ttk.Style().configure("TCheckbutton", foreground="#004D40", relief="flat", background="#B2DFDB", height=5)
        ttk.Style().configure("TEntry", font='helvetica 12', foreground="#004D40", relief="flat", background="#B2DFDB",
                              height=5)
        ttk.Style().configure("TLabel", font='helvetica 12', foreground="#004D40", relief="flat", height=5)

        self.root.title(title)
        self.resizible = (resizible[0], resizible[0])
        self.root.geometry(f"{width}x{height}+100+100")
        self.frame = ttk.Frame(self.root, width=400, height=450)
        self.frame1 = ttk.Frame(self.root, width=400, height=450)

        # User connection frame
        self.remember_me = ttk.Checkbutton(self.frame, )
        self.text_name = ttk.Label(self.frame, text='User name')
        self.text_passw = ttk.Label(self.frame, text='User password')
        self.entry_name = ttk.Entry(self.frame, width=30)
        self.entry_passw = ttk.Entry(self.frame, show="*", width=30)
        self.button_connect = ttk.Button(self.frame, text='Connect', state='disabled', command=self._login)

    def _login(self):
        engine = create_engine('sqlite:///users_and_messages.db', echo=True)
        Base = declarative_base()
        metadata = MetaData()

        Session = sessionmaker(bind=engine)
        session = Session()
        self.vardas = self.entry_name.get()
        self.result = Check_user_connection(self.vardas, self.entry_passw.get())
        print(self.vardas, )
        if self.result.check_connection():
            self.root.destroy()
            if self.result.user_status() == True:
                self.result.user_status2()

                # Read_rules.language_for_user(self)
                if __name__ == '__main__':
                    windowsmall = Read_rules(names=self.vardas)
                    windowsmall.RunFunction()
            if __name__ == '__main__':
                UP_window = UserProgram(user_name=self.vardas)
                UP_window.RFunction()



        return self.entry_name

    def runWidgets(self):
        self.frame.pack(anchor='center', pady=150)
        self.text_name.pack(pady=1)
        self.entry_name.pack(pady=1)
        self.entry_name.bind("<KeyRelease>", self.enabled)
        self.text_passw.pack(pady=1)
        self.entry_passw.pack(pady=5)
        self.entry_passw.bind("<KeyRelease>", self.enabled)
        self.button_connect.pack(pady=10)

    # Make connect button enable
    def enabled(self, event):
        a = len(self.entry_name.get())
        b = len(self.entry_passw.get())
        if a != 0 and b != 0:
            self.button_connect['state'] = 'normal'
            self.button_connect.update()

    def RunFunction(self):

        self.runWidgets()
        self.root.mainloop()


class Read_rules():
    def __init__(self, names, width=300, height=400, title=None, resizable=(True, True)):
        self.root = Tk()  # sasaja su pagrindiniu
        self.root.title(title)
        self.names = names
        self.root.geometry(f"{width}x{height}+100+100")
        self.root.resizable(resizable[0], resizable[1])
        self.lang_frame = Frame(self.root)
        self.languages = ['lietuvių', 'English', "Русский", 'Français']
        self.languages_var = StringVar()
        self.combobox = Combobox(self.lang_frame, textvariable=self.languages_var, values=self.languages,
                                 state='readonly')
        self.list = ScrolledText(self.lang_frame, width=40, height=20, bg='white', wrap=WORD)
        self.buton = Button(self.lang_frame, text=f'text', state=DISABLED, command=self.save_lang)

    def save_lang(self):
        engine1 = create_engine('sqlite:///users_and_messages.db', echo=True)
        Session1 = sessionmaker(bind=engine1)
        session1 = Session1()

        print(self.names, self.selection)
        for u in session1.query(Users).filter_by(user=self.names).all():
            u.language = self.selection

        session1.commit()
        self.root.destroy()

    def drawwidgets(self):
        self.lang_frame.pack()
        self.combobox.pack()
        self.root.bind("<<ComboboxSelected>>", self.selected)
        self.list.pack()
        self.buton.pack()

    def selected(self, event):
        self.list.delete(1.0, END)
        self.selection = self.combobox.get()
        for i in session.query(Languages_all).filter_by(lang=self.selection).all():
            self.list.insert(INSERT, i.text)
            self.buton['text'] = i.agree
        self.scrolled
        self.check_scroll
        self.root.after(100, self.check_scroll)

    def scrolled(self):
        self.list.yview_scroll(1, 'units')
        if float(self.list.yview()[1]) == 1.0:
            self.buton['state'] == NORMAL
        else:
            self.root.after(100, self.scrolled)

    def check_scroll(self):
        if float(self.list.yview()[1]) == 1.0:
            print("Finished scrolling to the end")
            self.buton['state'] = NORMAL
            self.buton.bind()
        else:
            self.root.after(100, self.check_scroll)

    def focus(self):

        self.root.grab_set()  # perima komandu vykdyma
        self.root.focus_set()  # uzdraudzia uzdaryti pagrindini
        self.root.wait_window()  # uzlaiko langus

    def RunFunction(self):
        self.drawwidgets()
        self.focus()
        self.root.mainloop()


if __name__ == '__main__':
    window = WindowClass(title='Social centre')
    window.RunFunction()
