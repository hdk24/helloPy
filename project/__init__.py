# -*- coding: utf-8 -*-
__version__ = '0.1'
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'random'
app.debug = True

# Register controllers here
from project.controllers import index
