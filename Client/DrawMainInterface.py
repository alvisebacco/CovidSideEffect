import tkinter as tk
from tkinter import messagebox


class DrawMainObj:
    def __init__(self, window_bg, title, geometry):

        self.window = tk.Tk()
        self.window.geometry(geometry)
        self.window['background'] = window_bg
        self.window.title(title)

    def draw_title(self, name: str, surname: str, role: str, dimension: int, bg: str, fg: str, x: int, y: int):
        label_welcome = tk.Label(self.window,
                                 text=f'Benvenuto {role} {name} {surname}',
                                 bg=bg,
                                 fg=fg,
                                 font=('Courier', dimension, 'bold'))
        label_welcome.place(x=x, y=y)

        label_subtitle = tk.Label(self.window,
                                  text=f'Segnalazioni di reazioni avverse da vaccini anti-Covid',
                                  bg=bg,
                                  fg=fg,
                                  font=('Courier', dimension, 'bold'))
        label_subtitle.place(x=x, y=y+20)


class DrawDoctor(DrawMainObj):
    def __init__(self):
        self.dark_red: str = '#910000'
        self.solarized_red: str = '#FF8282'
        super(DrawDoctor, self).__init__(window_bg=self.dark_red, title='CSET Edizione Medico',
                                         geometry='960x768')

    def draw_title(self, name: str, surname: str, **kwargs) -> None:
        super(DrawDoctor, self).draw_title(name, surname,
                                           'Dr.', 36, self.dark_red, self.solarized_red, 100, 10)


class DrawPharmaMan(DrawMainObj):
    def __init__(self):
        self.dark_green: str = '#073002'
        self.solarized_green: str = '#5CFF87'
        super(DrawPharmaMan, self).__init__(window_bg=self.dark_green, title='CEST Edizione Farmacologo',
                                            geometry='750x500')

    def draw_title(self, name: str, surname: str, **kwargs) -> None:
        super(DrawPharmaMan, self).draw_title(name, surname,
                                              'Farm.', 16, self.dark_green, self.solarized_green, 10, 10)
