import flet as ft
from model import corso


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

        self._btnCercaStudente = None
        self._btnCercaIscritti = None
        self._cognome = None
        self._nome = None
        self._matr = None
        self._ddListaCorsi = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App gestione studenti", color="blue", size=24)

        # Aggiungo dropdown dei corsi e lo riempio
        self._ddListaCorsi = ft.Dropdown(label="corso", hint_text="Selezionare un corso", options=[], expand = True)
        self._controller.fillListaCorsi()

        #Bottone per cercare iscritti
        self._btnCercaIscritti = ft.ElevatedButton(text="Cerca iscritti", on_click=self._controller.handleCercaIscritti)


        #Campi per matricola nome e cognome studente
        self._matr = ft.TextField(label= "Matricola", hint_text="Inserisci matricola", expand = True)
        self._nome = ft.TextField(label="Nome", expand=True, disabled= True)
        self._cognome = ft.TextField(label="Cognome", expand=True, disabled= True)

        #Bottone per cercare uno studente
        self._btnCercaStudente = ft.ElevatedButton(text="Cerca studente", on_click=self._controller.handleCercaStudente)

        #Bottone per cercare i corsi di uno studente
        self._btnCercaCorsi = ft.ElevatedButton(text="Cerca corsi", on_click=self._controller.handleCercaCorsi)

        row = ft.Container(self._title, alignment=ft.alignment.center)
        row1 = ft.Row([self._ddListaCorsi, self._btnCercaIscritti], alignment=ft.MainAxisAlignment.CENTER)
        row2 = ft.Row([self._matr, self._nome, self._cognome], alignment=ft.MainAxisAlignment.CENTER)
        row3 = ft.Row([self._btnCercaStudente, self._btnCercaCorsi], alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row, row1, row2, row3)

        #ROW with some controls
        # text field for the name
        # self.txt_name = ft.TextField(
        #     label="name",
        #     width=200,
        #     hint_text="Insert a your name"
        # )
        #
        # # button for the "hello" reply
        # self.btn_hello = ft.ElevatedButton(text="Hello", on_click=self._controller.handle_hello)
        # row1 = ft.Row([self.txt_name, self.btn_hello],
        #               alignment=ft.MainAxisAlignment.CENTER)
        # self._page.controls.append(row1)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
