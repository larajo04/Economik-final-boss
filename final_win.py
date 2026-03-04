import json

from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import (
        QApplication, QWidget,
        QHBoxLayout, QVBoxLayout, QGridLayout,
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit,
        QComboBox, QDoubleSpinBox, QTableWidget, QTableWidgetItem,
        QHeaderView, QMessageBox, QFrame, QTabWidget)

from instr import *
transactions_db = json.load(open("data/transactions_db.json", 'r'))

class FinalWin(QWidget):
    def __init__(self, exp, mode="transaction"):
        super().__init__()
        self.exp = exp
        self.mode = mode
        self.user_id = exp.user_id
        self.set_appear()
        self.initUI()
        self.show()

    def set_appear(self):
        if self.mode == "transaction":
            self.setWindowTitle(txt_transaction_title)
        elif self.mode == "history":
            self.setWindowTitle(txt_history_title)
        else:
            self.setWindowTitle(txt_balance_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        # Estilo base neón
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
                border-radius: 10px;
                padding: 12px 24px;
                font-weight: bold;
            }}
            QComboBox {{
                background-color: {NEON_PANEL};
                border: 2px solid {NEON_CYAN};
                border-radius: 8px;
                padding: 10px;
                color: {NEON_TEXT};
            }}
            QDoubleSpinBox {{
                background-color: {NEON_PANEL};
                border: 2px solid {NEON_GREEN};
                border-radius: 8px;
                padding: 10px;
                color: {NEON_TEXT};
            }}
            QLineEdit {{
                background-color: {NEON_PANEL};
                border: 2px solid {NEON_PURPLE};
                border-radius: 8px;
                padding: 10px;
                color: {NEON_TEXT};
            }}
            QTableWidget {{
                background-color: {NEON_PANEL};
                border: 2px solid {NEON_CYAN};
                border-radius: 10px;
                color: {NEON_TEXT};
                gridline-color: {NEON_ACCENT};
            }}
            QHeaderView::section {{
                background-color: {NEON_CYAN};
                color: {NEON_BG};
                padding: 10px;
                font-weight: bold;
            }}
        """)

        if self.mode == "transaction":
            self.init_transaction_ui()
        elif self.mode == "history":
            self.init_history_ui()
        else:
            self.init_balance_ui()

    def init_transaction_ui(self):
        # Título
        title = QLabel("💸 " + txt_transaction_title)
        title.setFont(QFont("Segoe UI", 24, QFont.Bold))
        title.setStyleSheet(f"color: {NEON_GREEN};")
        title.setAlignment(Qt.AlignCenter)

        # Frame del formulario
        form_frame = QFrame()
        form_frame.setStyleSheet(f"""
            QFrame {{
                background-color: {NEON_PANEL};
                border-radius: 20px;
                border: 2px solid {NEON_GREEN};
            }}
        """)
        form_layout = QVBoxLayout(form_frame)
        form_layout.setSpacing(15)
        form_layout.setContentsMargins(30, 30, 30, 30)

        # Tipo de operación
        type_label = QLabel(txt_type)
        type_label.setStyleSheet(f"color: {NEON_CYAN}; font-weight: bold; font-size: 14px;")
        
        self.combo_type = QComboBox()
        self.combo_type.addItems([txt_send, txt_receive])
        self.combo_type.setStyleSheet(f"""
            QComboBox {{
                background-color: {NEON_BG};
                border: 2px solid {NEON_PINK};
                color: {NEON_PINK};
                font-size: 14px;
            }}
        """)

        # Moneda (solo Bs y $)
        currency_label = QLabel(txt_currency)
        currency_label.setStyleSheet(f"color: {NEON_CYAN}; font-weight: bold; font-size: 14px;")
        
        self.combo_currency = QComboBox()
        self.combo_currency.addItems([CURRENCY_BSF, CURRENCY_USD])
        self.combo_currency.setStyleSheet(f"""
            QComboBox {{
                background-color: {NEON_BG};
                border: 2px solid {NEON_YELLOW};
                color: {NEON_YELLOW};
                font-size: 14px;
            }}
        """)

        # Monto
        amount_label = QLabel(txt_amount)
        amount_label.setStyleSheet(f"color: {NEON_CYAN}; font-weight: bold; font-size: 14px;")
        
        self.spin_amount = QDoubleSpinBox()
        self.spin_amount.setRange(0, 999999999)
        self.spin_amount.setDecimals(2)
        self.spin_amount.setValue(0)
        self.spin_amount.setStyleSheet(f"""
            QDoubleSpinBox {{
                background-color: {NEON_BG};
                border: 2px solid {NEON_GREEN};
                color: {NEON_GREEN};
                font-size: 16px;
            }}
        """)

        # Descripción (opcional, sin contraparte)
        desc_label = QLabel(txt_description)
        desc_label.setStyleSheet(f"color: {NEON_CYAN}; font-weight: bold; font-size: 14px;")
        
        self.line_description = QLineEdit()
        self.line_description.setPlaceholderText("Ej: Compra de víveres, Pago de servicios, etc.")

        # Info de tasa BCV
        rate_info = QLabel(f"📊 {txt_bcv_rate}")
        rate_info.setStyleSheet(f"color: {NEON_TEXT_DIM}; font-size: 12px;")
        rate_info.setAlignment(Qt.AlignCenter)

        # Botones
        self.btn_save = QPushButton("💾 " + txt_save)
        self.btn_save.setStyleSheet(f"""
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

        self.btn_back = QPushButton("← " + txt_back)
        self.btn_back.setStyleSheet(f"""
            QPushButton {{
                background-color: {NEON_PANEL};
                color: {NEON_TEXT};
                border: 2px solid {NEON_PINK};
            }}
            QPushButton:hover {{
                background-color: {NEON_PINK};
                color: {NEON_BG};
            }}
        """)

        # Agregar a formulario
        form_layout.addWidget(type_label)
        form_layout.addWidget(self.combo_type)
        form_layout.addWidget(currency_label)
        form_layout.addWidget(self.combo_currency)
        form_layout.addWidget(amount_label)
        form_layout.addWidget(self.spin_amount)
        form_layout.addWidget(desc_label)
        form_layout.addWidget(self.line_description)
        form_layout.addWidget(rate_info)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.btn_back)
        btn_layout.addWidget(self.btn_save)
        form_layout.addLayout(btn_layout)

        # Layout principal
        self.layout = QVBoxLayout()
        self.layout.setSpacing(20)
        self.layout.addWidget(title)
        self.layout.addWidget(form_frame)
        
        self.setLayout(self.layout)

        self.btn_save.clicked.connect(self.save_transaction)
        self.btn_back.clicked.connect(self.back_to_menu)

    def init_history_ui(self):
        # Título
        title = QLabel("📊 " + txt_history_title)
        title.setFont(QFont("Segoe UI", 24, QFont.Bold))
        title.setStyleSheet(f"color: {NEON_CYAN};")
        title.setAlignment(Qt.AlignCenter)

        # Filtros
        filter_frame = QFrame()
        filter_frame.setStyleSheet(f"""
            QFrame {{
                background-color: {NEON_PANEL};
                border-radius: 10px;
                padding: 10px;
            }}
        """)
        filter_layout = QHBoxLayout(filter_frame)

        self.combo_filter_type = QComboBox()
        self.combo_filter_type.addItems([txt_all, txt_send_filter, txt_receive_filter])
        self.combo_filter_type.currentTextChanged.connect(self.load_history)

        self.combo_filter_currency = QComboBox()
        self.combo_filter_currency.addItem(txt_all_currencies)
        self.combo_filter_currency.addItems([CURRENCY_BSF, CURRENCY_USD])
        self.combo_filter_currency.currentTextChanged.connect(self.load_history)

        filter_layout.addWidget(QLabel("Tipo:"))
        filter_layout.addWidget(self.combo_filter_type)
        filter_layout.addStretch()
        filter_layout.addWidget(QLabel("Moneda:"))
        filter_layout.addWidget(self.combo_filter_currency)

        # Tabla
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Tipo", "Monto", "Moneda", "Descripción"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Botón volver
        self.btn_back = QPushButton("← " + txt_back)
        self.btn_back.setStyleSheet(f"""
            QPushButton {{
                background-color: {NEON_PANEL};
                color: {NEON_TEXT};
                border: 2px solid {NEON_PINK};
            }}
            QPushButton:hover {{
                background-color: {NEON_PINK};
                color: {NEON_BG};
            }}
        """)

        self.layout = QVBoxLayout()
        self.layout.addWidget(title)
        self.layout.addWidget(filter_frame)
        self.layout.addWidget(self.table)
        self.layout.addWidget(self.btn_back)

        self.setLayout(self.layout)

        self.load_history()
        self.btn_back.clicked.connect(self.back_to_menu)

    def init_balance_ui(self):
        # Título
        title = QLabel("💰 " + txt_balance_title)
        title.setFont(QFont("Segoe UI", 24, QFont.Bold))
        title.setStyleSheet(f"color: {NEON_YELLOW};")
        title.setAlignment(Qt.AlignCenter)

        # Info BCV
        bcv_label = QLabel(f"📈 {txt_bcv_rate}")
        bcv_label.setStyleSheet(f"color: {NEON_CYAN}; font-size: 14px;")
        bcv_label.setAlignment(Qt.AlignCenter)

        # Calcular saldos
        balance = self.calculate_balance()
        
        self.layout = QVBoxLayout()
        self.layout.addWidget(title)
        self.layout.addWidget(bcv_label)

        if not balance:
            no_data = QLabel("No hay movimientos registrados")
            no_data.setAlignment(Qt.AlignCenter)
            no_data.setStyleSheet(f"color: {NEON_TEXT_DIM}; font-size: 16px;")
            self.layout.addWidget(no_data)
        else:
            total_rec = 0
            total_sent = 0
            
            for currency, amount in sorted(balance.items()):
                frame = QFrame()
                frame.setStyleSheet(f"""
                    QFrame {{
                        background-color: {NEON_PANEL};
                        border-radius: 15px;
                        border: 3px solid {NEON_CYAN if amount >= 0 else NEON_PINK};
                    }}
                """)
                frame_layout = QHBoxLayout(frame)
                frame_layout.setContentsMargins(20, 20, 20, 20)

                # Icono según moneda
                icon = "🇻🇪" if "Bolívar" in currency else "💵"
                
                curr_label = QLabel(f"{icon} {currency}")
                curr_label.setFont(QFont("Segoe UI", 18, QFont.Bold))
                curr_label.setStyleSheet(f"color: {NEON_CYAN};")

                amount_label = QLabel(f"{amount:,.2f}")
                amount_label.setFont(QFont("Segoe UI", 24, QFont.Bold))
                
                if amount > 0:
                    amount_label.setStyleSheet(f"color: {NEON_GREEN};")
                    total_rec += amount
                elif amount < 0:
                    amount_label.setStyleSheet(f"color: {NEON_PINK};")
                    total_sent += abs(amount)
                else:
                    amount_label.setStyleSheet(f"color: {NEON_TEXT_DIM};")

                frame_layout.addWidget(curr_label)
                frame_layout.addStretch()
                frame_layout.addWidget(amount_label)

                self.layout.addWidget(frame)

            # Resumen en frame
            summary_frame = QFrame()
            summary_frame.setStyleSheet(f"""
                QFrame {{
                    background-color: {NEON_ACCENT};
                    border-radius: 15px;
                    border: 2px solid {NEON_YELLOW};
                }}
            """)
            summary_layout = QVBoxLayout(summary_frame)

            rec_label = QLabel(f"📥 {txt_total_received}: {total_rec:,.2f}")
            rec_label.setStyleSheet(f"color: {NEON_GREEN}; font-size: 14px;")
            
            sent_label = QLabel(f"📤 {txt_total_sent}: {total_sent:,.2f}")
            sent_label.setStyleSheet(f"color: {NEON_PINK}; font-size: 14px;")
            
            net = total_rec - total_sent
            net_color = NEON_GREEN if net >= 0 else NEON_PINK
            net_label = QLabel(f"💳 {txt_net_balance}: {net:,.2f}")
            net_label.setStyleSheet(f"color: {net_color}; font-size: 18px; font-weight: bold;")

            summary_layout.addWidget(rec_label)
            summary_layout.addWidget(sent_label)
            summary_layout.addWidget(net_label)

            self.layout.addWidget(summary_frame)

        self.btn_back = QPushButton("← " + txt_back)
        self.btn_back.setStyleSheet(f"""
            QPushButton {{
                background-color: {NEON_PANEL};
                color: {NEON_TEXT};
                border: 2px solid {NEON_PINK};
                margin-top: 20px;
            }}
            QPushButton:hover {{
                background-color: {NEON_PINK};
                color: {NEON_BG};
            }}
        """)
        self.layout.addWidget(self.btn_back)

        self.setLayout(self.layout)
        self.btn_back.clicked.connect(self.back_to_menu)

    def calculate_balance(self):
        balance = {}
        for trans in transactions_db.get(self.user_id, []):
            curr = trans["currency"]
            if curr not in balance:
                balance[curr] = 0
            if trans["type"] == "receive":
                balance[curr] += trans["amount"]
            else:
                balance[curr] -= trans["amount"]
        return balance

    def save_transaction(self):
        trans_type = "send" if self.combo_type.currentIndex() == 0 else "receive"
        currency = self.combo_currency.currentText()
        amount = self.spin_amount.value()
        description = self.line_description.text().strip()

        if amount <= 0:
            QMessageBox.warning(self, "Error", "El monto debe ser mayor a cero")
            return

        transaction = {
            "type": trans_type,
            "amount": amount,
            "currency": currency,
            "description": description
        }

        if self.user_id not in transactions_db:
            transactions_db[self.user_id] = []

        transactions_db[self.user_id].append(transaction)
        json.dump(transactions_db, open("data/transactions_db.json", 'w'))

        QMessageBox.information(self, "Éxito", "Movimiento registrado")
        self.back_to_menu()

    def load_history(self):
        self.table.setRowCount(0)

        filter_type = self.combo_filter_type.currentText()
        filter_curr = self.combo_filter_currency.currentText()

        row = 0
        for trans in transactions_db.get(self.user_id, []):
            if filter_type == txt_send_filter and trans["type"] != "send":
                continue
            if filter_type == txt_receive_filter and trans["type"] != "receive":
                continue
            if filter_curr != txt_all_currencies and trans["currency"] != filter_curr:
                continue

            self.table.insertRow(row)

            # Tipo con emoji y color
            if trans["type"] == "send":
                type_text = "📤 Salida"
                type_color = NEON_PINK
            else:
                type_text = "📥 Entrada"
                type_color = NEON_GREEN

            type_item = QTableWidgetItem(type_text)
            type_item.setForeground(Qt.magenta if trans["type"] == "send" else Qt.green)
            self.table.setItem(row, 0, type_item)

            # Monto
            amount_item = QTableWidgetItem(f"{trans['amount']:,.2f}")
            amount_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.table.setItem(row, 1, amount_item)

            # Moneda
            self.table.setItem(row, 2, QTableWidgetItem(trans["currency"]))

            # Descripción
            self.table.setItem(row, 3, QTableWidgetItem(trans["description"]))

            row += 1

    def back_to_menu(self):
        self.hide()
        from second_win import TestWin
        self.tw = TestWin(self.user_id, self.exp.first_name, self.exp.last_name)