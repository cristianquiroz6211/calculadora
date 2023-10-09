import sys
from conversor import Operaciones
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import math
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

""" Saque la calculadora base de https://github.com/yogeshsinghgit/PYQt5-calculator
Se añade los nuevos bloques y labels para poder llamar al conversor e imprimir en  texto
 """




class Example(QWidget):
    def __init__(self):
        
        super().__init__()
        self.setFixedSize(400, 350)
        self.operaciones = Operaciones()  # Instancia de la clase Operaciones
        self.title = 'Calculadora poo'
        self.left = 100
        self.top = 100
        self.width = 320
        self.height = 200
        self.initUI()

    def initUI(self):
        self.current = ''

        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon('cal.svg'))
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Establecer el ícono
        self.setWindowIcon(QIcon('cal.svg'))

        self.show()
        frame = QVBoxLayout()
        
        self.display = QLineEdit('0')
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(21)
        font = self.display.font()
        font.setPointSize(font.pointSize() + 8)
        self.display.setFont(font)
        
        self.textDisplay = QLineEdit('Resultado en texto')
        self.textDisplay.setReadOnly(True)
        self.textDisplay.setAlignment(Qt.AlignCenter)
        font = self.textDisplay.font()
        font.setPointSize(font.pointSize() + 6)
        self.textDisplay.setFont(font)

        frame.addWidget(self.display)
        frame.addWidget(self.textDisplay)
        
        grid = QGridLayout()
        grid.setSpacing(5)
        frame.addLayout(grid)
        self.setLayout(frame)        

        names = ['Cls', 'Bck', 'Close', u"\N{DIVISION SIGN}",
                 '7', '8', '9', u"\N{MULTIPLICATION SIGN}",
                 '4', '5', '6', '-',
                 '1', '2', '3', '+',
                 '0', '00', '.', '=',
                 'sin', 'cos', 'tan',
                 'max', 'min', 'media', ',']

        positions = [(i, j) for i in range(7) for j in range(4)]
        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            button.resize(10, 10)
            button.clicked.connect(self.press_btn)
            grid.addWidget(button, *position)
    def press_btn(self):
        button_text = self.sender().text()
        result_num = None

        if self.display.text().isalpha():  # Si el resultado anterior fue una palabra
            if button_text in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
                self.current = ''  # Reinicia la pantalla si se presiona un número o punto después de una palabra

        # Operaciones básicas
        if button_text == '=':
            try:
                # Realiza la operación y obtiene el resultado numérico
                result_num = eval(self.current.replace(u"\N{DIVISION SIGN}",'/').replace(u"\N{MULTIPLICATION SIGN}","*"))
                self.current = str(result_num)
                self.display.setText(self.current)
            except Exception as e:
                QMessageBox.about(self, 'Calculator says', 'You passed a wrong expression: ' + str(e))

        # Funciones trigonométricas
        elif button_text in ['sin', 'cos', 'tan']:
            try:
                valor = float(self.current)
                if button_text == 'sin':
                    result_num = math.sin(math.radians(valor))
                    self.current = str(result_num)
                elif button_text == 'cos':
                    result_num = math.cos(math.radians(valor))
                    self.current = str(result_num)
                else:
                    result_num = math.tan(math.radians(valor))
                    self.current = str(result_num)
                self.display.setText(self.current)
            except Exception as e:
                QMessageBox.about(self, 'Calculator says', 'Error in trigonometric calculation: ' + str(e))

        # Operaciones de media, maximo y minimo
        elif button_text in ['media', 'max', 'min']:
            try:
                valores = [float(val) for val in self.current.split(',')]
                if button_text == 'media':
                    self.current = str(sum(valores) / len(valores))
                    result_num = float(self.current)
                elif button_text == 'max':
                    self.current = str(max(valores))
                    result_num = float(self.current)
                elif button_text == 'min':
                    self.current = str(min(valores))
                    result_num = float(self.current)
                self.display.setText(self.current)
            except Exception as e:
                QMessageBox.about(self, 'Error, cuidado ' + str(e))

            # Botones especiales
        elif button_text == 'Cls':
            self.current = ''
            self.textDisplay.clear()  # Limpia la ventana de texto
        elif button_text == 'Bck':
            self.current = self.current[:-1]
            # Si después de eliminar un carácter la entrada está vacía, limpiamos la ventana de texto
            if not self.current:
                self.textDisplay.clear()
        elif button_text == 'Close':
            self.close()        # Resto de los botones
        else:
            self.current += button_text
        self.display.setText(self.current)

        # Actualizar el display de texto después de cada operación
        if result_num is None:
            try:
                result_num = float(self.current)
            except:
                pass

        if result_num is not None:
            self.textDisplay.setText(self.operaciones.convertidor.convertir(result_num))
        else:
            self.textDisplay.clear()  # Si no hay un número válido, limpiamos la ventana de texto






if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
