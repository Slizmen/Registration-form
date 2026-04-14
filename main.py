import sys

from PyQt6.QtWidgets import QWidget, QApplication

from form_reg import Ui_Form

class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.addButton.clicked.connect(self.addItem)
        self.deleteButton.clicked.connect(self.deleteItem)
        self.items = []
    
    def addItem(self):
        name = self.namrField.text()
        gender = self.gender.currentText()
        date = self.dateEdit.date().toString('dd.MM.yyyy')
        self.items.append([name, gender, date])
        self.listWidget.addItem(', '.join([name, gender, date]))
    
    def deleteItem(self):
        index = self.listWidget.currentRow()
        if index == -1:
            return
        del self.items[index]
        self.updateList()
    
    def updateList(self):
        self.listWidget.clear()
        for item in self.items:
            self.listWidget.addItem(', '.join(item))

    
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
    