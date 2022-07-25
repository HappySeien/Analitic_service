import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

# Под переменные окружения
DOTENV_PATH = BASE_DIR / '.env'

if os.path.exists(DOTENV_PATH):
    load_dotenv(dotenv_path=DOTENV_PATH)

# База данных
