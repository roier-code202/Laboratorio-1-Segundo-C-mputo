import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt

class Ventana(QWidget):
    def __init__(self, nombre, edad):
        super().__init__()
        
        
        self.setWindowTitle("Datos Personales")
        self.setGeometry(100, 100, 300, 200)
        
        
        self.label_nombre = QLabel(f"Nombre completo: {nombre}", self)
        self.label_edad = QLabel(f"Edad: {edad} años", self)

        
        self.label_nombre.setAlignment(Qt.AlignCenter)
        self.label_edad.setAlignment(Qt.AlignCenter)
        
       
        layout = QVBoxLayout()
        layout.addWidget(self.label_nombre)
        layout.addWidget(self.label_edad)
        
        self.setLayout(layout)

if __name__ == "__main__":
    
    nombre = "Roger Josue Hurtado Rivera"
    edad = 20  
    
  
    app = QApplication(sys.argv)
    
    
    ventana = Ventana(nombre, edad)
    ventana.show()
    
  
    sys.exit(app.exec_())
