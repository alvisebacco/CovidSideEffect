import json
import tkinter as tk
from tkinter import messagebox, scrolledtext
from ApiOperations.ApiWhisper import ApiWhisper
import webbrowser
import requests


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
        api_prefix = f'/api/covid/get_reactions/{self.doctor}'
        response = ApiWhisper().get_reactions_from_doctor(api_prefix)
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
            label_data = tk.Label(text_area, text='Data\n\n' + all_date, font=('Courier', 16, 'bold'))
            label_data.grid(column=0, row=0)

            label_paziente = tk.Label(text_area, text='Pazienti\n\n' + all_patient, font=('Courier', 16, 'bold'),
                                      padx=space)
            label_paziente.grid(column=1, row=0)

            label_reazione = tk.Label(text_area, text='Reazione\n\n' + all_reaction, font=('Courier', 16, 'bold'))
            label_reazione.grid(column=2, row=0)

            label_vacc = tk.Label(text_area, text='Vaccinazione\n\n' + all_vacc, font=('Courier', 16, 'bold'),
                                  padx=space)
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
    def __init__(self, session):
        # Variabili per comporre la query
        self.bk_label = None
        self.s = None
        self.v = None
        self.h = None
        # Variabili di uso generico
        self.ph = session
        self.dark_green: str = '#073002'
        self.solarized_green: str = '#5CFF87'
        super(DrawPharmaMan, self).__init__(window_bg=self.dark_green, title=f'CEST Edizione Farmacologo: {session}',
                                            geometry='950x500')

    def virtual_title(self, name: str, surname: str, **kwargs) -> None:
        super(DrawPharmaMan, self).virtual_title(name, surname,
                                                 'Farm.', 16, 16, self.dark_green, self.solarized_green, 10, 10)

        self.get_all_data_for_pharmaman()

    def get_all_data_for_pharmaman(self):
        i = 0
        api_prefix = f'/api/covid/get_all/{self.ph}'
        response = ApiWhisper().get_reactions_from_doctor(api_prefix)
        response_numb = response['Number'][0]
        self.bk_label = tk.Label(self.window,
                                 text='Selezionare la scelta desiderata',
                                 fg=self.solarized_green,
                                 bg=self.dark_green,
                                 font=('Courier', 16, 'bold'))
        self.bk_label.place(x=10, y=100)

        if response != 'Error':
            numbers_of_detection = response['Number'][0]
            # 50 e' troppo, uso 5 in fase di test
            if numbers_of_detection >= 5:
                button_all = tk.Button(self.window,
                                       text='Tutto',
                                       bg='orange',
                                       font=('Courier', 16, 'bold'),
                                       command=self.get_all_all)
                button_all.place(x=10, y=350)

                button_all_patient = tk.Button(self.window,
                                               text='Vaccinazioni ordinate per medico curante',
                                               bg='orange',
                                               font=('Courier', 16, 'bold'),
                                               command=self.get_all_patient)
                button_all_patient.place(x=200, y=150)

                button_all_patient_ordered_by_vaccination = tk.Button(self.window,
                                                                      text='Pazienti ordinati per vaccinazione',
                                                                      bg='orange',
                                                                      font=('Courier', 16, 'bold'),
                                                                      command=
                                                                      self.get_all_patient_ordered_by_vaccination)
                button_all_patient_ordered_by_vaccination.place(x=200, y=200)

                button_reaction = tk.Button(self.window,
                                            text='Reazioni per gravità',
                                            bg='orange',
                                            font=('Courier', 16, 'bold'),
                                            command=self.get_for_critallity)
                button_reaction.place(x=200, y=250)

                button_reaction_vacc = tk.Button(self.window,
                                                 text='Reazioni per vaccinazione',
                                                 bg='orange',
                                                 font=('Courier', 16, 'bold'),
                                                 command=self.get_for_critallity_vacc)
                button_reaction_vacc.place(x=200, y=300)

                button_risk = tk.Button(self.window,
                                        text='Rischi per paziente, ordinati per rischio',
                                        bg='orange',
                                        font=('Courier', 16, 'bold'),
                                        command=self.get_risk)
                button_risk.place(x=200, y=350)

                button_vaccination = tk.Button(self.window,
                                               text='Vaccinazioni per paziente, dose e site',
                                               bg='orange',
                                               font=('Courier', 16, 'bold'),
                                               command=self.get_vaccination_info)
                button_vaccination.place(x=200, y=400)

                button_vaccination_ = tk.Button(self.window,
                                                text='Vaccinazioni per sito',
                                                bg='orange',
                                                font=('Courier', 16, 'bold'),
                                                command=self.get_vaccination_info_)
                button_vaccination_.place(x=200, y=450)

                button_vaccination_ = tk.Button(self.window,
                                                text='Segnala...',
                                                bg='red',
                                                font=('Courier', 16, 'bold'),
                                                command=self.post_segnalation)
                button_vaccination_.place(x=750, y=450)

    @staticmethod
    def get_all_all():
        api_prefix = f'/api/covid/all/all'
        url = 'http://127.0.0.1:5006' + api_prefix
        webbrowser.open(url)

    @staticmethod
    def get_all_patient():
        api_prefix = f'/api/covid/all/patient'
        url = 'http://127.0.0.1:5006' + api_prefix
        webbrowser.open(url)

    @staticmethod
    def get_all_patient_ordered_by_vaccination():
        api_prefix = f'/api/covid/all/patient_order_by_vaccination'
        url = 'http://127.0.0.1:5006' + api_prefix
        webbrowser.open(url)

    @staticmethod
    def get_for_critallity():
        api_prefix = f'/api/covid/all/criticality'
        url = 'http://127.0.0.1:5006' + api_prefix
        webbrowser.open(url)

    @staticmethod
    def get_for_critallity_vacc():
        api_prefix = f'/api/covid/all/vacc'
        url = 'http://127.0.0.1:5006' + api_prefix
        webbrowser.open(url)

    @staticmethod
    def get_risk():
        api_prefix = f'/api/covid/all/risk'
        url = 'http://127.0.0.1:5006' + api_prefix
        webbrowser.open(url)

    @staticmethod
    def get_vaccination_info():
        api_prefix = f'/api/covid/all/vaccination_info'
        url = 'http://127.0.0.1:5006' + api_prefix
        webbrowser.open(url)

    @staticmethod
    def get_vaccination_info_():
        api_prefix = f'/api/covid/all/vaccination_info_'
        url = 'http://127.0.0.1:5006' + api_prefix
        webbrowser.open(url)

    @staticmethod
    def post_segnalation():
        api_prefix = f'/api/covid/all/order_by_vaccination_risks'
        url = 'http://127.0.0.1:5006' + api_prefix
        vaccinations = requests.get(url)
        vaccinations = json.loads(vaccinations.text)
        for content in vaccinations['Vaccinazioni']:
            messagebox.askyesno('Segnalare?', content)

    @staticmethod
    def get_str_instead_of_array_with_space(_list_: list) -> str:
        magic_string: str = ''
        for elements in _list_:
            magic_string += elements + '\n'
        return magic_string
