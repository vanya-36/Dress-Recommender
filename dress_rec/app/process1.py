#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 21:30:45 2019

@author: vanya
"""

import os, pandas as pd

class classifier:

    def __init__(self,s_dress):
        self.s_dress=s_dress
        f = open (os.path.expanduser("~/Downloads/new_product_dump - facet_dump1.csv"))
        #f=open("iCloud Drive▸Desktop▸dress_set.txt")
        dataset = pd.read_csv("~/Downloads/new_product_dump - facet_dump1.csv")
        self.links = dataset.iloc[:,10].values
        lines=f.readlines()
        f.close()
        #for index, row in dataset.head(n=2).iterrows():
        #   print(dat
        self.title = pd.array
        self.title.append(dataset[0])
        print(self.title)
        #f=open("dress_set.txt")
        self.format=lines[0].strip().split(',')
        #print(format)
        self.data=[]
        self.ignore = []
        self.linkss=[]
        c=-1
        for line in lines[1:]:
            fields = line.strip().split(',')
            vector = []
            for i in range(len(self.format)):
                    if self.format[i] == 'Fabric':
                        vector.append(fields[i])
                    elif self.format[i] == 'Occasion':
                        vector.append(fields[i])
                    elif self.format[i] == 'Pattern':
                        vector.append(fields[i])
                    elif self.format[i] == 'Title':
                        self.ignore.append(fields[i])
                        c=c+1
                    elif self.format[i] == 'Image URL':
                        self.linkss.append(fields[i])
            for j in range(len(vector)):
                try:
                    int(vector[j])
                except:
                    #if vector[j] == '':
                        vector[j]=0
                    #elif isinstance(vector[j], str):
                     #   vector[j]=0
                vector[j]=int(vector[j])
                    
                   # print(j)
            #print(self.linkss[:3])
            self.data.append((vector, self.ignore[c]))
            #vector = []
        #print(self.data[:3])
        #print(self.s_dress)
        
        
    def numbering(self,s_dress):
        if s_dress[0]=='Polyester':
            s_dress[0]=1
        elif s_dress[0]=='Blended':
            s_dress[0]=2
        elif s_dress[0]=='Viscose-Rayon':
            s_dress[0]=3
        elif s_dress[0]=='Georgette':
            s_dress[0]=4
        elif s_dress[0]=='Cotton':
            s_dress[0]=5
        if s_dress[1]=='Casual':
            s_dress[1]=1
        elif s_dress[1]=='Ethnic':
            s_dress[1]=2
        elif s_dress[1]=='Party':
            s_dress[1]=3
        if s_dress[2]=='Floral':
            s_dress[2]=1
        elif s_dress[2]=='Solid':
            s_dress[2]=2
        elif s_dress[2]=='Geometric':
            s_dress[2]=3
        return s_dress    
            
    def mandist(self,vector1,vector2):
        return sum(map(lambda v1, v2: abs(v1 - v2), vector1, vector2))
    
    def nearestNeighbour(self, itemVector):
        return min([ (self.mandist(itemVector, item[0]), item)
                     for item in self.data])
    
    def link(self,s_dress):
      c=0
      t=0
      for i in self.ignore:
          if i==s_dress:
                t=c
          c=c+1
      print(t)
      return self.links[t]
  

name=input("Please enter your name")
s_dress=[]
dress_val=[]
#d={"sleeves":0,"fabric":0,"shape":0,"occassion":0,"pattern":0}
#d={"fabric":0,"occassion":0,"pattern":0}
#a=int(input("Please enter a sleeve length based on the key below: \n No sleeves: 1 \n Short sleeves: 2 \n Medium sleeves: 3 \n Long/ Three-fourth sleeves: 4 \n Cold/Off shoulder sleeves:5 \n"))
#s_dress.append(("sleeves",a))
#dress_val.append(a)                         
a=int(input("Please enter a fabric type based on the key below: \n Polyester: 0 \n Blended: 1 \n Viscose Rayon: 2 \n Georgette: 3 \n Cotton: 5 \n"))
s_dress.append(("fabric",a))
dress_val.append(a)
#a=int(input("Please enter a shape/style based on the key below: \n Sheath: 1 \n Maxi: 2 \n Fit and Flare: 3 \n A-line: 4 \n"))
#dress_val.append(a)                         
#s_dress.append(("shape",a))
a=int(input("Please enter an occassion based on the key below: \n Casual: 1 \n Ethnic: 2 \n Party: 3 \n"))
s_dress.append(("occassion",a))
dress_val.append(a)                       
a=int(input("Please enter a pattern based on the key given below: \n Floral: 1 \n Solid: 2 \n Geometric: 3 \n Self-design: 4 \n"))
s_dress.append(("pattern",a))
dress_val.append(a)
classify = classifier(dress_val)
