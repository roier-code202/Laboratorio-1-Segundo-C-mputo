import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        
       
        self.setWindowTitle("Ingreso de Datos")
        self.setGeometry(100, 100, 400, 200)
        
        
        self.label_nombre = QLabel("Nombre completo:", self)
        self.input_nombre = QLineEdit(self)
        
        
        self.label_dui = QLabel("Número de DUI:", self)
        self.input_dui = QLineEdit(self)

        
        self.boton = QPushButton("Confirmar", self)
        self.boton.clicked.connect(self.mostrar_datos)
        
        
        layout = QVBoxLayout()
        layout.addWidget(self.label_nombre)
        layout.addWidget(self.input_nombre)
        layout.addWidget(self.label_dui)
        layout.addWidget(self.input_dui)
        layout.addWidget(self.boton)

        self.setLayout(layout)

    def mostrar_datos(self):
        
        nombre = self.input_nombre.text()
        dui = self.input_dui.text()

        
        print(f"Nombre completo: {nombre}")
        print(f"Número de DUI: {dui}")

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    
    
    ventana = Ventana()
    ventana.show()
    
    
    sys.exit(app.exec_())
