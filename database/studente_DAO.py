# Add whatever it is needed to interface with the DB Table studente
from database.DB_connect import DBConnect
from model.studente import Studente

def getIscritti(codiceCorso):
    cnx = DBConnect.get_connection()
    cursor = cnx.cursor(dictionary=True)
    query = """SELECT matricola FROM iscrizione WHERE codins = %s"""
    cursor.execute(query,(codiceCorso,))
    ris = []
    for row in cursor:
        ris.append(row["matricola"])

    query2 = f"""select * from studente where matricola in ({', '.join(['%s']*len(ris))})"""
    cursor.execute(query2,ris)
    studenti = [Studente(row["matricola"],row["cognome"],row["nome"],row["CDS"]) for row in cursor.fetchall()]
    cnx.close()
    return studenti

def getStudente(matricola):
    cnx = DBConnect.get_connection()
    cursor = cnx.cursor(dictionary=True)
    query = """select * from studente where matricola = %s"""
    cursor.execute(query,(matricola,))

    row = cursor.fetchone()
    cnx.close()

    if row:
        return Studente(row["matricola"],row["cognome"],row["nome"],row["CDS"])
    else:
        return None
