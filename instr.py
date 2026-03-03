from PyQt5.QtCore import QTime

# Configuración de ventana
win_x, win_y = 100, 100
win_width, win_height = 1000, 600

# Paleta de colores NEON
NEON_BG = "#0a0a0a"           # Negro casi puro
NEON_PANEL = "#1a1a2e"        # Azul muy oscuro
NEON_ACCENT = "#16213e"       # Azul oscuro
NEON_PINK = "#ff006e"         # Rosa neón
NEON_CYAN = "#00f5ff"         # Cian neón
NEON_GREEN = "#39ff14"        # Verde neón
NEON_YELLOW = "#fff01f"       # Amarillo neón
NEON_PURPLE = "#bc13fe"       # Púrpura neón
NEON_ORANGE = "#ff6600"       # Naranja neón
NEON_TEXT = "#ffffff"         # Blanco
NEON_TEXT_DIM = "#a0a0a0"     # Gris claro

# Tasa de cambio BCV
BCV_RATE = 450  # 450 Bs por $1

# Pantalla 1 - Login
txt_title = '💰 EconomiK - Gestión Monetaria'
txt_hello = 'Bienvenido a EconomiK'
txt_instruction = ('Sistema de gestión monetaria personal.\n'
                   'Registre sus movimientos en Bolívares (BCV) y Dólares.\n'
                   'Tasa BCV: 450 Bs = $1 USD')
txt_next = 'Iniciar Sesión'
txt_register = 'Registrarse'

# Campos de login
txt_name = 'Nombre'
txt_lastname = 'Apellido'
txt_pin = 'PIN (4 dígitos)'
txt_hintname = "Ingrese su nombre"
txt_hintlastname = "Ingrese su apellido"

# Pantalla 2 - Menú Principal
txt_menu_title = 'Menú Principal'
txt_welcome = '¿Qué desea hacer hoy?'
txt_new_transaction = 'Nuevo Movimiento'
txt_view_history = 'Ver Movimientos'
txt_view_balance = 'Ver Saldos'
txt_logout = 'Cerrar Sesión'

# Pantalla 3 - Transacciones
txt_transaction_title = 'Nuevo Movimiento'
txt_type = 'Tipo de operación'
txt_send = 'Gasto / Salida'
txt_receive = 'Ingreso / Entrada'
txt_currency = 'Moneda'
txt_amount = 'Monto'
txt_description = 'Descripción (opcional)'
txt_save = 'Guardar'
txt_back = 'Volver'

# Opciones de moneda
CURRENCY_BSF = 'Bolívares (Bs)'
CURRENCY_USD = 'Dólares ($)'

# Pantalla 4 - Historial
txt_history_title = 'Historial de Movimientos'
txt_filter_type = 'Filtrar:'
txt_filter_currency = 'Moneda:'
txt_all = 'Todos'
txt_send_filter = 'Salidas'
txt_receive_filter = 'Entradas'
txt_all_currencies = 'Todas'

# Pantalla 5 - Saldos
txt_balance_title = 'Mis Saldos'
txt_total_received = 'Total Ingresos'
txt_total_sent = 'Total Gastos'
txt_net_balance = 'Balance Neto'
txt_bcv_rate = 'Tasa BCV: 450 Bs = $1'

# Textos de resultado (mantenidos por compatibilidad)
txt_index = 'Índice: '
txt_workheart = 'Estado: '
txt_res1 = "bajo"
txt_res2 = "satisfactorio"
txt_res3 = "promedio"
txt_res4 = "por encima del promedio"
txt_res5 = "alto"

# Configuración de tiempo
time = QTime(0, 0, 15)
txt_timer = time.toString("hh:mm:ss")
txt_age = 'Edad:'
txt_finalwin = 'Resultados'