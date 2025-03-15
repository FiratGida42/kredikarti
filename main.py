import sys
from PyQt6.QtWidgets import QApplication
from views.login_view import LoginView
from models.database import init_db

def main():
    # Uygulama başlatılması
    app = QApplication(sys.argv)
    
    # Veritabanını başlat
    init_db()
    
    # Giriş penceresini göster
    login_window = LoginView()
    login_window.show()
    
    # Uygulamayı çalıştır
    return app.exec()

if __name__ == "__main__":
    main() 