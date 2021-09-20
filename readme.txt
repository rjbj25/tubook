- Iniciar Django venv
source djangovenv/bin/activate
- Iniciar Servidor con:
python manage.py runserver
- Iniciar Servidor en modo detached en produccion
screen -d -m python3 manage.py runserver 0.0.0.0:8000
