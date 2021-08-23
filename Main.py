# -*- coding: utf-8 -*-
from App import app
from dotenv import load_dotenv
from os.path import join, dirname
import os

load_dotenv()

class Main:
    def __init__(self):

        if __name__ == '__main__':
            host = os.getenv('FLASK_HOST', '')
            port = int(os.getenv('FLASK_PORT', 5000))
            app.run(host='0.0.0.0', port=port)

main = Main()