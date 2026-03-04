import json

from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import (
        QApplication, QWidget,
        QHBoxLayout, QVBoxLayout, QGridLayout,
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit,
        QSpinBox, QMessageBox, QFrame)

from instr import *
from second_win import TestWin,Experiment

# Base de datos
users_db = json.load(open("data/users_db.json", 'r'))
transactions_db = json.load(open("data/transactions_db.json", 'r'))

class MainWin(QWidget):
    def __init__(self):
        users_db = json.load(open("data/users_db.json", 'r'))
        transactions_db = json.load(open("data/transactions_db.json", 'r'))

        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def initUI(self):
        # Frame principal con estilo neón
        self.setStyleSheet(f"""
            QWidget {{
                background-color: {NEON_BG};
                color: {NEON_TEXT};
                font-family: 'Segoe UI', Arial;
            }}
            QLabel {{
                color: {NEON_TEXT};
                background: transparent;
            }}
            QLineEdit {{
                background-color: {NEON_PANEL};
                border: 2px solid {NEON_CYAN};
                border-radius: 10px;
                padding: 12px;
                color: {NEON_TEXT};
                font-size: 14px;
            }}
            QLineEdit:focus {{
                border: 2px solid {NEON_PINK};
            }}
            QPushButton {{
                background-color: {NEON_PANEL};
                border: 2px solid {NEON_CYAN};
                border-radius: 10px;
                padding: 15px 30px;
                color: {NEON_CYAN};
                font-weight: bold;
                font-size: 14px;
            }}
            QPushButton:hover {{
                background-color: {NEON_CYAN};
                color: {NEON_BG};
            }}
            QSpinBox {{
                background-color: {NEON_PANEL};
                border: 2px solid {NEON_PINK};
                border-radius: 8px;
                padding: 10px;
                color: {NEON_TEXT};
                font-size: 18px;
            }}
        """)

        # Título neón
        self.hello_text = QLabel("💰 EconomiK")
        self.hello_text.setFont(QFont("Segoe UI", 32, QFont.Bold))
        self.hello_text.setStyleSheet(f"color: {NEON_CYAN};")
        self.hello_text.setAlignment(Qt.AlignCenter)

        # Subtítulo
        self.subtitle = QLabel("Sistema de Gestión Monetaria")
        self.subtitle.setFont(QFont("Segoe UI", 14))
        self.subtitle.setStyleSheet(f"color: {NEON_PINK};")
        self.subtitle.setAlignment(Qt.AlignCenter)

        # Frame del formulario
        form_frame = QFrame()
        form_frame.setStyleSheet(f"""
            QFrame {{
                background-color: {NEON_PANEL};
                border-radius: 20px;
                border: 2px solid {NEON_PURPLE};
            }}
        """)
        form_layout = QVBoxLayout(form_frame)
        form_layout.setSpacing(15)
        form_layout.setContentsMargins(30, 30, 30, 30)

        # Campos
        self.text_name = QLabel(txt_name)
        self.text_name.setStyleSheet(f"color: {NEON_CYAN}; font-weight: bold;")
        self.line_name = QLineEdit(txt_hintname)

        self.text_lastname = QLabel(txt_lastname)
        self.text_lastname.setStyleSheet(f"color: {NEON_CYAN}; font-weight: bold;")
        self.line_lastname = QLineEdit(txt_hintlastname)

        self.text_pin = QLabel(txt_pin)
        self.text_pin.setStyleSheet(f"color: {NEON_PINK}; font-weight: bold;")

        # PIN digits
        pin_container = QHBoxLayout()
        pin_container.setSpacing(10)
        self.pin_digits = []
        for i in range(4):
            spin = QSpinBox()
            spin.setRange(0, 9)
            spin.setWrapping(True)
            spin.setAlignment(Qt.AlignCenter)
            spin.setFixedSize(60, 60)
            spin.setStyleSheet(f"""
                QSpinBox {{
                    background-color: {NEON_BG};
                    border: 3px solid {NEON_PINK};
                    border-radius: 10px;
                    color: {NEON_PINK};
                    font-size: 24px;
                    font-weight: bold;
                }}
                QSpinBox:focus {{
                    border: 3px solid {NEON_CYAN};
                    color: {NEON_CYAN};
                }}
            """)
            self.pin_digits.append(spin)
            pin_container.addWidget(spin)

        pin_widget = QWidget()
        pin_widget.setLayout(pin_container)

        # Botones
        self.btn_login = QPushButton("🚀 " + txt_next)
        self.btn_login.setStyleSheet(f"""
            QPushButton {{
                background-color: {NEON_GREEN};
                color: {NEON_BG};
                border: none;
                font-size: 16px;
            }}
            QPushButton:hover {{
                background-color: {NEON_CYAN};
            }}
        """)

        self.btn_register = QPushButton("📝 " + txt_register)
        self.btn_register.setStyleSheet(f"""
            QPushButton {{
                background-color: {NEON_PURPLE};
                color: {NEON_TEXT};
                border: none;
                font-size: 16px;
            }}
            QPushButton:hover {{
                background-color: {NEON_PINK};
            }}
        """)

        # Agregar al formulario
        form_layout.addWidget(self.text_name)
        form_layout.addWidget(self.line_name)
        form_layout.addWidget(self.text_lastname)
        form_layout.addWidget(self.line_lastname)
        form_layout.addWidget(self.text_pin)
        form_layout.addWidget(pin_widget, alignment=Qt.AlignCenter)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.btn_login)
        btn_layout.addWidget(self.btn_register)
        form_layout.addLayout(btn_layout)

        # Layout principal
        self.layout = QVBoxLayout()
        self.layout.setSpacing(20)
        self.layout.addStretch()
        self.layout.addWidget(self.hello_text)
        self.layout.addWidget(self.subtitle)
        self.layout.addWidget(form_frame)
        self.layout.addStretch()

        self.setLayout(self.layout)

    def get_pin(self):
        return "".join(str(digit.value()) for digit in self.pin_digits)

    def next_click(self):
        first = self.line_name.text().strip()
        last = self.line_lastname.text().strip()
        pin = self.get_pin()

        if not all([first, last, pin]):
            QMessageBox.warning(self, "Error", "Complete todos los campos")
            return

        user_id = f"{first.lower()}_{last.lower()}"

        if user_id in users_db and users_db[user_id]["pin"] == pin:
            self.hide()

            self.tw = TestWin(user_id, first, last)
        else:
            QMessageBox.warning(self, "Error", "Credenciales incorrectas")

    def register_click(self):
        first = self.line_name.text().strip()
        last = self.line_lastname.text().strip()
        pin = self.get_pin()

        if not all([first, last, pin]):
            QMessageBox.warning(self, "Error", "Complete todos los campos")
            return

        if len(pin) != 4 or not pin.isdigit():
            QMessageBox.warning(self, "Error", "PIN debe ser 4 dígitos")
            return

        user_id = f"{first.lower()}_{last.lower()}"

        if user_id in users_db:
            QMessageBox.warning(self, "Error", "Usuario ya existe")
            return

        users_db[user_id] = {
            "first_name": first,
            "last_name": last,
            "pin": pin
        }
        transactions_db[user_id] = []

        json.dump(users_db, open("data/users_db.json", 'w'))
        json.dump(transactions_db, open("data/transactions_db.json", 'w'))

        QMessageBox.information(self, "Éxito", "Usuario registrado")
        self.line_name.clear()
        self.line_lastname.clear()
        for digit in self.pin_digits:
            digit.setValue(0)

    def connects(self):
        self.btn_login.clicked.connect(self.next_click)
        self.btn_register.clicked.connect(self.register_click)

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)


def main():
    app = QApplication([])
    app.setStyle('Fusion')
    mw = MainWin()
    app.exec_()


if __name__ == "__main__":
    main()