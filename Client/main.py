# Client per il tracciamento degli effetti
# indesiderati delle vaccinazioni anti Covid-19

# Alvise Bacco
# 19/04/22

# Made with <3

from tkinter import messagebox
from DrawObj import DrawObj
import requests
from ApiOperations.ApiWhisper import ApiWhisper

if __name__ == '__main__':
    if ApiWhisper().check_connection():
        DrawObj()
    else:
        is_internet_connected = requests.get('https://8.8.8.8')
        if is_internet_connected.status_code == 200:
            messagebox.showerror('Server', 'Server non disponibile!')
        else:
            messagebox.showerror('Internet', 'Internet non disponibile!')
