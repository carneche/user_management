import db

class Utilisateur:
    def __init__(self):
        pass
    #     self.identifiant = 0
    #     self.nom = ""
    #     self.prenom = ""
    #     self.age = 15
    #     self.ville = ""

    def chargerDonnees(self):
        try:
            con = db.connexion()
            cursor = con.cursor()
            requete = "SELECT mat, nom, prenom, age, ville FROM Users"
            cursor.execute(requete)
            resultat = cursor.fetchall()
        except BaseException as e :
            print("Erreur", e)
        else:
            header = ["Matricule", "Nom", "Prénom", "Age", "Ville"]
            mylist = [element for element in resultat]
        return header, mylist

    def rechercherUserId(self, id):
        try:
            con = db.connexion()
            cursor = con.cursor()
            requete = "SELECT * FROM users WHERE mat = %s"
            valeurs = (id,)
            cursor.execute(requete, valeurs)
            resultat = cursor.fetchone()
        except EOFError as e:
            print("Erreur", e)
        else:
            return resultat

    def rechercherUserName(self, nom):
        try:
            con = db.connexion()
            cursor = con.cursor()
            requete = "SELECT * FROM users WHERE nom = %s"
            valeurs = (nom,)
            cursor.execute(requete, valeurs)
            resultat = cursor.fetchone()
        except EOFError as e:
            print("Erreur", e)
        else:
            return resultat

    def ajoutUser(self, mat, nom, prenom, age, ville):
        nom = str(nom)
        prenom = str(prenom)
        ville = str(ville)
        try:
            if nom.isdigit() or prenom.isdigit() or ville.isdigit():
                raise ValueError("Seul l'âge doit être un entier.")
            if age < 14:
                raise ValueError("L'âge doit être un supérieur à 14 ans.")
            con = db.connexion()
            cursor = con.cursor()
            requete = "INSERT INTO Users (mat, nom, prenom, age, ville) VALUES (%s, %s, %s, %s, %s)"
            valeurs = (mat, nom, prenom, age, ville, )
            cursor.execute(requete, valeurs)
            con.commit()
        except ValueError as e:
            print(e, "Veuillez entrer les caractères...")
        else:
            print(cursor.rowcount, "élément enregistré dans la base.")
            
    def supprimerUser(self, mat):
        try:
            con = db.connexion()
            cursor = con.cursor()
            requete = "DELETE FROM Users WHERE mat = %s"
            valeur = (mat, )
            cursor.execute(requete, valeur)
            con.commit()
        except BaseException as e:
            print("Erreur", e)
        else:
            print(cursor.rowcount, "enregistrement a été supprimé.")
    
    def modifierUser(self, mat, nom, prenom, age, ville, mat1):
        try:
            con = db.connexion()
            cursor = con.cursor()
            requete = "UPDATE Users SET mat = %s, nom = %s, prenom = %s, age =%s, ville = %s WHERE mat = %s" 
            valeur = (mat, nom, prenom, age, ville, mat1, )
            cursor.execute(requete, valeur)
            con.commit()
        except BaseException as e:
            print("Erreur", e)
        else:
            print(cursor.rowcount, "enregistrement a été modifié.")

    def afficherUsers(self):
        try:
            con = db.connexion()
            cursor = con.cursor()
            requete = "SELECT mat, nom, prenom, age, ville FROM Users"
            cursor.execute(requete)
            resultat = cursor.fetchall()
        except BaseException as e :
            print("Erreur", e)
        else:
            return resultat
                # print (f"Matricule : {element[0]} - Nom :{element[1]} - Prénom :{element[2]} Age : {element[3]} - Ville : {element[4]}")


util = Utilisateur()
# print(util.rechercherUser("MAT01"))
# util.ajoutUser("MAT07", "MATON", "Jacques", 21, "Fontenay")
# util.supprimerUser("MAT07")
# util.modifierUser("MAT06", "Coquelin", "Eugène", 21, "Fontenay", "MAT06")
# util.afficherUsers()
   
# con = db.connexion()
# cursor = con.cursor()
# cursor.execute("SELECT * FROM users")

# result = cursor.fetchall()

# for x in result:
#   print(x)
