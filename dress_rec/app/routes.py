#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 19:56:15 2019

@author: vanya
"""

from flask import Flask, render_template, redirect, request
from app import app


from app.forms import SimpleForm
from app.process import classifier
@app.route('/')
@app.route('/ind')
def index():
    return render_template('base.html')

@app.route('/dress',methods=['POST','GET'])
def hello_world():
    form = SimpleForm()
    if form.validate_on_submit():
        return redirect('/')
    #return render_template('basicform7.html',form=form,buttons=form.fabric,buttons1=form.occasion,buttons2=form.pattern)
    return render_template('basicform9.html',form=form)
@app.route('/thanks',  methods=['GET', 'POST'])
def thanks():
    #input2 = request.form.get('url')
    input1 = request.form.get('fabric')
    print(input1)
    input2 = request.form.get('occasion')
    input3 = request.form.get('pattern')
    inputt = [input1,input2,input3]
    dress = classifier(inputt)
    dress1 = dress.numbering(inputt)
    dress2 = dress.nearestNeighbour(dress1)
    link1 = dress.link(dress2[1][1])
    return render_template('thanks2.html', checkval=dress2[1][1], image1=link1)

