import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QRadioButton, QVBoxLayout, QPushButton, QSpinBox, QHBoxLayout, QGroupBox

class Ventana(QWidget):
    def __init__(self):
        super().__init__()

        
        self.setWindowTitle("Formulario de Datos")
        self.setGeometry(100, 100, 400, 300)

        
        self.label_edad = QLabel("Edad:")
        self.spinbox_edad = QSpinBox(self)
        self.spinbox_edad.setRange(1, 100)  

        
        self.groupbox_genero = QGroupBox("Selecciona tu género:")
        self.radio_hombre = QRadioButton("Hombre", self)
        self.radio_mujer = QRadioButton("Mujer", self)
        self.radio_otro = QRadioButton("Otro", self)

        
        vbox_radio = QVBoxLayout()
        vbox_radio.addWidget(self.radio_hombre)
        vbox_radio.addWidget(self.radio_mujer)
        vbox_radio.addWidget(self.radio_otro)
        self.groupbox_genero.setLayout(vbox_radio)

        
        self.boton_confirmar = QPushButton("Confirmar", self)
        self.boton_confirmar.clicked.connect(self.mostrar_datos)

        
        layout = QVBoxLayout()
        layout.addWidget(self.label_edad)
        layout.addWidget(self.spinbox_edad)
        layout.addWidget(self.groupbox_genero)
        layout.addWidget(self.boton_confirmar)

        self.setLayout(layout)

    def mostrar_datos(self):
        
        edad = self.spinbox_edad.value()

        
        genero = ""
        if self.radio_hombre.isChecked():
            genero = "Hombre"
        elif self.radio_mujer.isChecked():
            genero = "Mujer"
        elif self.radio_otro.isChecked():
            genero = "Otro"

       
        print(f"Edad: {edad}")
        print(f"Género: {genero}")

if __name__ == "__main__":
  
    app = QApplication(sys.argv)

    
    ventana = Ventana()
    ventana.show()

 
    sys.exit(app.exec_())


#Este programa es un formulario simple donde el usuario ingresa la edad usando un SpinBox y seleccionar
#  su género utilizando RadioBox. Cuando el usuario presiona el botón "Confirmar",
#  se muestran los datos ingresados en la consola.

#¿Cuál es el problema que resuelve?
#Este tipo de interfaz gráfica puede ser útil para cualquier formulario o encuesta que requiera recopilar 
# información básica sobre un individuo, como su edad y género, de una manera fácil y amigable. Los widgets
# facilitan la introducción de datos de manera interactiva y visualmente clara, evitando errores de entrada 
# y garantizando que el usuario seleccione solo una opción de género y edad dentro del rango permitido.