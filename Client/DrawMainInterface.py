import tkinter as tk
from tkinter import messagebox, scrolledtext
from ApiOperations.ApiWhisper import ApiWhisper


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


class DrawMyReaction(DrawMainObj):
    def __init__(self, doctor):
        self.doctor = doctor
        self.dark_red: str = '#634900'
        self.violet = '#ffe7a6'
        super(DrawMyReaction, self).__init__(window_bg=self.dark_red, title=f'Sessione univoca utente: {doctor}',
                                             geometry='1520x500')

    def virtual_title(self, name: str, surname: str, **kwargs) -> None:
        super(DrawMyReaction, self).virtual_title(name, surname,
                                                  'Dr.', 36, 16, self.dark_red, self.violet, 100, 10)
        self.print_reaction_on_window()

    def print_reaction_on_window(self):
        response = ApiWhisper().get_reactions_from_doctor(self.doctor)
        if response == 'Error':
            messagebox.showinfo('Server', f'Nessun dato presente per {self.doctor}')
        else:
            label_name = tk.Label(self.window,
                                  text='Lista delle segnalazioni effettuate',
                                  fg=self.violet,
                                  bg=self.dark_red,
                                  font=('Courier', 16, 'bold'))
            label_name.place(x=20, y=100)

            text_area = scrolledtext.ScrolledText(self.window,
                                                  wrap=tk.WORD,
                                                  height=10,
                                                  font=('Courier', 16, 'bold'))
            text_area.grid(column=4, row=len(response), pady=10, padx=10, columnspan=30)
            text_area.place(x=20, y=150)
            space = 200

            all_patient = []
            all_reaction = []
            all_date = []
            all_vacc = []

            for r in response['pazienti']:
                all_patient.append(r)
            all_patient = self.get_str_instead_of_array_with_slash_n(all_patient)

            for r in response['reazioni']:
                all_reaction.append(r)
            all_reaction = self.get_str_instead_of_array_with_slash_n(all_reaction)

            for r in response['date']:
                all_date.append(r)
            all_date = self.get_str_instead_of_array_with_slash_n(all_date)

            for r in response['vaccinazioni']:
                all_vacc.append(r)
            all_vacc = self.get_str_instead_of_array_with_slash_n(all_vacc)


            # Creo i nomi delle tabelle per la visualizzazione della tupla
            label_data = tk.Label(text_area, text='Data', font=('Courier', 16, 'bold'))
            label_data.grid(column=0, row=0)

            label_paziente = tk.Label(text_area, text='Pazienti\n\n' + all_patient, font=('Courier', 16, 'bold'),
                                      padx=space)
            label_paziente.grid(column=1, row=0)

            label_reazione = tk.Label(text_area, text='Reazione\n\n' + all_reaction, font=('Courier', 16, 'bold'))
            label_reazione.grid(column=2, row=0)

            label_vacc = tk.Label(text_area, text='Vaccinazione\n\n' + all_vacc, font=('Courier', 16, 'bold'), padx=space)
            label_vacc.grid(column=3, row=0)

            label_vacc = tk.Label(text_area, text='Data\n\n' + all_date, font=('Courier', 16, 'bold'), padx=space)
            label_vacc.grid(column=4, row=0)

            # Making the text read only
            text_area.configure(state='disabled')

    @staticmethod
    def get_str_instead_of_array_with_slash_n(_list_: list) -> str:
        magic_string: str = ''
        for element in _list_:
            magic_string += element + '\n'
        return magic_string


class DrawPharmaMan(DrawMainObj):
    def __init__(self):
        self.dark_green: str = '#073002'
        self.solarized_green: str = '#5CFF87'
        super(DrawPharmaMan, self).__init__(window_bg=self.dark_green, title='CEST Edizione Farmacologo',
                                            geometry='750x500')

    def virtual_title(self, name: str, surname: str, **kwargs) -> None:
        super(DrawPharmaMan, self).virtual_title(name, surname,
                                                 'Farm.', 16, 16, self.dark_green, self.solarized_green, 10, 10)
