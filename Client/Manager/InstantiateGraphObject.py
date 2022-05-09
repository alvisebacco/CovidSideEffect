from DrawMainInterface import DrawMainObj
from DefensiveCode import Defender
import tkinter as tk
from tkinter import messagebox
from datetime import datetime


class InstantiateGraphicalObject(DrawMainObj):
    def __init__(self):
        self.dark_red: str = '#3c002f'
        self.solarized_red: str = '#FFCCCC'
        self.violet = '#e330b0'
        super(InstantiateGraphicalObject, self).__init__(window_bg=self.dark_red, title='CSET Edizione Medico',
                                                         geometry='960x768')
        self.title_ = ''
        self.cf = None
        self.default_text = None
        self.slider = None
        self.antiflu = None
        self.sinovak = None
        self.sputnik = None
        self.moderna = None
        self.pfzier = None
        self.astrazeneca = None
        self.under_pressure = None
        self.fatty_boy = None
        self.heart_cancer = None
        self.smoke = None
        self.font = 'Courier', 16, 'bold'
        self.tb_cf_existing_patient = tk.Entry(self.window, bg=self.solarized_red, fg=self.dark_red, font=self.font)
        self.tb_cf = tk.Entry(self.window, bg=self.solarized_red, fg=self.dark_red, font=self.font)
        self.tb_description = tk.Entry(self.window, bg=self.solarized_red, fg=self.dark_red, font=self.font)
        self.tb_reaction_date = tk.Entry(self.window, bg=self.solarized_red, fg=self.dark_red, font=self.font)
        self.tb_job = tk.Entry(self.window, bg=self.solarized_red, fg=self.dark_red, font=self.font)
        self.tb_city = tk.Entry(self.window, bg=self.solarized_red, fg=self.dark_red, font=self.font)
        self.tb_yyyy = tk.Entry(self.window, bg=self.solarized_red, fg=self.dark_red, font=self.font)

    def virtual_title(self, name: str, surname: str, **kwargs) -> None:
        super(InstantiateGraphicalObject, self).virtual_title(name, surname,
                                                              'Dr.', 36, 16, self.dark_red, self.violet, 100, 10)
        self.virtual_label()

    def virtual_label(self) -> None:
        super(InstantiateGraphicalObject, self).label_patient_informations('label_cf', 'Codice fiscale paziente:',
                                                                           self.solarized_red, self.dark_red, 10, 150)
        super(InstantiateGraphicalObject, self).label_patient_informations('label_year_of_birth', 'Anno di nascita:',
                                                                           self.solarized_red, self.dark_red, 10, 180)
        super(InstantiateGraphicalObject, self).label_patient_informations('label_city', 'Provincia:',
                                                                           self.solarized_red, self.dark_red, 10, 210)
        super(InstantiateGraphicalObject, self).label_patient_informations('job', 'Professione:',
                                                                           self.solarized_red, self.dark_red, 10, 240)
        super(InstantiateGraphicalObject, self).label_patient_informations('risk_factor', 'CF paziente: ',
                                                                           self.solarized_red, self.dark_red, 10, 320)
        super(InstantiateGraphicalObject, self).label_patient_informations('reaction_date', 'Data della reazione: '
                                                                                            '(es. 22/05/2022)',
                                                                           self.solarized_red, self.dark_red, 10, 430)
        super(InstantiateGraphicalObject, self).label_patient_informations('vaccinations_received',
                                                                           'Precedenti vaccinazioni ricevute',
                                                                           self.solarized_red, self.dark_red, 10, 460)
        super(InstantiateGraphicalObject, self).label_patient_informations('risk',
                                                                           'Precedenti vaccinazioni ricevute',
                                                                           self.solarized_red, self.dark_red, 10, 460)
        super(InstantiateGraphicalObject, self).separator('zero', self.solarized_red, 2, 950, 10, 120)
        super(InstantiateGraphicalObject, self).separator('first', self.solarized_red, 2, 950, 10, 300)
        super(InstantiateGraphicalObject, self).label_patient_informations('risk_level',
                                                                           'Gravità',
                                                                           self.solarized_red, self.dark_red, 10, 590)
        super(InstantiateGraphicalObject, self).label_patient_informations('risk_description',
                                                                           'Descrizione',
                                                                           self.solarized_red, self.dark_red, 400, 590)
        self.draw_text_box()

    def draw_text_box(self):
        self.tb_yyyy.place(x=350, y=180)
        self.tb_city.place(x=350, y=210)
        self.tb_job.place(x=350, y=240)
        self.tb_reaction_date.place(x=500, y=430)
        self.tb_description.place(x=200, y=650, width=700)
        self.tb_cf_existing_patient.place(x=500, y=320)
        self.tb_cf.place(x=350, y=150)
        self.draw_checkbox()

    def draw_checkbox(self):
        # CheckBox
        ck_smoke = tk.Checkbutton(self.window, bg=self.dark_red, fg=self.solarized_red, text='Fumatore',
                                  variable=self.smoke, onvalue=1, offvalue=0,
                                  font=('Courier', 16, 'bold'))
        ck_smoke.place(x=100, y=350)

        ck_iper = tk.Checkbutton(self.window, bg=self.dark_red, fg=self.solarized_red, text='Iperteso',
                                 variable=self.under_pressure, onvalue=1, offvalue=0,
                                 font=('Courier', 16, 'bold'))
        ck_iper.place(x=300, y=350)

        ck_fatty = tk.Checkbutton(self.window, bg=self.dark_red, fg=self.solarized_red, text='Sovrappeso',
                                  variable=self.fatty_boy, onvalue=1, offvalue=0,
                                  font=('Courier', 16, 'bold'))
        ck_fatty.place(x=500, y=350)

        ck_cardioonco = tk.Checkbutton(self.window, bg=self.dark_red, fg=self.solarized_red, text='Cardio/Onco',
                                       variable=self.heart_cancer, onvalue=1, offvalue=0,
                                       font=('Courier', 16, 'bold'))
        ck_cardioonco.place(x=700, y=350)
        super(InstantiateGraphicalObject, self).separator('two', self.solarized_red, 2, 950, 10, 400)
        ck_astra_z = tk.Checkbutton(self.window, bg=self.dark_red, fg=self.solarized_red, text='AstraZeneca',
                                    variable=self.astrazeneca, onvalue=1, offvalue=0,
                                    font=('Courier', 16, 'bold'))
        ck_astra_z.place(x=10, y=500)
        ck_pfizer = tk.Checkbutton(self.window, bg=self.dark_red, fg=self.solarized_red, text='Pfizer',
                                   variable=self.pfzier, onvalue=1, offvalue=0,
                                   font=('Courier', 16, 'bold'))
        ck_pfizer.place(x=10, y=530)
        ck_moderna = tk.Checkbutton(self.window, bg=self.dark_red, fg=self.solarized_red, text='Moderna',
                                    variable=self.moderna, onvalue=1, offvalue=0,
                                    font=('Courier', 16, 'bold'))
        ck_moderna.place(x=300, y=500)
        ck_sputnik = tk.Checkbutton(self.window, bg=self.dark_red, fg=self.solarized_red, text='Sputnik',
                                    variable=self.sputnik, onvalue=1, offvalue=0,
                                    font=('Courier', 16, 'bold'))
        ck_sputnik.place(x=300, y=530)
        ck_sinovak = tk.Checkbutton(self.window, bg=self.dark_red, fg=self.solarized_red, text='Sinovak',
                                    variable=self.sinovak, onvalue=1, offvalue=0,
                                    font=('Courier', 16, 'bold'))
        ck_sinovak.place(x=600, y=500)
        ck_antiflu = tk.Checkbutton(self.window, bg=self.dark_red, fg=self.solarized_red, text='Anti flu',
                                    variable=self.antiflu, onvalue=1, offvalue=0,
                                    font=('Courier', 16, 'bold'))
        ck_antiflu.place(x=600, y=530)

        super(InstantiateGraphicalObject, self).separator('first', self.solarized_red, 2, 950, 10, 580)

        slider = tk.Scale(self.window, from_=1, to=5, orient='horizontal')
        slider.place(x=10, y=650, variable=self.slider)
        self.draw_buttons()

    def draw_buttons(self):
        button_send_reaction = tk.Button(self.window,
                                         text='Invia reazione',
                                         bg='orange',
                                         font=('Courier', 16, 'bold'),
                                         command=print(''))
        button_send_reaction.place(x=700, y=700)

        button_post_data_patient = tk.Button(self.window,
                                             text='Registra paziente',
                                             bg='orange',
                                             font=('Courier', 16, 'bold'),
                                             command=self.post_data_patient)
        button_post_data_patient.place(x=700, y=230)

    def post_data_patient(self):
        patient_data = self.get_all_value_from_patient()
        cf = self.tb_cf.get()
        if len(cf) == 16:
            self.inset_into_cf(cf)

    def inset_into_cf(self, e):
        self.tb_cf_existing_patient.insert(0, e)

    def get_all_value_from_patient(self) -> tuple:
        fiscal_code = False
        year_of_birth = False
        province = False
        job = False

        patient_fiscal_code = self.tb_cf.get()
        if Defender.fiscal_code(patient_fiscal_code):
            self.inset_into_cf(patient_fiscal_code)
        y_of_birth = self.tb_yyyy.get()
        if not y_of_birth.isdigit():
            messagebox.showerror('Client', 'Inserisci un valore tipo: 1985')
        y_of_birth = int(y_of_birth)
        if not Defender.year_is_only_year(y_of_birth):
            messagebox.showerror('Client', 'Anno non valido')
        return 'ok', 'baby'
