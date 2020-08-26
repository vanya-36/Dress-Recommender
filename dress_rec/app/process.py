#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 23:16:44 2019

@author: vanya
"""
import os, pandas as pd

class classifier:

    def __init__(self,s_dress):
        self.s_dress=s_dress
        f = open (os.path.expanduser("~/Dress-Recommender/dress_rec/new_product_dump - facet_dump1.csv"))
        #f=open("iCloud Drive▸Desktop▸dress_set.txt")
        dataset = pd.read_csv("~/Downloads/new_product_dump - facet_dump1.csv")
        self.links = dataset.iloc[:,10].values
        lines=f.readlines()
        f.close()
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
