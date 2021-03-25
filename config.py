import os

BASE_DIR=os.path.abspath(os.path.dirname(__file__))  
DEBUG=True
JSON_AS_ASCII=False

FLASK_ENV="development"
FLASK_APP="myapp.app.py"
FLASK_PORT=5000
FLASK_DEBUG=True
FLASK_HOST="0.0.0.0"

MAIL_USERNAME="myemail@gmail.com"
MAIL_PASSWORD="my secret password"

DATABASE_URL="sqlite:///development_database.db"
