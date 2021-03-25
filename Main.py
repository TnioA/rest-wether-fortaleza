# -*- coding: utf-8 -*-
from App import app
import os
from os.path import join, dirname

class Main:
    def __init__(self):

        if __name__ == '__main__':
            port = int(os.environ.get('PORT', 5000))
            app.run(host='0.0.0.0', port=port)

main = Main()