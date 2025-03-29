# Add whatever it is needed to interface with the DB Table corso

from database.DB_connect import DBConnect
from model.corso import Corso

def getAllCorsi():
    cnx = DBConnect.get_connection()
    cursor = cnx.cursor(dictionary=True)
    query = """select * from corso"""
    cursor.execute(query)
    ris = []
    for row in cursor:
        corso = Corso(row["codins"], row["crediti"], row["nome"], row["pd"])
        ris.append(corso)
    cnx.close()
    return ris

def getCorsi(matricola):
    cnx = DBConnect.get_connection()
    cursor = cnx.cursor(dictionary=True)
    query = """select codins from iscrizione where matricola = %s"""
    cursor.execute(query, (matricola,))

    ris1 = []
    for row in cursor:
        ris1.append(row["codins"])

    query2 = f"""select * from corso where codins in ({', '.join(['%s']*len(ris1))})"""
    cursor.execute(query2,ris1)

    corsi = [Corso(row["codins"], row["crediti"], row["nome"], row["pd"]) for row in cursor.fetchall()]
    cnx.close()
    return corsi