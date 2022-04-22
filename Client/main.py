# Client per il tracciamento degli effetti
# indesiderati delle vaccinazioni anti Covid-19

# Alvise Bacco
# 19/04/22

# Made with <3

import tkinter as tk
from tkinter import messagebox
import requests

from ApiOperations.ApiWhisper import ApiWhisper
from DefensiveCode import Defender


class DrawObj:
    def __init__(self):
        super().__init__()

        """Istanzio gli oggetti della UI"""

        # Finestra
        midnight_blue = '#151B54'
        self.window = tk.Tk()
        self.window.geometry('500x500')
        self.window['background'] = midnight_blue
        self.window.title('Covid Side Effect Tracker')

        # Etichette
        self.label_fiscal_code = tk.Label(self.window,
                                          text='Codice fiscale',
                                          fg='orange',
                                          bg=midnight_blue,
                                          font=('Courier', 16, 'bold'))

        self.label_password = tk.Label(self.window,
                                       text='Password',
                                       fg='orange',
                                       bg=midnight_blue,
                                       font=('Courier', 16, 'bold'))

        self.label_re_password = tk.Label(self.window,
                                          text='Re-Password',
                                          fg='orange',
                                          bg=midnight_blue,
                                          font=('Courier', 16, 'bold'))

        # Pulsanti

        # Pulsante inizio
        self.button_begin = tk.Button(self.window,
                                      text='Sistema connesso! Iniziamo :)',
                                      bg='orange',
                                      font=('Courier', 16, 'bold'),
                                      command=self.begin)

        self.button_begin.place(x=50, y=200)

        # Pulsante di login
        self.button_login = tk.Button(self.window,
                                      text='Login',
                                      bg='orange',
                                      font=('Courier', 16, 'bold'),
                                      command=self.login)

        # Pulsante registrati
        self.button_new_user = tk.Button(self.window,
                                         text='Registrati',
                                         bg='orange',
                                         font=('Courier', 16, 'bold'),
                                         command=self.new_user)

        self.button_create_new_user = tk.Button(self.window,
                                                text='Invia i dati!',
                                                bg='orange',
                                                font=('Courier', 16, 'bold'),
                                                command=self.send_data_for_new_registration)

        # TextBox
        self.tb_fiscal_code = tk.Entry(self.window,
                                       bg='orange',
                                       font=('Courier', 16, 'bold'))

        self.tb_password = tk.Entry(self.window,
                                    bg='orange',
                                    font=('Courier', 16, 'bold'),
                                    show='*')
        self.tb_re_password = tk.Entry(self.window,
                                       bg='orange',
                                       font=('Courier', 16, 'bold'),
                                       show='*')

        # MainLoop
        self.window.mainloop()

    def begin(self):
        self.button_begin.place_forget()
        self.button_login.place(x=50, y=250)
        self.button_new_user.place(x=50, y=200)

    def login(self):
        pass

    def new_user(self):
        self.button_new_user.place_forget()
        self.button_login.place_forget()

        self.label_fiscal_code.place(x=100, y=50)
        self.tb_fiscal_code.place(x=100, y=80)

        self.label_password.place(x=100, y=150)
        self.tb_password.place(x=100, y=180)

        self.label_re_password.place(x=100, y=250)
        self.tb_re_password.place(x=100, y=280)

        self.button_create_new_user.place(x=100, y=330)

    def send_data_for_new_registration(self):
        can_we_go = True
        fiscal_code = self.tb_fiscal_code.get()
        password = self.tb_password.get()
        re_password = self.tb_re_password.get()

        if Defender.fiscal_code(fiscal_code):
            self.tb_fiscal_code.config(bg='green')
        else:
            self.tb_fiscal_code.config(bg='red')
            can_we_go = False

        if Defender.password(password) and Defender.password(re_password) and \
                Defender.password_is_re_password(password, re_password):
            self.tb_password.config(bg='green')
            self.tb_re_password.config(bg='green')
        else:
            self.tb_password.config(bg='red')
            self.tb_re_password.config(bg='red')
            can_we_go = False

        if can_we_go:
            self.label_fiscal_code.place_forget()
            self.tb_fiscal_code.place_forget()
            self.label_password.place_forget()
            self.tb_password.place_forget()
            self.label_re_password.place_forget()
            self.tb_re_password.place_forget()
            self.button_create_new_user.place_forget()
            self.begin()


if __name__ == '__main__':
    if ApiWhisper().check_connection():
        DrawObj()
    else:
        is_internet_connected = requests.get('https://8.8.8.8')
        if is_internet_connected.status_code == 200:
            messagebox.showerror('Server', 'Server non disponibile!')
        else:
            messagebox.showerror('Internet', 'Internet non disponibile!')
