#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 23:37:07 2019

@author: vanya
"""
from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField
from wtforms.validators import DataRequired
from wtforms import widgets, SelectMultipleField
import os

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember_me= BooleanField('Remember me')
    #submit = SubmitField('Sign In')


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()
    
class SimpleForm(FlaskForm):
    string_of_files = ['check1,check2']
    list_of_files = string_of_files[0].split(',')
# create a list of value/description tuples
    
    files1 = ['Polyester,Blended,Viscose-Rayon,Georgette,Cotton']
    list_of_files = files1[0].split(',')  
    files = [(x, x) for x in list_of_files]
    #print(files)
    fabric = RadioField('Fabric', choices=files)
    
    files11 = ['Casual,Ethnic,Party']
    list_of_files1 = files11[0].split(',') 
    files111 = [(x, x) for x in list_of_files1]
    #print(files)    
    occasion = RadioField('Occasion', choices=files111)
    
    files12 = ['Floral,Solid,Geometric']
    list_of_files2 = files12[0].split(',')    
    files22 = [(x, x) for x in list_of_files2]
    #print(files)
    pattern = RadioField('Pattern', choices=files22)
    
    submit = SubmitField('submit')
    

    