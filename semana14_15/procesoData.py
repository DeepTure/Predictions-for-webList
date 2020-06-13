import pandas as pd
import numpy as np
from flask import Flask, render_template, request
from trabajo_deDatos import contarClasesSaltadasVsMateriasReprobadas
from trabajo_deDatos import treeAlgorithm
from trabajo_deDatos import howManyBelive
from pruebas import knnButIsTree
from trabajo_deDatos import fpa
from analysisData import *

#algoritmo necesarios para la pagina principal
a = contarClasesSaltadasVsMateriasReprobadas()
c = howManyBelive()
e = fpa()

#---------------app web------------------
app = Flask(__name__)
@app.route('/')
def login():
    #esta es la pagina web principal
	return render_template('login.html')

@app.route('/menu')
def main():
    #este es el menu, algo así como un lobi, los parametros son los datos para las graficas
    return render_template('main.html',a=a,c=c,e=e)

@app.route('/menu/treeDecision')
def tree():
    #esta es la pagina para el algoritmo de k-nn
	return render_template('treeDecision.html');

@app.route('/menu/knnn')
def knn():
    #esta es la pagina para el algoritmo de arbol de decision
    return render_template('k-nn.html');

@app.route('/treeDecisionResult', methods=["GET","POST"])
def treeResult():
    #esta pagina es la encargada de obtener la respuesta de ambos algoritmos procesarla, hacer la prediccion y mostrar la prediccion al usuario
    if (request.form['tree']=='t'):
        #este if se ejecuta si es arbol de decision
        op = request.form['op']
        abcd = knnButIsTree(op);
        return render_template('impresion.html', abcd = abcd, ti='arbol de decisiones')

    elif (request.form['op']!=''):
        #este if se ejecuta si es k_nn
            op = request.form['op']
            abcd = treeAlgorithm(op,'op')
            return render_template('impresion.html', abcd = abcd, ti='K-NN')
    else:
        return '<script type="text/javascript"> alert("Debe llenar solo un campo"); window.location.replace("http://localhost:5000/menu/treeDecision"); </script>'

#esta funcion es la que te lleva a el analisis de datos
@app.route('/menu/AnalizisData')
def analysis():
    m = moda()
    mm = mediana()
    ma = mediaA()
    #supongo que no hace fakta decir que hacen los parametros
    return render_template('mostrarData.html',m=m,mm=mm,ma=ma)


if __name__=="__main__":
	app.run(debug=True)

