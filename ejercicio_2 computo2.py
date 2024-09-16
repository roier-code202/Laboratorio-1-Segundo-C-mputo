import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        
       
        self.setWindowTitle("Ingresar Clave Secreta")
        self.setGeometry(100, 100, 300, 200)
        
        
        self.label = QLabel("Ingresa tu clave secreta:", self)
        
       
        self.clave_secreta = QLineEdit(self)
        self.clave_secreta.setEchoMode(QLineEdit.Password)  
        
        
        self.boton = QPushButton("Confirmar", self)
        self.boton.clicked.connect(self.mostrar_clave)

        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.clave_secreta)
        layout.addWidget(self.boton)

        self.setLayout(layout)
    
    def mostrar_clave(self):
        clave = self.clave_secreta.text()  
        print(f"Clave secreta ingresada: {clave}")  
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    
    
    ventana = Ventana()
    ventana.show()
    
    
    sys.exit(app.exec_())
