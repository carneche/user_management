import mysql.connector as mc

def connexion():
    mydb = mc.connect(
        host="localhost",
        user="root",
        passwd="",
        database="utilisateurs"
    )
    return mydb

