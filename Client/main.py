# Client per il tracciamento degli effetti
# indesiderati delle vaccinazioni anti Covid-19

# Alvise Bacco
# 19/04/22

# Made with <3

import tkinter as tk
from tkinter import messagebox
import requests

from ApiOperations.ApiWhisper import ApiWhisper


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
        self.label_check_connection = tk.Label()

        # Pulsanti

        # Pulsante inizio
        self.button_begin = tk.Button(self.window,
                                      text='Sistema connesso! Iniziamo :)',
                                      bg='orange',
                                      font=('Courier', 16, 'bold'),
                                      command=self.begin)

        self.button_begin.pack()
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

        # TextBox
        self.fiscal_code = tk.Text

        # MainLoop
        self.window.mainloop()

    def begin(self):
        self.button_begin.place_forget()
        self.button_begin.pack_forget()
        self.button_login.pack()
        self.button_login.place(x=50, y=250)
        self.button_new_user.pack()
        self.button_new_user.place(x=50, y=200)

    def login(self):
        self.label_check_connection.config(text='Operativo :)')

    def new_user(self):
        self.button_new_user.pack_forget()
        self.button_new_user.place_forget()
        self.button_login.pack_forget()
        self.button_login.place_forget()




if __name__ == '__main__':
    if ApiWhisper().check_connection():
        DrawObj()
    else:
        is_internet_connected = requests.get('https://8.8.8.8')
        if is_internet_connected.status_code == 200:
            messagebox.showerror('Server', 'Server non disponibile!')
        else:
            messagebox.showerror('Internet', 'Internet non disponibile!')
