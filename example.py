# Accessing the module QtWidgets from the PyQt6 library and the module has
# several classes like QApplication, QVBoxLayout
from PyQt6.QtWidgets import (QApplication, QLabel, QWidget,
                             QGridLayout, QLineEdit, QPushButton)

# sys is a standard library in python, it's the short form of system. It provides various functionalities for input and
# output
import sys
from datetime import datetime

# Why do we inherit from QWidget class?
# Because QWidget is a class which creates windows
class AgeCalculator(QWidget):
    def __init__(self):
        # super is a function which returns the parent of the class.
        super().__init__()
        self.setWindowTitle("Age Calculator")
        grid = QGridLayout()  # GridLayout is an invisible widget, but all the widgets have to added to that grid

        # Create Widgets
        name_label = QLabel("Name:")
        self.name_line_edit = QLineEdit()

        date_birth_label = QLabel("Date of Birth MM/DD/YYYY:")
        self.date_birth_line_edit = QLineEdit()

        calculate_button = QPushButton("Calculate Age")
        calculate_button.clicked.connect(self.calculate_age)
        self.output_label = QLabel()

        # Add widgets to grid
        grid.addWidget(name_label, 0, 0)    # addWidget is a method of the QGridLayout instance
        grid.addWidget(self.name_line_edit, 0, 1)    # addWidget is a method of the QGridLayout instance
        grid.addWidget(date_birth_label, 1, 0)    # addWidget is a method of the QGridLayout instance
        grid.addWidget(self.date_birth_line_edit, 1, 1)    # addWidget is a method of the QGridLayout instance
        grid.addWidget(calculate_button, 2, 0, 1, 2)    # addWidget is a method of the QGridLayout instance
        grid.addWidget(self.output_label, 3, 0, 1, 2)    # addWidget is a method of the QGridLayout instance

        # setLayout method is inherited from QWidget
        self.setLayout(grid)

    def calculate_age(self):
        current_year = datetime.now().year
        date_of_birth = self.date_birth_line_edit.text()
        year_of_birth = datetime.strptime(date_of_birth, "%m/%d/%Y").date().year
        age = current_year - year_of_birth
        self.output_label.setText(f"{self.name_line_edit.text()} is {age} years old.")

app = QApplication(sys.argv)
# Constructing QWidget AgeCalculator which is a child of QWidget
age_calculator = AgeCalculator()
age_calculator.show()
sys.exit(app.exec())