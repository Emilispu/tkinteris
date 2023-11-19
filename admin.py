from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import tkinter.messagebox as tm
import sqlite3
from googletrans import Translator, LANGUAGES
import datetime
from PIL import Image, ImageTk


class Admin_Login_Class():
    def __init__(self, width, heigth, title=None, resizable = [False, False]):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f'{width}x{heigth}+200+200')
        self.root.resizable(resizable[0], resizable[1])

        ttk.Style().configure("TButton", font='helvetica 10', foreground="#004D40", relief="flat", background="#B2DFDB",
                              height=5)
        ttk.Style().configure("TCheckbutton", foreground="#004D40", relief="flat", background="#B2DFDB", height=5)
        ttk.Style().configure("TEntry", font='helvetica 12', foreground="#004D40", relief="flat", background="#B2DFDB",
                              height=5)
        ttk.Style().configure("TLabel", font='helvetica 12', foreground="#004D40", relief="flat", height=5)
        ttk.Style().configure("TFrame", font='helvetica 12', foreground="#004D40", relief="flat", height=5)
        ttk.Style().configure("TNotebook.Tab", font='helvetica 10', padding=(10, 5), foreground="#004D40",
                              relief="flat", height=5)
        ttk.Style().configure("Vertical.TScrollbar", gripcount=0, background="#004D40", troughcolor="#B2DFDB")


        self.label=ttk.Label(text='Please fill User connect information:\n ', font=('Arial', 12),anchor=CENTER)
        self.label_user_name = ttk.Label(text='User name: ', font=('helvetica', 10), anchor=CENTER)
        self.label_user_password = ttk.Label(text='Password: ', font=('helvetica', 10), anchor=CENTER)
        self.button = ttk.Button(text = 'Connect',   command=self._login )
        self.entry_user_name = ttk.Entry()
        self.entry_user_password = ttk.Entry(show="*")
        self.entry_user_password.bind("return", self._login)

    def RunFunction(self):
        # self.draw_widgets()
        self._login()
        self.root.mainloop()

    def draw_widgets(self):
        self.label.pack()
        self.label_user_name.pack()
        self.entry_user_name.pack()
        self.label_user_password.pack()
        self.entry_user_password.pack()
        self.button.pack(pady=5)

    def _login(self):
        # username = self.entry_user_name.get()
        # userpassword = self.entry_user_password.get()
        username = 'admin'
        userpassword = 'a'
        dataname = sqlite3.connect('users_and_messages.db')
        variables = dataname.cursor()
        with dataname:
            for el, el1 in variables.execute(f"SELECT admin_name, admin_pass FROM admin WHERE admin_name=='{username}'"):
                i = el
                j = el1
        if (username, userpassword)==(i, j):
            # tm.showinfo("Login info", f"Welcome, {username}")
            self.root.destroy()
            wind = Admin_app()
            wind.RunFunction()

        else:
            tm.showerror("Login error", "Connect information arent correct, please try again")


class Admin_app():
    def __init__(self,  width=850, heigth=600, title=None, resizable = [False, False]):
        self.root1 = Tk()
        self.root1.geometry(f'{width}x{heigth}+100+100')
        self.root1.resizable(resizable[1], resizable[1])

        ttk.Style().configure("TButton", font='helvetica 10', foreground="#004D40", relief="flat", background="#B2DFDB",
                              height=5)
        ttk.Style().configure("TCheckbutton", foreground="#004D40", relief="flat", background="#B2DFDB", height=5)
        ttk.Style().configure("TEntry", font='helvetica 12', foreground="#004D40", relief="flat", background="#B2DFDB",
                              height=5)
        ttk.Style().configure("TLabel", font='helvetica 12', foreground="#004D40", relief="flat", height=5)
        ttk.Style().configure("TFrame", font='helvetica 12', foreground="#004D40", relief="flat", height=5)
        ttk.Style().configure("TNotebook.Tab", font='helvetica 10', padding=(10, 5), foreground="#004D40",
                              relief="flat", height=5)
        ttk.Style().configure("Vertical.TScrollbar", gripcount=0, background="#004D40", troughcolor="#B2DFDB")

        self.tab_control = ttk.Notebook(self.root1, width=800, height=550)
        self.tab1 = ttk.Frame(self.tab_control, width=800, height=550)
        self.tab_control.add(self.tab1, text=('Nustatymai'))
        self.tab2 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab2, text=('Valdyti vartotojus'))
        self.tab3 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab3, text=('Rašyti žinutę'))
        self.tab4 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab4, text=('Skaityti žinutes'))


    def draw_widgets(self):
        self.tab_control.pack(fill=BOTH)
        MessageApp(root2=self.tab4)
        Users_settings(root3=self.tab2)
    def RunFunction(self):
        self.draw_widgets()
        self.root1.mainloop()

class Users_settings():
    def __init__(self, root3):
        self.root3 = root3



        ttk.Style().configure("TButton", font='helvetica 10', foreground="#004D40", relief="flat", background="#B2DFDB",
                              height=5)
        ttk.Style().configure("TCheckbutton", foreground="#004D40", relief="flat", background="#B2DFDB", height=5)
        ttk.Style().configure("TEntry", font='helvetica 12', foreground="#004D40", relief="flat", background="#B2DFDB",
                              height=5)
        ttk.Style().configure("TLabel", font='helvetica 12', foreground="#004D40", relief="flat", height=5)
        ttk.Style().configure("TFrame", font='helvetica 12', foreground="#004D40", relief="flat", height=5)
        ttk.Style().configure("TNotebook.Tab", font='helvetica 10', padding=(10, 5), foreground="#004D40",
                              relief="flat", height=5)
        ttk.Style().configure("Vertical.TScrollbar", gripcount=0, background="#004D40", troughcolor="#B2DFDB")

        self.default_text = "rašyti"

        self.entry = ttk.Entry(self.root3)
        self.dataname = sqlite3.connect("users_and_messages.db")
        self.variables = self.dataname.cursor()

        self.users = []
        for el in self.variables.execute("SELECT User_name FROM users").fetchall():
            self.users.append(el[0])

        self.listbox = Listbox(self.root3)
        for item in self.users:
            self.listbox.insert(END, item)

        self.entry_label = ttk.Label(self.root3, text="Įveskite")

        self.entry_label.pack()
        self.entry.pack()
        self.listbox.pack()
        self.entry.bind("<FocusIn>", self.clear_default_text)
        self.entry.bind("<FocusOut>", self.restore_default_text)
        self.entry.bind("<KeyRelease>", self.filter_by_name)
        self.root3.mainloop()

    def clear_default_text(self, event):
        if self.entry.get() == self.default_text:
            self.entry.delete(0, END)
            self.entry.config(fg="black")  # Pakeičiame teksto spalvą į juodą

    def restore_default_text(self, event):
        if not self.entry.get():
            self.entry.insert(0, self.default_text)
            self.entry.config(fg="gray")  # Pakeičiame teksto spalvą į pilką

    def filter_by_name(self, event=None):
        self.name_text = self.entry.get()
        self.filtered_name = [item for item in self.users if item.startswith(self.name_text)]
        self.listbox.delete(0, END)
        for item in self.filtered_name:
            self.listbox.insert(END, item)


    # def RunFunction(self):
    #     self.entry.bind("<FocusIn>", self.clear_default_text)
    #     self.entry.bind("<FocusOut>", self.restore_default_text)
    #     self.entry.bind("<KeyRelease>", self.filter_by_name)
    #     self.root3.mainloop()

class MessageApp:
    def __init__(self, root2):
        self.root2 = root2
        self.combo_var = StringVar()
        style = ttk.Style()

        style.configure("Treeview", font=("Helvetica", 10), foreground="#004D40")
        style.configure("Treeview.Heading", font=("Helvetica", 11), foreground="#004D40")
        style.configure("TLabel", font=("Helvetica", 10), foreground="#004D40")
        style.configure("TFrame", font=("Helvetica", 10), foreground="#004D40")
        self.tree = ttk.Treeview(self.root2, columns=("id", "Sender", "Date", "Message Preview", "Status", "Comments"), height=550, show="headings")
        self.tree.heading("id", text="Nr.", command=lambda: self.sort_column("id", False))
        self.tree.heading("Sender", text="Siuntėjas", command=lambda: self.sort_column("Sender", False))
        self.tree.heading("Date", text="Siuntimo laikas", command=lambda: self.sort_column("Date", False))
        self.tree.heading("Message Preview", text="Žinutės peržiūra", command=lambda: self.sort_column("Message Preview", False))
        self.tree.heading("Status", text="Statusas", command=lambda: self.sort_column("Status", False))
        self.tree.heading("Comments", text="Komentaras", command=lambda: self.sort_column("Comments", False))

        self.tree.column("id", width=40)
        self.tree.column("Sender", width=70)
        self.tree.column("Date", width=170)
        self.tree.column("Message Preview", width=200)
        self.tree.column("Status", width=100)
        self.tree.column("Comments", width=200)

        self.tree.pack(padx=20, pady=20, anchor='n', expand=True)
        self.tree.bind("<Double-1>", self.show_full_message)

        # Prisijungti prie SQLite duomenų bazės
        self.conn = sqlite3.connect('users_and_messages.db')
        self.cursor = self.conn.cursor()

        # Išgauti žinutes iš duomenų bazės
        self.get_messages()

        # Default sorting column and order
        self.sort_column("id", False)

    def get_messages(self):
        self.cursor.execute("""SELECT id, user_id, "Data of message", Message, "Status of message", "Message comments" FROM message """)
        messages = self.cursor.fetchall()
        for message in messages:
            id, sender, date, full_message, stat, comm = message
            user_name = self.cursor.execute(f"SELECT User_name FROM users WHERE id == {sender}").fetchone()[0]
            message_preview = full_message[:20] if len(full_message) > 20 else full_message
            date_time = date[:19] if len(date) > 19 else date
            self.tree.insert("", "end", values=(id, user_name, date_time, message_preview, stat, comm))

    def show_full_message(self, event):
        selected_item = self.tree.selection()
        message_window = Toplevel(self.root2)
        message_window.title("Pilna Žinutė")

        ttk.Label(message_window, text='Pilna zinute:').grid(row=0, column=0, columnspan=2, pady=5)

        if selected_item:
            self.id = self.tree.item(selected_item, "values")[0]
            self.full_message = self.cursor.execute(
                f"""SELECT user_id, Message, "Atached file", "Data of message", "Status of message", "Message comments" FROM message WHERE id == {self.id}""").fetchone()
            vartotojas = self.cursor.execute(f"SELECT User_name FROM users WHERE id={self.full_message[0]}").fetchone()[0]

            ttk.Label(message_window, text='Vartotojas', width=20, font=("Helvetica, 12")).grid(row=1, column=0,
                                                                                                       pady=5)
            ttk.Label(message_window, text=f'{vartotojas}', width=20, anchor="w", borderwidth=2,
                      background="white").grid(row=1, column=1, pady=5)

            ttk.Label(message_window, text='Data ir laikas:', width=20, font=("Helvetica, 12"), background=None).grid(row=2,column=0, pady=5)
            ttk.Label(message_window, text=f'{self.full_message[3][:19]}', width=20, anchor="w", borderwidth=2,
                      background="white").grid(row=2, column=1, pady=5)

            ttk.Label(message_window, text='Žinutė:', font=("Helvetica, 12"), background=None).grid(row=3, column=0, sticky= 'w',  padx=20, pady=5)
            self.messscroll = ScrolledText(message_window, width=40, height=5, bg='white', wrap=WORD)
            self.messscroll.insert(INSERT, self.full_message[1])
            self.messscroll.grid(row=4, rowspan = 2, column=0, padx=20, pady=10)

            translator = TextTranslator(text=self.full_message[1])
            translation_result = translator.translate_to_lithuanian()
            ttk.Label(message_window, text=f'Vertimas į kalbą: {translation_result[0]}', font=("Helvetica, 12"),
                      background=None).grid(row=3, column=1, pady=5)
            self.messscroll = ScrolledText(message_window, width=40, height=5, bg='white', wrap=WORD)
            self.messscroll.insert(INSERT, translation_result[1])
            self.messscroll.grid(row=4, column=1, columnspan=2, padx=20, pady=10)
            ttk.Label(message_window, text='Statusas:', width=20, font=("Helvetica, 12"), background=None).grid(row=5,column=0, pady=5)
            self.combo = ttk.Combobox(message_window, textvariable=self.combo_var, values=("Priimta", "Išsiųsta", "Atmesta"), state="readonly")
            self.combo.set(self.full_message[4])
            self.combo.grid(row=5,column=1, pady=5)
            ttk.Button(message_window, text='Įrašyti pakeitimus', command=self.insert_data).grid(row=7, column=0)
    def insert_data(self):
        statusas1 = self.combo.get()
        print(statusas1, self.id)
        self.cursor.execute(f"""UPDATE message SET "Status of message" = ? WHERE id==?""", (statusas1, self.id))
        self.conn.commit()

    def on_combobox_select(self, event):
        self.selected_value = self.combo_var.get()
        self.full_message [4] =self.selected_value

    def sort_column(self, col, reverse):
        data = [(self.tree.set(item, col), item) for item in self.tree.get_children('')]
        data.sort(reverse=reverse)
        for index, (val, item) in enumerate(data):
            self.tree.move(item, '', index)
        self.tree.heading(col, command=lambda: self.sort_column(col, not reverse))

    def RunFunction(self):
        self.combo.bind("<<ComboboxSelected>>", self.on_combobox_select)
        self.root2.mainloop()
class TextTranslator:
    def __init__(self, text):
        self.translator = Translator()
        self.text = text

    def translate_to_lithuanian(self):
        try:
            result = self.translator.detect(self.text)
            detected_lang = result.lang
            if detected_lang == 'lt':
                return f'Tekstas jau lietuvių kalba: {self.text}'
            elif detected_lang == 'und':
                return 'Kalba nenustatyta'
            else:
                translation = self.translator.translate(self.text, src=detected_lang, dest='lt')
                return LANGUAGES[detected_lang].capitalize(), translation.text
        except Exception as e:
            return f'Klaida vertimui: {str(e)}'

if __name__ == '__main__':
    window = Admin_Login_Class(300, 200, 'Foreign registracion centre')
    window.RunFunction()


