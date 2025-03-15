import os
import sys
from pathlib import Path

# Proje kök dizinini ayarla
project_root = Path(__file__).parent
os.chdir(project_root)
sys.path.insert(0, str(project_root))

# Ana uygulamayı çalıştır
from main import main

if __name__ == "__main__":
    sys.exit(main()) 