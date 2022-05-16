import json

from DrawMainInterface import DrawMainObj
from DefensiveCode import Defender
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
from ApiOperations.ApiWhisper import ApiWhisper


class InstantiateGraphicalObject(DrawMainObj):
    def __init__(self, session):

        self.session = session
        self.dark_red: str = '#3c002f'
        self.solarized_red: str = '#FFCCCC'
        self.violet = '#e330b0'
        super(InstantiateGraphicalObject, self).__init__(window_bg=self.dark_red, title='CSET Edizione Medico',
                                                         geometry='960x768')
        self.title_ = ''
        self.cf = None
        self.default_text = None
        self.slider = tk.IntVar(self.window)
        self.antiflu = tk.StringVar(self.window)
        self.sinovak = tk.StringVar(self.window)
        self.sputnik = tk.StringVar(self.window)
        self.moderna = tk.StringVar(self.window)
        self.pfzier = tk.StringVar(self.window)
        self.astrazeneca = tk.StringVar(self.window)
        self.smoke = tk.StringVar(self.window)
        self.cardioonco = tk.StringVar(self.window)
        self.fatty = tk.StringVar(self.window)
        self.iper = tk.StringVar(self.window)
        self.ck_cardioonco = tk.Checkbutton(self.window, bg=self.dark_red, fg=self.solarized_red, text='Cardio/Onco',
                                            onvalue='Patologia cardiaca o neoplastica',
                                            offvalue='Non cardio, non neoplasie', variable=self.cardioonco,
                                            font=('Courier', 16, 'bold'))
        self.ck_fatty = tk.Checkbutton(self.window, bg=self.dark_red, fg=self.solarized_red, text='Sovrappeso',
                                       onvalue='Sovrappeso', offvalue='Non sovrappeso', variable=self.fatty,
                                       font=('Courier', 16, 'bold'))
        self.ck_iper = tk.Checkbutton(self.window, bg=self.dark_red, fg=self.solarized_red, text='Iperteso',
                                      onvalue='Iperteso', offvalue='Pressione regolare', variable=self.iper,
                                      font=('Courier', 16, 'bold'))
        self.ck_smoke = tk.Checkbutton(self.window, bg=self.dark_red, fg=self.solarized_red, text='Fumatore',
                                       variable=self.smoke, onvalue='Fumatore', offvalue='Non fumatore',
                                       font=('Courier', 16, 'bold'))

        self.ck_astra_z = tk.Checkbutton(self.window, bg=self.dark_red, fg=self.solarized_red, text='AstraZeneca',
                                         variable=self.astrazeneca, onvalue='Astrazeneca', offvalue='Non',
                                         font=('Courier', 16, 'bold'))
        self.ck_pfizer = tk.Checkbutton(self.window, bg=self.dark_red, fg=self.solarized_red, text='Pfizer',
                                        variable=self.pfzier, onvalue='Pfizer', offvalue='Non',
                                        font=('Courier', 16, 'bold'))
        self.ck_moderna = tk.Checkbutton(self.window, bg=self.dark_red, fg=self.solarized_red, text='Moderna',
                                         variable=self.moderna, onvalue='Moderna', offvalue='Non',
                                         font=('Courier', 16, 'bold'))
        self.ck_sputnik = tk.Checkbutton(self.window, bg=self.dark_red, fg=self.solarized_red, text='Sputnik',
                                         variable=self.sputnik, onvalue='Sputnik', offvalue='Non',
                                         font=('Courier', 16, 'bold'))
        self.ck_sinovak = tk.Checkbutton(self.window, bg=self.dark_red, fg=self.solarized_red, text='Sinovak',
                                         variable=self.sinovak, onvalue='Sinovak', offvalue='Non',
                                         font=('Courier', 16, 'bold'))
        self.ck_antiflu = tk.Checkbutton(self.window, bg=self.dark_red, fg=self.solarized_red, text='Anti flu',
                                         variable=self.antiflu, onvalue='Antinfluenzale', offvalue='Non',
                                         font=('Courier', 16, 'bold'))
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
                                                                                            '(gg/mm/aaaa)',
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
        deselect_all = []
        self.ck_smoke.place(x=100, y=350)
        deselect_all.append(self.ck_smoke)
        self.ck_iper.place(x=300, y=350)
        deselect_all.append(self.ck_iper)
        self.ck_fatty.place(x=500, y=350)
        deselect_all.append(self.ck_fatty)
        self.ck_cardioonco.place(x=700, y=350)
        deselect_all.append(self.ck_cardioonco)
        super(InstantiateGraphicalObject, self).separator('two', self.solarized_red, 2, 950, 10, 400)
        self.ck_astra_z.place(x=10, y=500)
        deselect_all.append(self.ck_astra_z)
        self.ck_pfizer.place(x=10, y=530)
        deselect_all.append(self.ck_pfizer)
        self.ck_moderna.place(x=300, y=500)
        deselect_all.append(self.ck_moderna)
        self.ck_sputnik.place(x=300, y=530)
        deselect_all.append(self.ck_sputnik)
        self.ck_sinovak.place(x=600, y=500)
        deselect_all.append(self.ck_sinovak)
        self.ck_antiflu.place(x=600, y=530)
        deselect_all.append(self.ck_antiflu)
        for checkbox in deselect_all:
            checkbox.deselect()

        super(InstantiateGraphicalObject, self).separator('first', self.solarized_red, 2, 950, 10, 580)
        slider = tk.Scale(self.window, from_=1, to=5, orient='horizontal', variable=self.slider)
        slider.place(x=10, y=650)
        self.draw_buttons()

    def draw_buttons(self):
        button_send_reaction = tk.Button(self.window,
                                         text='Invia reazione',
                                         bg='orange',
                                         font=('Courier', 16, 'bold'),
                                         command=self.post_reaction)
        button_send_reaction.place(x=700, y=700)

        button_post_data_patient = tk.Button(self.window,
                                             text='Registra paziente',
                                             bg='orange',
                                             font=('Courier', 16, 'bold'),
                                             command=self.post_data_patient)
        button_post_data_patient.place(x=700, y=230)

    def post_data_patient(self):
        self.tb_cf_existing_patient.delete(0, 16)
        get_job, get_province, get_y_of_birth, get_fiscal_code = self.get_all_value_from_patient()
        if get_job and get_province and get_y_of_birth and get_fiscal_code:
            self.inset_into_cf(get_fiscal_code)
            obj_to_send = {'CF': get_fiscal_code,
                           'yyyy': get_y_of_birth,
                           'city': get_province,
                           'job': get_job,
                           'med': self.session}
            api_prefix = f'/api/covid/new_patient'
            where_from, message = ApiWhisper().post_to_server(obj_to_send, api_prefix)
            messagebox.showinfo(where_from, message)

    def get_all_value_from_patient(self) -> tuple:
        fiscal_code = False
        year_of_birth = False
        province = False
        job = False

        get_fiscal_code = self.tb_cf.get()
        if Defender.fiscal_code(get_fiscal_code):
            fiscal_code = True
            self.tb_cf.config(bg='green')
        else:
            self.tb_cf.config(bg='red')

        get_y_of_birth = self.tb_yyyy.get()
        if not get_y_of_birth.isdigit():
            messagebox.showerror('Client', 'Anno di nascita tipo: 1985')
            year_of_birth = False
            self.tb_yyyy.config(bg='red')
        else:
            get_y_of_birth = int(get_y_of_birth)
            if not Defender.year_is_only_year(get_y_of_birth):
                messagebox.showerror('Client', 'Anno di nascita tipo: 1985')
                self.tb_yyyy.config(bg='red')
                year_of_birth = False
            else:
                year_of_birth = True
                self.tb_yyyy.config(bg='green')

        get_province = self.tb_city.get()
        if Defender.name_surname(str(get_province)):
            province = True
            self.tb_city.config(bg='green')
        else:
            self.tb_city.config(bg='red')

        get_job = self.tb_job.get()
        if Defender.name_surname(str(get_job)):
            job = True
            self.tb_job.config(bg='green')
        else:
            self.tb_job.config(bg='red')
        if fiscal_code and year_of_birth and province and job:
            return get_job, get_province, get_y_of_birth, get_fiscal_code
        else:
            return False, False, False, False

    def post_reaction(self):
        """Funzione per inserimento dati relativi al covid"""

        # fattori di rischio
        is_smoker = self.smoke.get()
        is_fatty = self.fatty.get()
        is_cardioonco = self.cardioonco.get()
        is_hypertension = self.iper.get()

        # vaccinazioni eseguite
        vaccinations = []
        has_astrazeneca = self.astrazeneca.get()
        vaccinations.append(has_astrazeneca)
        has_pfizer = self.pfzier.get()
        vaccinations.append(has_pfizer)
        has_antiflu = self.antiflu.get()
        vaccinations.append(has_antiflu)
        has_moderna = self.moderna.get()
        vaccinations.append(has_moderna)
        has_sputnik = self.sputnik.get()
        vaccinations.append(has_sputnik)
        has_sinovak = self.sinovak.get()
        vaccinations.append(has_sinovak)

        # Data di nascita
        reaction_date = self.tb_reaction_date.get()
        reaction_date, go_ok = Defender.check_and_get_datetime_reaction_date(reaction_date)
        if not go_ok:
            messagebox.showerror('Client', 'Data in formato non corretto!')
            self.tb_reaction_date.config(bg='red')
            date = False
        else:
            self.tb_reaction_date.config(bg='green')
            date = True

        # Cf paziente
        cf_patient = self.tb_cf_existing_patient.get()
        if not Defender.fiscal_code(cf_patient):
            messagebox.showerror('Client', 'Formato del codice fiscale non corretto')
            self.tb_cf_existing_patient.config(bg='red')
            cf = False
        else:
            self.tb_cf_existing_patient.config(bg='green')
            cf = True

        # Description
        description = self.tb_description.get()

        # Severity
        severity = self.slider.get()

        if cf and date:
            vaccination_received = []
            vaccination_dates = []
            vaccination_doses = []
            vaccination_places = []
            object_to_send = {}
            for vaccination in vaccinations:
                if vaccination != 'Non':
                    vaccination_received.append(vaccination)
                if vaccination != 'Non':
                    vaccination_date_is_not_good = True
                    while vaccination_date_is_not_good:
                        vaccination_date = simpledialog.askstring('Data', f'Data della vaccinazione per {vaccination} '
                                                                          f'espressa in gg/mm/aaaa')
                        iso_vaccination_date, its_ok = Defender.check_and_get_datetime_reaction_date(vaccination_date)
                        if its_ok:
                            vaccination_dates.append(vaccination_date)
                            vaccination_date_is_not_good = False
                        else:
                            vaccination_date_is_not_good = True

                    dose_is_not_good = True
                    while dose_is_not_good:
                        allowed_doses = ['I', 'II', 'III', 'IV', 'unica']
                        dose = simpledialog.askstring('Dose', f'Per quale dose di {vaccination} '
                                                              f'si segnala la reazione avversa?'
                                                              f'Indicare solo I, II, III, IV o unica')
                        if dose in allowed_doses:
                            vaccination_doses.append(dose)
                            dose_is_not_good = False
                        else:
                            dose_is_not_good = True
                    vaccination_place = None
                    while vaccination_place is None:
                        vaccination_place = simpledialog.askstring('Centro vaccinale',
                                                                   f'Dove è stata eseguita la vaccinazione '
                                                                   f'per {vaccination}?')
                    vaccination_places.append(vaccination_place)

            object_to_send = {'smoker': is_smoker,
                              'fatty': is_fatty,
                              'cardioonco': is_cardioonco,
                              'hypert': is_hypertension,
                              'reaction_date': str(reaction_date),
                              'cf_primary_key': cf_patient,
                              'vaccination_received': vaccination_received,
                              'vaccination_dates': vaccination_dates,
                              'vaccination_doses': vaccination_doses,
                              'vaccination_places': vaccination_places
                              }
            api_prefix = f'/api/covid/new_reaction/'
            server, message = ApiWhisper().post_to_server(object_to_send, api_prefix)

    def inset_into_cf(self, e):
        self.tb_cf_existing_patient.insert(0, e)
