import flet as ft
from model import corso
from model import studente

class Controller:

    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_hello(self, e):
        """Simple function to handle a button-pressed event,
        and consequently print a message on screen"""
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()

    def fillListaCorsi(self):
        lista = self._model.elencoCorsi()
        for i in lista:
            self._view._ddListaCorsi.options.append(ft.dropdown.Option(key = i.codins, text = str(i)))

    def handleCercaIscritti(self, e):
        self._view.txt_result.clean()
        corsoScelto = self._view._ddListaCorsi.value
        if corsoScelto is None:
           self._view.txt_result.controls.append(ft.Text("Attenzione! Non hai scelto un corso",color= "red"))
           self._view.update_page()
           return
        codiceCorso = corsoScelto
        listaStud = self._model.cercaIscritti(codiceCorso)
        self._view.txt_result.controls.append(ft.Text(f"Ci sono {len(listaStud)} iscritti:", color= "black"))
        for studente in listaStud:
            self._view.txt_result.controls.append(ft.Text(studente, color= "black"))
        self._view.update_page()
        return

    def handleCercaStudente(self, e):
        self._view.txt_result.clean()
        matricola = self._view._matr.value
        if matricola == "":
            self._view.txt_result.controls.append(ft.Text("Attenzione! Non hai scelto nessuna matricola", color="red"))
            self._view.update_page()
            return

        stud = self._model.cercaStudente(matricola)
        if stud is None:
            self._view.txt_result.controls.append(ft.Text("Attenzione! Matricola non presente", color="red"))
            self._view.update_page()
            return

        self._view._nome.value = stud.nome
        self._view._nome.color = "black"
        self._view._cognome.value = stud.cognome
        self._view._cognome.color = "black"
        self._view.update_page()
        return

    def handleCercaCorsi(self, e):
        self._view.txt_result.clean()
        matricola = self._view._matr.value
        if matricola == "":
            self._view.txt_result.controls.append(ft.Text("Attenzione! Non hai scelto nessuna matricola", color="red"))
            self._view.update_page()
            return
        stud = self._model.cercaStudente(matricola)

        if stud is None:
            self._view.txt_result.controls.append(ft.Text("Attenzione! Matricola non presente", color="red"))
            self._view.update_page()
            return

        self._view._nome.value = stud.nome
        self._view._nome.color = "black"
        self._view._cognome.value = stud.cognome
        self._view._cognome.color = "black"
        self._view.update_page()

        corsi = self._model.cercaCorsi(matricola)

        self._view.txt_result.controls.append(ft.Text(f"Lo studente è iscritto a {len(corsi)} corsi: ", color= "black"))
        for corso in corsi:
            self._view.txt_result.controls.append(ft.Text(corso, color= "black"))
        self._view.update_page()
        return


