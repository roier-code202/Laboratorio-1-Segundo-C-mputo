import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QFormLayout

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        
        
        self.setWindowTitle("Ingreso de Datos de Mascotas")
        self.setGeometry(100, 100, 400, 400)
        
        
        layout = QFormLayout()
        
        
        self.label_mascota1 = QLabel("Mascota 1:")
        self.input_nombre1 = QLineEdit(self)
        self.input_edad1 = QLineEdit(self)
        self.input_tipo1 = QLineEdit(self)
        
        layout.addRow("Nombre Mascota 1:", self.input_nombre1)
        layout.addRow("Edad Mascota 1:", self.input_edad1)
        layout.addRow("Tipo Mascota 1:", self.input_tipo1)

        
        self.label_mascota2 = QLabel("Mascota 2:")
        self.input_nombre2 = QLineEdit(self)
        self.input_edad2 = QLineEdit(self)
        self.input_tipo2 = QLineEdit(self)
        
        layout.addRow("Nombre Mascota 2:", self.input_nombre2)
        layout.addRow("Edad Mascota 2:", self.input_edad2)
        layout.addRow("Tipo Mascota 2:", self.input_tipo2)

      
        self.label_mascota3 = QLabel("Mascota 3:")
        self.input_nombre3 = QLineEdit(self)
        self.input_edad3 = QLineEdit(self)
        self.input_tipo3 = QLineEdit(self)
        
        layout.addRow("Nombre Mascota 3:", self.input_nombre3)
        layout.addRow("Edad Mascota 3:", self.input_edad3)
        layout.addRow("Tipo Mascota 3:", self.input_tipo3)
        
       
        self.boton = QPushButton("Confirmar", self)
        self.boton.clicked.connect(self.mostrar_datos)
        
        layout.addRow(self.boton)

        
        self.setLayout(layout)

    def mostrar_datos(self):
        
        nombre1 = self.input_nombre1.text()
        edad1 = self.input_edad1.text()
        tipo1 = self.input_tipo1.text()
        
        nombre2 = self.input_nombre2.text()
        edad2 = self.input_edad2.text()
        tipo2 = self.input_tipo2.text()
        
        nombre3 = self.input_nombre3.text()
        edad3 = self.input_edad3.text()
        tipo3 = self.input_tipo3.text()
        
        
        print("Datos de las mascotas:")
        print(f"Mascota 1: Nombre: {nombre1}, Edad: {edad1}, Tipo: {tipo1}")
        print(f"Mascota 2: Nombre: {nombre2}, Edad: {edad2}, Tipo: {tipo2}")
        print(f"Mascota 3: Nombre: {nombre3}, Edad: {edad3}, Tipo: {tipo3}")

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    
   
    ventana = Ventana()
    ventana.show()
    
   
    sys.exit(app.exec_())
