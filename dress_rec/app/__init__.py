#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 19:53:44 2019

@author: vanya
"""

from flask import Flask, render_template
from config import Config
app = Flask(__name__)
app.config.from_object(Config)
from app import routes