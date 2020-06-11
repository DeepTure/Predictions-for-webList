import pandas as pd
import numpy as np
from flask import Flask, render_template, request
from trabajo_deDatos import contarClasesSaltadasVsMateriasReprobadas
from trabajo_deDatos import treeAlgorithm
from trabajo_deDatos import howManyBelive
from trabajo_deDatos import lostTime
from pruebas import knnButIsTree
from trabajo_deDatos import fpa

#algoritmo necesarios para la pagina principal
a = contarClasesSaltadasVsMateriasReprobadas()
#b = treeAlgorithm(0)
b = lostTime()
c = howManyBelive()
d = lostTime()
e = fpa()

#---------------app web------------------
app = Flask(__name__)
@app.route('/')
def login():
	return render_template('login.html')

@app.route('/menu')
def main():
    return render_template('main.html',a=a,b=b,c=c,d=d,e=e)

@app.route('/menu/treeDecision')
def tree():
	return render_template('treeDecision.html');

@app.route('/menu/knnn')
def knn():
    return render_template('k-nn.html');

@app.route('/treeDecisionResult', methods=["GET","POST"])
def treeResult():
    if (request.form['tree']=='t'):
        op = request.form['op']
        abcd = knnButIsTree(op);
        return render_template('impresion.html', abcd = abcd)

    elif (request.form['op']!=''):
            op = request.form['op']
            abcd = treeAlgorithm(op,'op')
            return render_template('impresion.html', abcd = abcd)
    else:
        return '<script type="text/javascript"> alert("Debe llenar solo un campo"); window.location.replace("http://localhost:5000/menu/treeDecision"); </script>'

if __name__=="__main__":
	app.run(debug=True)

