from tkinter import *
from tkinter import ttk, filedialog
from tkinter.scrolledtext import ScrolledText
import tkinter.messagebox as tm
import tkinter
import sqlite3
import datetime
from PIL import Image, ImageTk


class UserProgram():
    def __init__(self, user_name, width=450, height=650, title=None):
        self.root1 = Tk()
        self.root1.title(title)
        self.root1.geometry(f'{width}x{height}+100+100')

        # styliaus aprašymas
        ttk.Style().configure("TButton", font='helvetica 12', foreground="#004D40", relief="flat", background="#B2DFDB",
                              height=5)
        ttk.Style().configure("TCheckbutton", foreground="#004D40", relief="flat", background="#B2DFDB", height=5)
        ttk.Style().configure("TEntry", font='helvetica 12', foreground="#004D40", relief="flat", background="#B2DFDB",
                              height=5)
        ttk.Style().configure("TLabel", font='helvetica 12', foreground="#004D40", relief="flat", height=5)
        ttk.Style().configure("TFrame", font='helvetica 12', foreground="#004D40", relief="flat", height=5)
        ttk.Style().configure("TNotebook.Tab", font='helvetica 10', padding=(10, 5), foreground="#004D40", relief="flat", height=5)
        ttk.Style().configure("Vertical.TScrollbar", gripcount=0, background="#004D40", troughcolor="#B2DFDB")

        # vartotojo vardo perkėlimas į klasę
        self.user_name = user_name
        # Aprašomi TAB lango įdėklų lapeliai
        self.tab_control = ttk.Notebook(self.root1)
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab1, text=('Informacija'))
        self.tab2 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab2, text=('Rašyti žinutę'))
        self.tab3 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab3, text=('Skaityti žinutes'))


        self.frame_menu = Frame(self.tab2, width=400, height=20)
        self.frame_result = Frame(self.tab2,  width=400, height=300)
        self.filename = ''

        image = Image.open("off.png")
        self.photo = ImageTk.PhotoImage(image)

        self.label_name = ttk.Label(self.frame_result, width=15, justify=LEFT, text='Username:', foreground="#004D40",font=('helvetica', 12))
        self.label_name_from_db = ttk.Label(self.frame_result, width=30, justify=LEFT, text=self.user_name, foreground="#004D40",font=('helvetica', 12))
        self.label_message = ttk.Label(self.frame_result, width=15, justify=LEFT, text='Your message: ', foreground="#004D40",font=('helvetica', 12))
        self.label_atach = ttk.Label(self.frame_result, width=30, justify=LEFT, text='', foreground="#004D40",font=('helvetica', 12))
        self.entry_message = ScrolledText(self.frame_result, width=30, height=10, bg='white',foreground="#004D40",font=('helvetica', 12))

        self.button_atachfile = ttk.Button(self.frame_result, text='Atach file:',  command=self.atach_files)
        self.button_send = ttk.Button(self.frame_result, text='Send', command=self.user_mess)

        self.frame_list = ttk.Frame(self.tab3, width=50, height=550)
        self.frame_list_result = ttk.Frame(self.tab3, width=400, height=450)
        self.frame_list.grid(row=0, column=0, sticky=NW)
        self.frame_list_result.grid(row=0, column=1, sticky=NW)

        self.conn = sqlite3.connect('users_and_messages.db')
        self.cursor = self.conn.cursor()

        self.zinutes_listbox = Listbox(self.frame_list, selectmode=SINGLE, width=17,foreground="#004D40",font=('helvetica', 10))
        self.zinutes_listbox.pack(padx=20, pady=45, side=TOP,)
        self.zinutes_listbox.bind("<<ListboxSelect>>", self.rodyti_zinute)

        self.rodyti_zinutes()


    def rodyti_zinutes(self):

        self.variable_id = self.cursor.execute("SELECT id FROM users WHERE User_name=?", (self.user_name,)).fetchone()
        # Išgauname žinutes iš duomenų bazės ir pridedame jas į listbox
        self.zinutes_listbox.delete(0, END)
        self.cursor.execute(f"""SELECT "Data of message" FROM message WHERE user_id=={self.variable_id[0]}""")
        zinutes = self.cursor.fetchall()
        for zinute in zinutes:
            print(zinute)
            self.zinutes_listbox.insert(END, zinute[0][0:19])


    def rodyti_zinute(self, event):
        # Atvaizduojame pasirinktą žinutę dešinėje pusėje

        selected_index = self.zinutes_listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            self.cursor.execute(f"""SELECT "Data of message", Message, "Status of message", "Message comments" FROM message WHERE user_id=={self.variable_id[0]}""")
            zinutes = self.cursor.fetchall()
            data_laikas, tekstas, statusas, komentaras = zinutes[selected_index]
            self.atvaizduoti_zinute(data_laikas, tekstas, statusas, komentaras)

    def spalva(self):
        self.label_statusas = self.statusai.cget("text")
        if self.label_statusas =='Išsiusta':
            print('aaa')
            self.statusai.configure(background='#FFFFE0')
        elif self.label_statusas =='Priimta':
            self.statusai.configure(background='#90EE90')
        elif self.label_statusas =='Atmesta':
            self.statusai.configure(background='#FF8A8A')
    def atvaizduoti_zinute(self, data_laikas, tekstas, statusas, komentaras):
        self.clear_dekstra()
        dekstra_frame = ttk.Frame(self.frame_list_result)
        dekstra_frame.pack(padx=20, pady=20, side=RIGHT)

        ttk.Label(dekstra_frame, text=f"Data ir laikas:").pack(pady=3)
        ttk.Label(dekstra_frame, background='white', text=f"{data_laikas[0:19]}").pack()
        ttk.Label(dekstra_frame, text=f"Žinutė:").pack(pady=5)
        self.message = ScrolledText(dekstra_frame, width=30, height=5, bg='white', wrap=WORD)
        self.message.insert(INSERT, tekstas)
        self.message.pack(pady=5)
        ttk.Label(dekstra_frame, text=f"žinutės statusas:").pack(pady=3)
        self.statusai = (ttk.Label(dekstra_frame, background='white', text=f"{statusas}"))
        self.spalva()
        self.statusai.pack(pady=5)
        ttk.Label(dekstra_frame, text=f"Komentaras:").pack(pady=3)
        self.message1 = ScrolledText(dekstra_frame, width=30, height=5, bg='white', wrap=WORD)
        self.message1.insert(INSERT, komentaras)
        self.message1.pack(pady=5)

        back_button = ttk.Button(dekstra_frame, text="Atgal", command=self.clear_dekstra)
        back_button.pack(pady=10)

        self.current_dekstra_frame = dekstra_frame


    def clear_dekstra(self):
        if hasattr(self, 'current_dekstra_frame'):
            self.current_dekstra_frame.destroy()


    def atach_files(self):
        self.filename = filedialog.askopenfilename()
        self.label_atach.configure(text=self.filename)
        return self.filename
    def write_messages(self):
        self.frame_menu.grid(row=0, column=0)
        self.frame_result.grid(row=1, column=0)
        self.label_name.grid(row=0, column=0, sticky=W, pady=5)
        self.label_name_from_db.grid(row=0, column=1, sticky=W, pady=5)
        self.label_message.grid(row=1, column=0, sticky=NW, pady=5)
        self.entry_message.grid(row=1, column=1, sticky=W, pady=5)
        self.button_atachfile.grid(row=2, column=0, sticky=N, pady=5)
        self.label_atach.grid(row=2, column=1, sticky=W, pady=5)
        self.button_send.grid(row=3, column=1, sticky=W, pady=5)


    def user_mess(self):
        if self.filename != '':
            with open(self.filename, mode='rb') as file:
                self.blobData =sqlite3.Binary(file.read())
        else: self.blobData = "NULL"

        message = self.entry_message.get("1.0", tkinter.END)
        data = datetime.datetime.now()
        dataname = sqlite3.connect('users_and_messages.db')
        variable = dataname.cursor()
        with dataname:
            self.variable_id = variable.execute("SELECT id FROM users WHERE User_name=?", (self.user_name,)).fetchone()

        with dataname:
            print(self.variable_id[0])
            variable.execute("INSERT INTO message (user_id, Message, 'Atached file', 'Data of message', 'Theme of message', 'Title of message', 'Status of message', 'Message comments') VALUES(?,?,?,?,?,?,?,?)", (int(self.variable_id[0]), f'{message}',  self.blobData, f'{data}','None', 'None', "Išsiusta",'None'))
        dataname.commit()
        dataname.close()
        tm.showinfo("Message", f"Your message is send")

    def RFunction(self):
        self.drwidgets()
        self.write_messages()
        self.root1.mainloop()

    def drwidgets(self):
        ttk.Button(image=self.photo, command=lambda: self.root1.quit()).place(x=400, y=590)
        self.tab_control.pack(expand=1, fill=BOTH, pady=5)

if __name__ == '__main__':
    UP_window = UserProgram(user_name='Emilis')
    UP_window.RFunction()