# -*- coding: utf-8 -*-
from App import app
from dotenv import load_dotenv
import os

load_dotenv()

class Main:
    def __init__(self):

        if __name__ == '__main__':
            host = os.getenv('FLASK_HOST', '')
            port = int(os.getenv('FLASK_PORT', 5000))
            app.run(host=host, port=port)

main = Main()