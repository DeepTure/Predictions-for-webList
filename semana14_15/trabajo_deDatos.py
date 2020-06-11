import pandas as pd 
import numpy as np 
from sklearn import tree
import pruebas


def contarClasesSaltadasVsMateriasReprobadas():
	df = pd.read_csv('encuestas.csv')
	a3 = list(df['¿Con que frecuencia te saltas clases?']=='Nunca')
	a4 = list(df['¿Cuantas materias tienes reprobadas?']=='Ninguna')
	tt = 0
	ft = 0
	tf = 0
	ff = 0
	for i in range(0,len(a3)):
		if ((a3[i]==True) and (a4[i]==True)):
			tt+=1
		elif ((a3[i]==False) and (a4[i]==True)):
			ft+=1
		elif ((a3[i]==True) and (a4[i]==False)):
			tf+=1
		elif ((a3[i]==False) and (a4[i]==False)):
			ff+=1

	print(f'tt: {tt}\nft:{ft} \ntf:{tf}\nff: {ff}')
	data = [tt,ft,tf,ff]
	return data

def howManyBelive():
	df = pd.read_csv('encuestas.csv')
	pu=0
	inu=0
	ut=0
	mu=0
	array = list(df['¿que tan útil crees que es pasar lista?'])
	for i in range(0,len(array)):
		if(array[i]=='Poco útil'):
			pu+=1
		if(array[i]=='Inutil'):
			inu+=1
		if(array[i]=='Útil'):
			ut+=1
		if(array[i]=='Muy útil'):
			mu+=1

	print(f'pu: {pu}\ninu: {inu}\nut: {ut}\nmu: {mu}')
	data = [pu,inu, ut, mu]
	return data

def fpa():
	df = pd.read_csv('encuestas.csv')
	pu=0
	inu=0
	ut=0
	mu=0
	array = list(df['¿Que tan seguido pasan asistencia tus profesores?'])
	for i in range(0,len(array)):
		if(array[i]=='Nunca'):
			pu+=1
		if(array[i]=='1-2 veces a la semana'):
			inu+=1
		if(array[i]=='3-4 veces a la semana'):
			ut+=1
		if(array[i]=='Todos los días'):
			mu+=1
	data = [pu,inu, ut, mu]
	return data

def treeAlgorithm(coo,cont):
    pred = pruebas.pred(coo)
    
    return pred
    """
    newlist = []
    list2 = []
    df = pd.read_csv('encuestas.csv')
    for x in df['¿Con que frecuencia te saltas clases?']:
        aux = []
        if x == 'Nunca':
            aux.append(0)
            newlist.append(aux)
        elif x == '1-2 veces al día':
            aux.append(0.5)
            newlist.append(aux)
        elif x == '3-4 veces al día':
            aux.append(3.5)
            newlist.append(aux)
        elif x == 'Más de 4 veces al día':
            aux.append(4.5)
            newlist.append(aux)
        elif x == '1-2 veces por semana':
            aux.append(10)
            newlist.append(aux)
        elif x == '3-4 veces por semana':
            aux.append(17)
            newlist.append(aux)
        elif x == '1-2 veces al mes':
            aux.append(45)
            newlist.append(aux)

    a2 = np.array(df['¿Cuantas materias tienes reprobadas?'])
    for x in a2:
        if x == 'Ninguna':
            newlist2.append('0')
        elif x == '1-2 materias':
            newlist2.append('0.5')
        elif x == '3-4 materias':
            newlist2.append('3.5')
        elif x == 'Más de 5 materias':
            newlist2.append('5.5')
            list2.append('5.5')

    if(cont=='sem'):
        coo=coo*5
    if(cont=='mes'):
        coo*=45

    classif = tree.DecisionTreeClassifier()
    classif.fit(newlist,newlist2)

    return classif.predict([[coo]])
"""
    

def lostTime():
	#¿Cuanto tiempo tardan tus profesores en pasar lista? // ¿Que tan seguido pasan asistencia tus profesores?
	df = pd.read_csv('encuestas.csv')
	data = []
	array = list(df['¿Cuanto tiempo tardan tus profesores en pasar lista?'])
	for i in range(0,len(array)):
		if(array[i]=='5 minutos'):
			data.append(2.5)
		if(array[i]=='6-10 minutos'):
			data.append(8)
		if(array[i]=='11-15 minutos'):
			data.append(13)
		if(array[i]=='Más de 15 minutos'):
			data.append(17.5)

	data2 = []
	array = list(df['¿Cuanto tiempo tardan tus profesores en pasar lista?'])
	for i in range(0,len(array)):
		if(array[i]=='Nunca'):
			data2.append(0)
		elif(array[i]=='3-4 veces a la semana'):
			data2.append(3.5)
		elif(array[i]=='Todos los días'):
			data2.append(6)
	return data2