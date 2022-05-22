import tkinter as tk
from tkinter import messagebox
import json
from Manager.InstantiateGraphObject import InstantiateGraphicalObject
from ApiOperations.ApiWhisper import ApiWhisper
from DefensiveCode import Defender
from DrawMainInterface import DrawPharmaMan


class DrawObj:
    def __init__(self):
        super(DrawObj, self).__init__()
        """Istanzio gli oggetti della UI"""

        # Window
        midnight_blue: str = '#151B54'
        solarized_blue: str = '#9bb5de'
        solarized_orange: str = '#6682ff'
        self.window = tk.Tk()
        self.window.geometry('500x500')
        self.window['background'] = midnight_blue
        self.window.title('CSET Login')

        # Label
        self.label_fiscal_code = tk.Label(self.window,
                                          text='Codice fiscale',
                                          fg=solarized_blue,
                                          bg=midnight_blue,
                                          font=('Courier', 16, 'bold'))

        self.label_login_fiscal_code = tk.Label(self.window,
                                                text='Codice fiscale',
                                                fg=solarized_blue,
                                                bg=midnight_blue,
                                                font=('Courier', 16, 'bold'))

        self.label_login_password = tk.Label(self.window,
                                             text='Password',
                                             fg=solarized_blue,
                                             bg=midnight_blue,
                                             font=('Courier', 16, 'bold'))

        self.label_name = tk.Label(self.window,
                                   text='Nome',
                                   fg=solarized_blue,
                                   bg=midnight_blue,
                                   font=('Courier', 16, 'bold'))

        self.label_surname = tk.Label(self.window,
                                      text='Cognome',
                                      fg=solarized_blue,
                                      bg=midnight_blue,
                                      font=('Courier', 16, 'bold'))

        self.label_password = tk.Label(self.window,
                                       text='Password',
                                       fg=solarized_blue,
                                       bg=midnight_blue,
                                       font=('Courier', 16, 'bold'))

        self.label_med_or_pharma = tk.Label(self.window,
                                            text='Medico o Farmacologo?',
                                            fg=solarized_blue,
                                            bg=midnight_blue,
                                            font=('Courier', 16, 'bold'))

        self.label_re_password = tk.Label(self.window,
                                          text='Re-Password',
                                          fg=solarized_blue,
                                          bg=midnight_blue,
                                          font=('Courier', 16, 'bold'))

        # Buttons

        # Button
        self.button_begin = tk.Button(self.window,
                                      text='Sistema connesso! Iniziamo :)',
                                      bg='orange',
                                      font=('Courier', 16, 'bold'),
                                      command=self.begin)

        self.button_begin.place(x=50, y=200)

        # Button
        self.button_login = tk.Button(self.window,
                                      text='Login',
                                      bg='orange',
                                      font=('Courier', 16, 'bold'),
                                      command=self.login)

        self.button_confirm_login = tk.Button(self.window,
                                              text='Login',
                                              bg='orange',
                                              font=('Courier', 16, 'bold'),
                                              command=self.send_data_to_login)

        # Button
        self.button_new_user = tk.Button(self.window,
                                         text='Registrati',
                                         bg='orange',
                                         font=('Courier', 16, 'bold'),
                                         command=self.new_user)

        self.button_back = tk.Button(self.window,
                                     text='Indietro',
                                     bg='orange',
                                     font=('Courier', 16, 'bold'),
                                     command=self.back)

        self.button_create_new_user = tk.Button(self.window,
                                                text='Registrati!',
                                                bg='orange',
                                                font=('Courier', 16, 'bold'),
                                                command=self.send_data_for_new_registration)

        # TextBox
        self.tb_fiscal_code = tk.Entry(self.window,
                                       bg=solarized_orange,
                                       font=('Courier', 16, 'bold'))

        self.tb_name = tk.Entry(self.window,
                                bg=solarized_orange,
                                font=('Courier', 16, 'bold'))

        self.tb_surname = tk.Entry(self.window,
                                   bg=solarized_orange,
                                   font=('Courier', 16, 'bold'))

        self.tb_password = tk.Entry(self.window,
                                    bg=solarized_orange,
                                    font=('Courier', 16, 'bold'),
                                    show='*')

        self.tb_re_password = tk.Entry(self.window,
                                       bg=solarized_orange,
                                       font=('Courier', 16, 'bold'),
                                       show='*')

        self.tb_login_password = tk.Entry(self.window,
                                          bg=solarized_orange,
                                          font=('Courier', 16, 'bold'),
                                          show='*')

        self.tb_login_cf = tk.Entry(self.window,
                                    bg=solarized_orange,
                                    font=('Courier', 16, 'bold'))

        # DropDown
        option = ['Medico', 'Farmacologo']
        self.med_or_pharma = tk.StringVar(self.window)
        self.med_or_pharma.set('Medico')
        self.option_doctor_or_ph = tk.OptionMenu(self.window,
                                                 self.med_or_pharma,
                                                 *option)
        self.option_doctor_or_ph.config(bg=solarized_orange, font=('Courier', 16, 'bold'), width=15)

        # MainLoop
        self.window.mainloop()

    def begin(self):
        self.button_begin.place_forget()
        self.button_login.place(x=50, y=250)
        self.button_new_user.place(x=50, y=200)

    def login(self):
        self.button_new_user.place_forget()
        self.button_login.place_forget()

        self.label_login_fiscal_code.place(x=110, y=150)
        self.tb_login_cf.place(x=110, y=180)
        self.label_login_password.place(x=110, y=210)

        self.tb_login_password.place(x=110, y=240)
        self.button_confirm_login.place(x=110, y=270)
        self.button_back.place(x=10, y=450)

    def send_data_to_login(self):
        fiscal_code = self.tb_login_cf.get()
        password = self.tb_login_password.get()
        # password = Defender.get_password_hash(password)
        data_to_send = {'cf': fiscal_code,
                        'password': password}
        name, surname, role, login_access = ApiWhisper().authenticate(data_to_send)
        if login_access and name and surname:
            messagebox.showinfo('Server', 'Benvenuto ' + name + ' ' + surname + '!')
            if role == 'Medico':
                InstantiateGraphicalObject(session=fiscal_code).virtual_title(name, surname)
            elif role == 'Farmacologo':
                DrawPharmaMan().draw_title(name, surname)
        elif not login_access and name and surname and role is None:
            messagebox.showerror('Server', 'Credenziali invalide :/')
        else:
            messagebox.showerror('Server', 'Server non raggiungibile, provare più tardi :/')

    def new_user(self):
        self.button_new_user.place_forget()
        self.button_login.place_forget()

        self.label_name.place(x=110, y=10)
        self.tb_name.place(x=110, y=40)

        self.label_surname.place(x=110, y=70)
        self.tb_surname.place(x=110, y=100)

        self.label_med_or_pharma.place(x=110, y=170)
        self.option_doctor_or_ph.place(x=110, y=200)

        self.label_fiscal_code.place(x=110, y=250)
        self.tb_fiscal_code.place(x=110, y=280)

        self.label_password.place(x=110, y=310)
        self.tb_password.place(x=110, y=340)

        self.label_re_password.place(x=110, y=370)
        self.tb_re_password.place(x=110, y=400)

        self.button_create_new_user.place(x=150, y=450)

        self.button_back.place(x=10, y=450)

    def send_data_for_new_registration(self):
        fiscal_code = self.tb_fiscal_code.get()
        password = self.tb_password.get()
        re_password = self.tb_re_password.get()
        name = self.tb_name.get()
        surname = self.tb_surname.get()

        if Defender.name_surname(name) and Defender.name_surname(surname):
            self.tb_name.config(bg='green')
            self.tb_surname.config(bg='green')
            go_name = True
        else:
            self.tb_name.config(bg='red')
            self.tb_surname.config(bg='red')
            go_name = False

        if Defender.fiscal_code(fiscal_code):
            self.tb_fiscal_code.config(bg='green')
            go_fiscal_code = True
        else:
            self.tb_fiscal_code.config(bg='red')
            go_fiscal_code = False

        if Defender.password(password) and Defender.password(re_password) and \
                Defender.password_is_re_password(password, re_password):
            # password = Defender.get_password_hash(password)
            self.tb_password.config(bg='green')
            self.tb_re_password.config(bg='green')
            go_pass = True
        else:
            self.tb_password.config(bg='red')
            self.tb_re_password.config(bg='red')
            go_pass = False

        if go_pass and go_name and go_fiscal_code:
            obj_to_send = {'Nome': name,
                           'Cognome': surname,
                           'Ruolo': str(self.med_or_pharma.get()),
                           'CF': fiscal_code,
                           'Password': password}

            self.registration_complete(obj_to_send)

    def registration_complete(self, obj: json):
        self.unpack_positions()
        if ApiWhisper().post_new_user_to_server(obj):
            messagebox.showinfo('Server', 'Registrazione completata!')
            self.begin()
        else:
            messagebox.showerror('Server', 'Registrazaione non completata, riprovare più tardi')
            self.begin()

    def back(self):
        self.unpack_positions()
        self.begin()

    def unpack_positions(self):
        self.label_login_fiscal_code.place_forget()
        self.tb_login_cf.place_forget()
        self.label_login_password.place_forget()
        self.tb_login_password.place_forget()
        self.button_back.place_forget()
        self.label_surname.place_forget()
        self.label_name.place_forget()
        self.label_password.place_forget()
        self.label_med_or_pharma.place_forget()
        self.option_doctor_or_ph.place_forget()
        self.tb_name.place_forget()
        self.option_doctor_or_ph.place_forget()
        self.tb_surname.place_forget()
        self.label_fiscal_code.place_forget()
        self.tb_fiscal_code.place_forget()
        self.label_password.place_forget()
        self.tb_password.place_forget()
        self.label_re_password.place_forget()
        self.tb_re_password.place_forget()
        self.button_create_new_user.place_forget()
        self.button_confirm_login.place_forget()
