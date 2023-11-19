from tkinter import *
from tkinter.ttk import *
from sqlalchemy import *
from sqlalchemy.orm import *
from darbui import Users
from tkinter.scrolledtext import ScrolledText

engine = create_engine('sqlite:///language.db', echo=True)
Base = declarative_base()
metadata = MetaData()
Session = sessionmaker(bind=engine)
session = Session()

class Read_rules():
    def __init__(self, width=300, height=400, title = None, resizable = (True, True)):
        self.root = Tk() #sasaja su pagrindiniu
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+100+100")
        self.root.resizable(resizable[0], resizable[1])
        self.lang_frame = Frame(self.root)
        self.languages=['lietuvių', 'English', "Русский", 'Français']
        self.languages_var = StringVar()
        self.combobox = Combobox(self.lang_frame, textvariable=self.languages_var, values=self.languages, state='readonly')
        self.list = ScrolledText(self.lang_frame, width=40, height=20, bg='white', wrap=WORD)
        self.buton = Button(self.lang_frame, text=f'text', state=DISABLED, command=self.root.destroy)

    # def language_for_user(self):
    #
    #     engine1 = create_engine('sqlite:///users_and_messages.db', echo=True)
    #     Session = sessionmaker(bind=engine1)
    #     session = Session()
    #     for i in session.query(users).filter_by(user=self.selection).all():
    #
    #     session.commit()
    #     session.close()
    def drawwidgets(self):

        self.lang_frame.pack()
        self.combobox.pack()
        self.root.bind("<<ComboboxSelected>>", self.selected)
        self.list.pack()
        self.buton.pack()



    def selected(self, event):
        self.list.delete(1.0, END)
        self.selection = self.combobox.get()
        for i in session.query(Users).filter_by(lang=self.selection).all():

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
        self.root.wait_window()  #uzlaiko langus

    def RunFunction(self):
        self.drawwidgets()
        self.focus()

        self.root.mainloop()



if __name__ == '__main__':

    window = Read_rules(title='Social centre')
    window.RunFunction()

Base.metadata.create_all(engine)