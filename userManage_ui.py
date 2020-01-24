from PySide2 import QtWidgets, QtGui, QtCore
from ui.fenetrePrincipale import Ui_fenetrePrincipale
from userManage import Utilisateur as ul # Les différentes méthodes de l'application
import customModel# as cm
import db

class UsersManage(QtWidgets.QWidget, Ui_fenetrePrincipale, ul):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        header, mylist = self.chargerDonnees()
        self.model = customModel.MyTableModel(self, header, mylist)
        self.tableView.setModel(self.model)
        self.msgBox = QtWidgets.QMessageBox()
        self.radio_matricule.setChecked(True)
        self.setupConnections()
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows) # Sélection de la ligne
        self.tableView.clicked.connect(self.selectionDonneesLigne)
        self.show()
    
    def setupConnections(self):
        self.btn_ajouter.clicked.connect(self.ajouterUtilisateur)
        # self.btn_modifier.connect(self.modifierUser)
        # self.btn_supprimer.connect(self.supprimerUser)
        self.btn_nettoyer.clicked.connect(self.nettoyerChamps)
        self.btn_rechercher.clicked.connect(self.rechercherUtilisateur)
    
    def selectionDonneesLigne(self, index):
        mat =  index.data() # Sélection d'un élément du tableau
        resultat = ul.rechercherUserId(self, mat)
        self.le_matricule.setText(resultat[1])
        self.le_nom.setText(resultat[2])
        self.le_prenom.setText(resultat[3])
        self.le_age.setText(str(resultat[4]))
        self.le_ville.setText(resultat[5])
        # a = self.tableView.selectionModel().
        # print(a)
   
    def ajouterUtilisateur(self):
        try:
            mat = self.le_matricule.text()
            nom = self.le_nom.text()
            prenom = self.le_prenom.text()
            age = int(self.le_age.text())
            ville = self.le_ville.text()        
        except TypeError:
            self.msgBox.setText("Erreur, vérifier les informations saisies.")
            self.msgBox.exec_()
        except ValueError :
            self.msgBox.setText("The document has been modified.")
            self.msgBox.exec_()
        else:
            ul.ajoutUser(self, mat, nom, prenom, age, ville)
            self.tableView.setModel(None)
            header, mylist = self.chargerDonnees()
            self.model = customModel.MyTableModel(self, header, mylist)
            self.tableView.setModel(self.model)

    def nettoyerChamps(self):
        indexes = self.tableView.selectionModel().selectedRows()
        for index in sorted(indexes):
            print('Row %d is selected' % index.row())
            # self.le_matricule.setText(" ")
            # self.le_nom.setText(" ")
            # self.le_prenom.setText(" ")
            # self.le_age.setText(" ")
            # self.le_ville.setText(" ")
    
    def rechercherUtilisateur(self):
        etat_radio = 0
        text = self.le_rechercher.text()   
        if self.radio_nom.isChecked():
            etat_radio = 1 
        try:
            if etat_radio == 0:                
                resultat = ul.rechercherUserId(self, text)
                self.le_matricule.setText(resultat[1])
                self.le_nom.setText(resultat[2])
                self.le_prenom.setText(resultat[3])
                self.le_age.setText(str(resultat[4]))
                self.le_ville.setText(resultat[5])
            else:
                resultat = ul.rechercherUserName(self, text)
                self.le_matricule.setText(resultat[1])
                self.le_nom.setText(resultat[2])
                self.le_prenom.setText(resultat[3])
                self.le_age.setText(str(resultat[4]))
                self.le_ville.setText(resultat[5])
        except TypeError:
            self.msgBox.setText("Attention !\n Vérifier les informations saisies.")
            self.msgBox.exec_()

    



    # def remplirChamps(self):
    #     resultat = self.afficherUsers()
    #     for element in resultat:
    #         self.le_matricule.setText(element[0])
    #         self.le_nom.setText(element[1])
    #         self.le_prenom.setText(element[2])
    #         self.le_age.setText(str(element[3]))
    #         self.le_ville.setText(element[4])

app = QtWidgets.QApplication([])
fn = UsersManage()
app.exec_()