import operator
from PySide2 import QtWidgets, QtGui, QtCore

class MyTableModel(QtCore.QAbstractTableModel):
    def __init__(self, parent, header, mylist):
        super().__init__()
        self.header = header
        self.mylist = mylist

    def rowCount(self, parent):
        return len(self.mylist)

    def columnCount(self, parent):
        return len(self.mylist[0])

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != QtCore.Qt.DisplayRole:
            return None
        return self.mylist[index.row()][index.column()]

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.header[col]
        return None
    
    # def flags(self, index):
    #     return QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsSelectable

    # def sort(self, col, order):
    #     """sort table by given column number col"""
    #     self.emit(QtCore.SIGNAL("layoutAboutToBeChanged()"))
    #     self.mylist = sorted(self.mylist,
    #                          key=operator.itemgetter(col))
    #     if order == QtCore.Qt.DescendingOrder:
    #         self.mylist.reverse()
    #     self.emit(QtCore.SIGNAL("layoutChanged()"))

# try:
#     con = db.connexion()
#     cursor = con.cursor()
#     requete = "SELECT mat, nom, prenom, age, ville FROM Users"
#     cursor.execute(requete)
#     resultat = cursor.fetchall()
# except BaseException as e :
#     print("Erreur", e)
# else:
#     header = ["Matricule", "Nom", "Prénom", "Age", "Ville"]
#     data_list = [element for element in resultat]