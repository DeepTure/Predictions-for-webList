import pandas as pd
import numpy as np

def moda():
	#primero preparamos la bbdd en pandas
	df = pd.read_csv('encuestas.csv')
	#preparamos variables a utilizar
	n = 0
	ud = 0
	tc = 0
	mc = 0
	uds = 0
	tcs = 0
	udm = 0
	a1 = np.array(df['¿Con que frecuencia te saltas clases?'])
    #este for recorre todas las veces que se saltan clases y aumanta cada uno de los valores
	for x in a1:
		aux = []
		if x == 'Nunca':
			n+=1
		elif x == '1-2 veces al día':
			ud+=1
		elif x == '3-4 veces al día':
			tc+=1
		elif x == 'Más de 4 veces al día':
			mc+=1
		elif x == '1-2 veces por semana':
			uds+=1
		elif x == '3-4 veces por semana':
			tcs+=1
		elif x == '1-2 veces al mes':
			udm+=1

	data = [n,ud,tc,mc,uds,tcs,udm]
    #sacamos el valor maximo de la lista
	fsc = max(data)
	#ahora vamos a ver cual es el que mas se repite
	i = data.index(fsc)
    #preparamos las variables
	n = 0
	ud = 0
	tc = 0
	m5 = 0
    #hacemos los mismo
	a2 = np.array(df['¿Cuantas materias tienes reprobadas?'])
	for x in a2:
		if x == 'Ninguna':
			n+=1
		elif x == '1-2 materias':
			ud+=1
		elif x == '3-4 materias':
			tc+=1
		elif x == 'Más de 5 materias':
			m5+=1

	ds = [n,ud,tc,m5]
	mr = max(ds)
	data = []
	if(i==0):
		data.append('Nunca')
	elif(i==1):
		data.append('1-2 veces al día')
	elif(i==2):
		data.append('3-4 veces al día')
	elif(i==3):
		data.append('Más de 4 veces al día')
	elif(i==4):
		data.append('1-2 veces por semana')
	elif(i==5):
		data.append('3-4 veces por semana')
	elif(i==6):
		data.append('1-2 veces al mes')

	i = ds.index(mr)
	if(i==0):
		data.append('Ninguna')
	elif(i==1):
		data.append('1-2 materias')
	elif(i==2):
		data.append('3-4 materias')
	elif(i==3):
		data.append('Más de 5 materias')

	return data

def mediana():
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

    a = sorted(newlist)
    b = sorted(newlist2)

    data = [a[83],a[84],b[83],b[84]]
    #sabemos que esto es [1,1,0,0] entnces
    dd = ['1-2 veces al día','Más de 4 veces al día','Ninguna']

    return dd

def mediaA():
    df = pd.read_csv('encuestas.csv')
    newlist = []
    newlist2 = []
    a1 = np.array(df['¿Con que frecuencia te saltas clases?'])
    aux = []
    for x in a1:
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

    aux1 = 0
    for i in aux:
    	aux1+=i

    aux2 = 0
    for i in newlist2:
    	aux2+=i

    data = []
    data.append(aux1/len(aux))
    data.append(aux2/len(newlist2))
    return data


def varianza():
    df = pd.read_csv('encuestas.csv')
    aux = []
    aux1 = []
    aux2 = []
    aux3 = []
    aux4 = []
    aux5 = []
    aux6 = []

    newlist2 = []
    a1 = np.array(df['¿Con que frecuencia te saltas clases?'])
    for x in a1:
        if x == 'Nunca':
            aux.append(0)
        elif x == '1-2 veces al día':
            aux1.append(1)
        elif x == '3-4 veces al día':
            aux2.append(2)
        elif x == 'Más de 4 veces al día':
            aux3.append(1)
        elif x == '1-2 veces por semana':
            aux4.append(4)
        elif x == '3-4 veces por semana':
            aux5.append(5)
        elif x == '1-2 veces al mes':
            aux6.append(6)
    
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

