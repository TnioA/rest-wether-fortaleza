# -*- coding: utf-8 -*-
from App import app
import os
from os.path import join, dirname
from dotenv import load_dotenv

class Main:
    def __init__(self):
        dotenv_path = join(dirname(__file__), 'config.py')
        load_dotenv(dotenv_path)

        host = os.getenv('FLASK_HOST')
        port = int(os.getenv('FLASK_PORT'))
        debug = os.getenv('FLASK_DEBUG')
        
        app.run(host=host, port=port, debug=debug)

main = Main()