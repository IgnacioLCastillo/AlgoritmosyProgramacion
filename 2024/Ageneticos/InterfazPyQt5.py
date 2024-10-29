import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Calculator')
        layout = QVBoxLayout()

        self.num1 = QLineEdit(self)
        self.num2 = QLineEdit(self)
        self.result = QLabel('Result:', self)

        layout.addWidget(self.num1)
        layout.addWidget(self.num2)
        layout.addWidget(self.result)

        self.add_button = QPushButton('Add', self)
        self.sub_button = QPushButton('Subtract', self)
        self.mul_button = QPushButton('Multiply', self)
        self.div_button = QPushButton('Divide', self)

        self.add_button.clicked.connect(self.add)
        self.sub_button.clicked.connect(self.subtract)
        self.mul_button.clicked.connect(self.multiply)
        self.div_button.clicked.connect(self.divide)

        layout.addWidget(self.add_button)
        layout.addWidget(self.sub_button)
        layout.addWidget(self.mul_button)
        layout.addWidget(self.div_button)

        self.setLayout(layout)

    def add(self):
        num1 = float(self.num1.text())
        num2 = float(self.num2.text())
        self.result.setText(f'Result: {num1 + num2}')

    def subtract(self):
        num1 = float(self.num1.text())
        num2 = float(self.num2.text())
        self.result.setText(f'Result: {num1 - num2}')

    def multiply(self):
        num1 = float(self.num1.text())
        num2 = float(self.num2.text())
        self.result.setText(f'Result: {num1 * num2}')

    def divide(self):
        num1 = float(self.num1.text())
        num2 = float(self.num2.text())
        if num2 != 0:
            self.result.setText(f'Result: {num1 / num2}')
        else:
            self.result.setText('Error: Division by zero')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
