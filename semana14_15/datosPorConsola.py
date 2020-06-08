import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.cluster import KMeans

df = pd.read_csv('encuestas.csv')

print(np.array(df['¿Con que frecuencia te saltas clases?']))

print('-------------------------------')

print(np.array(df['¿Cuantas materias tienes reprobadas?']))


a1 = np.array(df['¿Con que frecuencia te saltas clases?'])
newlist = []
for x in df['¿Con que frecuencia te saltas clases?']:
	if x == 'Nunca':
		newlist.append(0)
	elif x == '1-2 veces al día':
		newlist.append(0.5)
	elif x == '3-4 veces al día':
		newlist.append(3.5)
	elif x == 'Más de 4 veces al día':
		newlist.append(4.5)
	elif x == '1-2 veces por semana':
		newlist.append(10)
	elif x == '3-4 veces por semana':
		newlist.append(17)
	elif x == '1-2 veces al mes':
		newlist.append(45)

print(f'Lista nueva: \n{newlist}')


a2 = np.array(df['¿Cuantas materias tienes reprobadas?'])
newlist2 = []
for x in a2:
	if x == 'Ninguna':
		newlist2.append(0)
	elif x == '1-2 materias':
		newlist2.append(0.5)
	elif x == '3-4 materias':
		newlist2.append(3.5)
	elif x == 'Más de 5 materias':
		newlist2.append(5.5)
print(newlist2)
newlist2.append(0.5)
print(f'\n{len(newlist2)} \n{len(newlist)}')


plt.scatter(newlist,newlist2,alpha=0.5)

#plt.bar(newlist,newlist2,facecolor='#9999ff')

#-----------------------------------------------------------------------

a3 = list(df['¿Con que frecuencia te saltas clases?']=='Nunca')
a4 = list(df['¿Cuantas materias tienes reprobadas?']=='Ninguna')
print('-----------------------------------\n',a3,'\n-------------------------------\n',a4)

a35 = np.array(df['¿Con que frecuencia te saltas clases?'])
a45 = np.array(df['¿Cuantas materias tienes reprobadas?'])

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

print((a3[0]==True and a4[0]==True))

#en este array list voy a unir newlist y newlist2
features = []
labels = []
for i in range(0,len(a3)):
	aux = []
	ax = newlist[i]
	ax2 = newlist2[i]
	aux.append(ax)
	aux.append(ax2)
	features.append(aux)
	if ((a3[i]==True) and (a4[i]==True)):
		labels.append('tt')
	elif ((a3[i]==False) and (a4[i]==True)):
		labels.append('ft')
	elif ((a3[i]==True) and (a4[i]==False)):
		labels.append('tf')
	elif ((a3[i]==False) and (a4[i]==False)):
		labels.append('ff')

classif = tree.DecisionTreeClassifier()
classif.fit(features, labels)
print(classif.predict([[0,0]]))

#clustering -------------------------------------
xx = np.array(list(zip(newlist,newlist2)))

kmeans=KMeans(n_clusters=6)
kmeans=kmeans.fit(features)
labels=kmeans.predict(features)
centroids=kmeans.cluster_centers_

colors=['m.','r.','c.','y.','b.','g.']

for i in range(len(features)):
	print("coordenada: ",features[i], 'label: ',labels[i])
	plt.plot(features[i][0],features[i][1],colors[labels[i]],markersize=10)


plt.scatter(centroids[:,0],centroids[:,1],marker='x',s=150,linewidths=5,zorder=10)

plt.show()


print('____________________________________________________________Belive\n')
df = pd.read_csv('encuestas.csv')#Muy útil
pu=0
inu=0
ut=0
mu=0
array = list(df['¿que tan útil crees que es pasar lista?'])
for i in range(0,len(array)):
	print(array[i])

print('---------------------------------------------------------------------------')


def predictions(coo):
	df = pd.read_csv('encuestas.csv')
	a1 = np.array(df['¿Con que frecuencia te saltas clases?'])
	newlist = []
	for x in df['¿Con que frecuencia te saltas clases?']:
		if x == 'Nunca':
			newlist.append(0)
		elif x == '1-2 veces al día':
			newlist.append(0.5)
		elif x == '3-4 veces al día':
			newlist.append(3.5)
		elif x == 'Más de 4 veces al día':
			newlist.append(4.5)
		elif x == '1-2 veces por semana':
			newlist.append(10)
		elif x == '3-4 veces por semana':
			newlist.append(17)
		elif x == '1-2 veces al mes':
			newlist.append(45)

	print(f'Lista nueva: \n{newlist}')


	a2 = np.array(df['¿Cuantas materias tienes reprobadas?'])
	newlist2 = []
	for x in a2:
		if x == 'Ninguna':
			newlist2.append(0)
		elif x == '1-2 materias':
			newlist2.append(0.5)
		elif x == '3-4 materias':
			newlist2.append(3.5)
		elif x == 'Más de 5 materias':
			newlist2.append(5.5)
	print(newlist2)
	newlist2.append(0.5)
	print(f'\n{len(newlist2)} \n{len(newlist)}')
	#-----------------------termina newList-----------------------------
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

	print((a3[0]==True and a4[0]==True))

	#en este arrayList voy a unir newlist y newlist2 atraves de data
	features = []
	labels = []
	for i in range(0,len(a3)):
		aux = []
		ax = newlist[i]
		ax2 = newlist2[i]
		aux.append(ax)
		aux.append(ax2)
		features.append(aux)
		if ((a3[i]==True) and (a4[i]==True)):
			labels.append('tt')
		elif ((a3[i]==False) and (a4[i]==True)):
			labels.append('ft')
		elif ((a3[i]==True) and (a4[i]==False)):
			labels.append('tf')
		elif ((a3[i]==False) and (a4[i]==False)):
			labels.append('ff')

	#clustering -------------------------------------
	kmeans=KMeans(n_clusters=6)
	kmeans=kmeans.fit(features)
	labels=kmeans.predict(features)
	prd = kmeans.predict(coo)
	centroids=kmeans.cluster_centers_	

	print(f'Prediction whit clustering-------------------------\n{prd}\n---------------------------')
	for i in range(len(features)):
		print(f'coordenada: {features[i]}     label:{labels[i]}')

predictions([[0,0.7]])


print('----------------------------')
features = [[6],[7],[3],[5]]

labels = [0, 0, 1, 1]
classif = tree.DecisionTreeClassifier()
classif.fit(features, labels)
#segun los datos ingresados va a predecir que animal es


print(classif.predict([[-30]]))


#ejemplo de arbol de decisiones------------------
'''from sklearn.tree import DecisionTreeRegressor
algor = DecisionTreeRegressor()
algor.fit(newlist,0)
print(algor.predict(0.5,0))'''


#prueba del algoritmo del arbol
def treeAlgorithm(coo):
	newlist = []
	newlist2 = []
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
	newlist2.append('5.5')

	classif = tree.DecisionTreeClassifier()
	classif.fit(newlist,newlist2)

	print(classif.predict([[coo]]))

treeAlgorithm(10)