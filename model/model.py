from database.corso_DAO import getAllCorsi, getCorsi
from database.studente_DAO import getIscritti, getStudente

class Model:
    def __init__(self):
        pass

    def elencoCorsi(self):
        return getAllCorsi()

    def cercaIscritti(self,codiceCorso):
        return getIscritti(codiceCorso)

    def cercaStudente(self,matricola):
        return getStudente(matricola)

    def cercaCorsi(self,matricola):
        return getCorsi(matricola)