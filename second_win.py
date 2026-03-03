from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout, QGridLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)

from instr import *
from final_win import *
from my_app import transactions_db


class Experiment():
   def __init__(self, user_id, first_name, last_name):
       self.user_id = user_id
       self.first_name = first_name
       self.last_name = last_name


class TestWin(QWidget):
   def __init__(self, user_id, first_name, last_name):
       super().__init__()
       self.user_id = user_id
       self.first_name = first_name
       self.last_name = last_name
       self.exp = Experiment(user_id, first_name, last_name)
       self.set_appear()
       self.initUI()
       self.connects()
       self.show()

   def set_appear(self):
       self.setWindowTitle(txt_menu_title)
       self.resize(win_width, win_height)
       self.move(win_x, win_y)

   def initUI(self):
       # Estilo neón
       self.setStyleSheet(f"""
           QWidget {{
               background-color: {NEON_BG};
               color: {NEON_TEXT};
               font-family: 'Segoe UI', Arial;
           }}
           QLabel {{
               background: transparent;
           }}
           QPushButton {{
               border-radius: 15px;
               padding: 20px;
               font-weight: bold;
               font-size: 16px;
           }}
       """)

       # Título de bienvenida
       welcome = QLabel(f"¡Hola, {self.first_name}!")
       welcome.setFont(QFont("Segoe UI", 28, QFont.Bold))
       welcome.setStyleSheet(f"color: {NEON_CYAN};")
       welcome.setAlignment(Qt.AlignCenter)

       question = QLabel(txt_welcome)
       question.setFont(QFont("Segoe UI", 16))
       question.setStyleSheet(f"color: {NEON_TEXT_DIM};")
       question.setAlignment(Qt.AlignCenter)

       # Botones del menú con colores neón
       self.btn_new = QPushButton("💸\n" + txt_new_transaction)
       self.btn_new.setStyleSheet(f"""
           QPushButton {{
               background-color: {NEON_PANEL};
               border: 3px solid {NEON_GREEN};
               color: {NEON_GREEN};
               min-height: 120px;
           }}
           QPushButton:hover {{
               background-color: {NEON_GREEN};
               color: {NEON_BG};
           }}
       """)

       self.btn_history = QPushButton("📊\n" + txt_view_history)
       self.btn_history.setStyleSheet(f"""
           QPushButton {{
               background-color: {NEON_PANEL};
               border: 3px solid {NEON_CYAN};
               color: {NEON_CYAN};
               min-height: 120px;
           }}
           QPushButton:hover {{
               background-color: {NEON_CYAN};
               color: {NEON_BG};
           }}
       """)

       self.btn_balance = QPushButton("💰\n" + txt_view_balance)
       self.btn_balance.setStyleSheet(f"""
           QPushButton {{
               background-color: {NEON_PANEL};
               border: 3px solid {NEON_YELLOW};
               color: {NEON_YELLOW};
               min-height: 120px;
           }}
           QPushButton:hover {{
               background-color: {NEON_YELLOW};
               color: {NEON_BG};
           }}
       """)

       self.btn_logout = QPushButton("🚪\n" + txt_logout)
       self.btn_logout.setStyleSheet(f"""
           QPushButton {{
               background-color: {NEON_PANEL};
               border: 3px solid {NEON_PINK};
               color: {NEON_PINK};
               min-height: 100px;
           }}
           QPushButton:hover {{
               background-color: {NEON_PINK};
               color: {NEON_BG};
           }}
       """)

       # Layout
       self.layout = QVBoxLayout()
       self.layout.setSpacing(20)
       self.layout.addWidget(welcome)
       self.layout.addWidget(question)
       self.layout.addWidget(self.btn_new)
       self.layout.addWidget(self.btn_history)
       self.layout.addWidget(self.btn_balance)
       self.layout.addWidget(self.btn_logout)
       
       self.setLayout(self.layout)

   def next_click(self):
       self.hide()
       self.fw = FinalWin(self.exp, mode="transaction")

   def history_click(self):
       self.hide()
       self.fw = FinalWin(self.exp, mode="history")

   def balance_click(self):
       self.hide()
       self.fw = FinalWin(self.exp, mode="balance")

   def logout_click(self):
       self.hide()
       from my_app import MainWin
       self.mw = MainWin()

   def connects(self):
       self.btn_new.clicked.connect(self.next_click)
       self.btn_history.clicked.connect(self.history_click)
       self.btn_balance.clicked.connect(self.balance_click)
       self.btn_logout.clicked.connect(self.logout_click)