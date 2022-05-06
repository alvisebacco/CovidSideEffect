import tkinter as tk
from tkinter import messagebox


class DrawMainObj:
    def __init__(self, window_bg, title, geometry):
        self.window = tk.Tk()
        self.window.geometry(geometry)
        self.window['background'] = window_bg
        self.window.title(title)

    def draw_title(self, name: str, surname: str, role: str,
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


class DrawDoctor(DrawMainObj):
    def __init__(self):
        self.under_pressure = None
        self.fatty_boy = None
        self.heart_cancer = None
        self.smoke = None

        self.dark_red: str = '#3c002f'
        self.solarized_red: str = '#FF8282'

        super(DrawDoctor, self).__init__(window_bg=self.dark_red, title='CSET Edizione Medico',
                                         geometry='960x768')

    def draw_title(self, name: str, surname: str, **kwargs) -> None:
        super(DrawDoctor, self).draw_title(name, surname,
                                           'Dr.', 36, 16, self.dark_red, self.solarized_red, 100, 10)
        self.get_patient_information()

    def get_patient_information(self, **kwargs):
        super(DrawDoctor, self).label_patient_informations('label_year_of_birth', 'Anno di nascita:',
                                                           self.solarized_red, self.dark_red, 10, 120)
        super(DrawDoctor, self).label_patient_informations('label_city', 'Provincia:',
                                                           self.solarized_red, self.dark_red, 10, 150)
        super(DrawDoctor, self).label_patient_informations('job', 'Professione:',
                                                           self.solarized_red, self.dark_red, 10, 180)
        super(DrawDoctor, self).label_patient_informations('risk_factor', 'Fattori di rischio',
                                                           self.solarized_red, self.dark_red, 10, 270)

        tb_yyyy = tk.Entry(self.window,
                           bg=self.solarized_red,
                           fg=self.dark_red,
                           font=('Courier', 16, 'bold'))
        tb_yyyy.place(x=500, y=120)

        tb_city = tk.Entry(self.window,
                           bg=self.solarized_red,
                           fg=self.dark_red,
                           font=('Courier', 16, 'bold'))
        tb_city.place(x=500, y=150)

        tb_job = tk.Entry(self.window,
                          bg=self.solarized_red,
                          fg=self.dark_red,
                          font=('Courier', 16, 'bold'))
        tb_job.place(x=500, y=180)

        super(DrawDoctor, self).separator('first', self.solarized_red, 2, 950, 10, 240)

        # CheckBox
        ck_smoke = tk.Checkbutton(self.window, bg=self.dark_red, fg=self.solarized_red, text='Fumo',
                                  variable=self.smoke, onvalue=1, offvalue=0,
                                  font=('Courier', 16, 'bold'))
        ck_smoke.place(x=100, y=300)

        ck_smoke = tk.Checkbutton(self.window, bg=self.dark_red, fg=self.solarized_red, text='Ipertensione',
                                  variable=self.under_pressure, onvalue=1, offvalue=0,
                                  font=('Courier', 16, 'bold'))
        ck_smoke.place(x=300, y=300)

        ck_smoke = tk.Checkbutton(self.window, bg=self.dark_red, fg=self.solarized_red, text='Sovrappeso',
                                  variable=self.fatty_boy, onvalue=1, offvalue=0,
                                  font=('Courier', 16, 'bold'))
        ck_smoke.place(x=500, y=300)

        ck_smoke = tk.Checkbutton(self.window, bg=self.dark_red, fg=self.solarized_red, text='Cardio/Onco',
                                  variable=self.heart_cancer, onvalue=1, offvalue=0,
                                  font=('Courier', 16, 'bold'))
        ck_smoke.place(x=700, y=300)


class DrawPharmaMan(DrawMainObj):
    def __init__(self):
        self.dark_green: str = '#073002'
        self.solarized_green: str = '#5CFF87'
        super(DrawPharmaMan, self).__init__(window_bg=self.dark_green, title='CEST Edizione Farmacologo',
                                            geometry='750x500')

    def draw_title(self, name: str, surname: str, **kwargs) -> None:
        super(DrawPharmaMan, self).draw_title(name, surname,
                                              'Farm.', 16, 16, self.dark_green, self.solarized_green, 10, 10)
