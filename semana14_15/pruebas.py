# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 10:27:08 2020

@author: kcram
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree

def pred(dat1):
    df = pd.read_csv('encuestas.csv')
    newlist = []
    newlist2 = []
    a1 = np.array(df['¿Con que frecuencia te saltas clases?'])
    for x in a1:
        aux = []
        if x == 'Nunca':
            aux.append(0)
            newlist.append(aux)
        elif x == '1-2 veces al día':
            aux.append(1)
            newlist.append(aux)
        elif x == '3-4 veces al día':
            aux.append(2)
            newlist.append(aux)
        elif x == 'Más de 4 veces al día':
            aux.append(1)
            newlist.append(aux)
        elif x == '1-2 veces por semana':
            aux.append(4)
            newlist.append(aux)
        elif x == '3-4 veces por semana':
            aux.append(5)
            newlist.append(aux)
        elif x == '1-2 veces al mes':
            aux.append(6)
            newlist.append(aux)
    
    a2 = np.array(df['¿Cuantas materias tienes reprobadas?'])
    for x in a2:
        if x == 'Ninguna':
            newlist2.append(0)
        elif x == '1-2 materias':
            newlist2.append(1)
        elif x == '3-4 materias':
            newlist2.append(2)
        elif x == 'Más de 5 materias':
            newlist2.append(3)
            
    X_train,X_test,y_train,y_test=train_test_split(newlist, newlist2, test_size=1)
    
    knn = KNeighborsClassifier(n_neighbors=7)
    
    knn.fit(X_train, y_train)
    
    #Se realiza la prediccion
    
    Y_pred = knn.predict([[dat1]])
    
    return Y_pred

def knnButIsTree(dat1):
    #esto es arbol de decisiones
    df = pd.read_csv('encuestas.csv')
    newlist = []
    newlist2 = []
    a1 = np.array(df['¿Con que frecuencia te saltas clases?'])
    for x in a1:
        aux = []
        if x == 'Nunca':
            aux.append(0)
            newlist.append(aux)
        elif x == '1-2 veces al día':
            aux.append(1)
            newlist.append(aux)
        elif x == '3-4 veces al día':
            aux.append(2)
            newlist.append(aux)
        elif x == 'Más de 4 veces al día':
            aux.append(1)
            newlist.append(aux)
        elif x == '1-2 veces por semana':
            aux.append(4)
            newlist.append(aux)
        elif x == '3-4 veces por semana':
            aux.append(5)
            newlist.append(aux)
        elif x == '1-2 veces al mes':
            aux.append(6)
            newlist.append(aux)
    
    a2 = np.array(df['¿Cuantas materias tienes reprobadas?'])
    for x in a2:
        if x == 'Ninguna':
            newlist2.append(0)
        elif x == '1-2 materias':
            newlist2.append(1)
        elif x == '3-4 materias':
            newlist2.append(2)
        elif x == 'Más de 5 materias':
            newlist2.append(3)

    classif = tree.DecisionTreeClassifier()
    classif.fit(newlist,newlist2)

    return classif.predict([[dat1]])

