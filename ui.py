import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *

class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shape Analysis")
        self.setGeometry(0, 0, 600, 400)

        self.central_widget = QWidget(self)
        self.central_layout = QVBoxLayout(self.central_widget)

        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(self.central_layout)

        self.main_frame = QFrame(self.central_widget)
        self.main_layout = QVBoxLayout(self.main_frame)

        self.input_frame = QFrame(self.main_frame)
        self.input_layout = QGridLayout(self.input_frame)

        self.x_spinbox = QSpinBox(self.input_frame)
        self.x_spinbox.setPrefix("X: ")
        self.x_spinbox.setMinimum(-99)
        self.x_spinbox.setMaximum(99)
        self.input_layout.addWidget(self.x_spinbox, 1, 1, 1, 1)

        self.y_spinbox = QSpinBox(self.input_frame)
        self.y_spinbox.setPrefix("Y: ")
        self.y_spinbox.setMinimum(-99)
        self.y_spinbox.setMaximum(99)
        self.input_layout.addWidget(self.y_spinbox, 3, 1, 1, 1)

        self.add_button = QPushButton(self.input_frame)
        self.add_button.setText("Add")
        self.input_layout.addWidget(self.add_button, 1, 2, 1, 1)

        self.remove_button = QPushButton(self.input_frame)
        self.remove_button.setText("Remove")
        self.input_layout.addWidget(self.remove_button, 3, 2, 1, 1)

        self.clear_button = QPushButton(self.input_frame)
        self.clear_button.setText("Clear")
        self.input_layout.addWidget(self.clear_button, 3, 3, 1, 1)

        self.random_frame = QFrame(self.input_frame)
        self.random_layout = QHBoxLayout(self.random_frame)
        self.random_layout.setContentsMargins(0, 0, 0, 0)

        self.random_button = QPushButton(self.random_frame)
        self.random_button.setText("Random")
        self.random_layout.addWidget(self.random_button)

        self.random_spinbox = QSpinBox(self.random_frame)
        self.random_layout.addWidget(self.random_spinbox)

        self.input_layout.addWidget(self.random_frame, 1, 3, 1, 1)
        self.main_layout.addWidget(self.input_frame)

        self.plot_frame = QFrame(self.main_frame)
        self.plot_layout = QHBoxLayout(self.plot_frame)

        self.plot_table = QTreeWidget(self.plot_frame)
        self.plot_table.headerItem().setText(0, "Points")
        self.plot_layout.addWidget(self.plot_table)

        self.main_layout.addWidget(self.plot_frame)
        self.central_layout.addWidget(self.main_frame)