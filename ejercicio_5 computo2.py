import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QFormLayout

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        
        
        self.setWindowTitle("Ingreso de Datos Personales")
        self.setGeometry(100, 100, 500, 600)
        
      
        layout = QFormLayout()
        
       
        self.input_nombre = QLineEdit(self)
        self.input_edad = QLineEdit(self)
        self.input_direccion = QLineEdit(self)
        self.input_correo = QLineEdit(self)
        self.input_telefono = QLineEdit(self)
        self.input_ocupacion = QLineEdit(self)
        self.input_genero = QLineEdit(self)
        self.input_estado_civil = QLineEdit(self)
        self.input_nacionalidad = QLineEdit(self)
        self.input_identificacion = QLineEdit(self)

        
        layout.addRow("Nombre Completo:", self.input_nombre)
        layout.addRow("Edad:", self.input_edad)
        layout.addRow("Dirección:", self.input_direccion)
        layout.addRow("Correo Electrónico:", self.input_correo)
        layout.addRow("Teléfono:", self.input_telefono)
        layout.addRow("Ocupación:", self.input_ocupacion)
        layout.addRow("Género:", self.input_genero)
        layout.addRow("Estado Civil:", self.input_estado_civil)
        layout.addRow("Nacionalidad:", self.input_nacionalidad)
        layout.addRow("Número de Identificación:", self.input_identificacion)
        
       
        self.boton = QPushButton("Confirmar", self)
        self.boton.clicked.connect(self.mostrar_datos)
        
        
        layout.addRow(self.boton)

        
        self.setLayout(layout)

    def mostrar_datos(self):
       
        nombre = self.input_nombre.text()
        edad = self.input_edad.text()
        direccion = self.input_direccion.text()
        correo = self.input_correo.text()
        telefono = self.input_telefono.text()
        ocupacion = self.input_ocupacion.text()
        genero = self.input_genero.text()
        estado_civil = self.input_estado_civil.text()
        nacionalidad = self.input_nacionalidad.text()
        identificacion = self.input_identificacion.text()

        
        print("Datos Personales Ingresados:")
        print(f"Nombre Completo: {nombre}")
        print(f"Edad: {edad}")
        print(f"Dirección: {direccion}")
        print(f"Correo Electrónico: {correo}")
        print(f"Teléfono: {telefono}")
        print(f"Ocupación: {ocupacion}")
        print(f"Género: {genero}")
        print(f"Estado Civil: {estado_civil}")
        print(f"Nacionalidad: {nacionalidad}")
        print(f"Número de Identificación: {identificacion}")

if __name__ == "__main__":
  
    app = QApplication(sys.argv)
    
   
    ventana = Ventana()
    ventana.show()
    
    
    sys.exit(app.exec_())
