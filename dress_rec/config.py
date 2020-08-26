#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 23:34:40 2019

@author: vanya
"""

import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'