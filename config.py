import os
from pathlib import Path

# Uygulama bilgileri
APP_NAME = "Kredi Kartı Takip Programı"
APP_VERSION = "1.0.0"
APP_AUTHOR = "Kredi Kart Takip Projesi"

# Dosya yolları
APP_DIR = Path(__file__).parent
ASSETS_DIR = APP_DIR / "assets"
DATABASE_FILE = Path.home() / f"{APP_NAME.replace(' ', '_').lower()}.db"

# Veritabanı ayarları
DB_CONNECTION = f"sqlite:///{DATABASE_FILE}"

# GUI ayarları
WINDOW_MIN_WIDTH = 1200
WINDOW_MIN_HEIGHT = 800
START_MAXIMIZED = True

# Tema ayarları
DEFAULT_THEME = "light"  # veya "dark"

# Diğer ayarlar
DATE_FORMAT = "dd.MM.yyyy"
CURRENCY_FORMAT = "#,##0.00"
CURRENCY_SYMBOL = "₺" 