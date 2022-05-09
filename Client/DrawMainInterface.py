import tkinter as tk


class DrawMainObj:
    def __init__(self, window_bg, title, geometry):
        self.window = tk.Tk()
        self.window.geometry(geometry)
        self.window['background'] = window_bg
        self.window.title(title)

    def virtual_title(self, name: str, surname: str, role: str,
                      dimension: int, dimension_sub: int,
                      bg: str, fg: str, x: int, y: int):
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
                                  font=('Courier', dimension_sub, 'bold'))
        label_subtitle.place(x=x, y=y + 60)

    # Istanzia label
    def label_patient_informations(self, label_name, text, fg, bg, x, y):
        label_name = tk.Label(self.window,
                              text=text,
                              fg=fg,
                              bg=bg,
                              font=('Courier', 16, 'bold'))
        label_name.place(x=x, y=y)

    def separator(self, separator: str, bg: str, h: int, w: int, x: int, y: int):
        separator = tk.Frame(self.window, bg=bg, height=h, width=w)
        separator.place(x=x, y=y)


class DrawPharmaMan(DrawMainObj):
    def __init__(self):
        self.dark_green: str = '#073002'
        self.solarized_green: str = '#5CFF87'
        super(DrawPharmaMan, self).__init__(window_bg=self.dark_green, title='CEST Edizione Farmacologo',
                                            geometry='750x500')

    def draw_title(self, name: str, surname: str, **kwargs) -> None:
        super(DrawPharmaMan, self).virtual_title(name, surname,
                                                 'Farm.', 16, 16, self.dark_green, self.solarized_green, 10, 10)
