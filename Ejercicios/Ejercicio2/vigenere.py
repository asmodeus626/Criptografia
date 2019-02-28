
import math
import sys

alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

#             A      B     C      D      E      F      G     H       I      J      K     L       M      N      Ñ      O     P       Q      R      S     T       U     V       W     X     Y     Z
frecEsp = [0.1243,0.0173,0.041,0.0478,0.1306,0.0058,0.0106,0.0112,0.0647,0.0054,0.0004,0.0592,0.0291,0.0685,0.0017,0.0996,0.0232,0.0106,0.0646,0.0728,0.0430,0.0411,0.0107,0.0002,0.001,0.011,0.0045] #La frecuencia de las letras en el español.

f = open (sys.argv[1],'r')
entrada = f.read() #La entrada completa.
entrada2 = "" #La entrada sin signos de puntuación, números, etc...

for c in entrada:
	if c in alfabeto:
		entrada2 = entrada2+c
f.close()
n = len(entrada2) #n guarda la longitud de la entrada2.
#Hasta aquí ya leímos y limpiamos la entrada del programa.

#Crea el bloque con los índices 0, t, 2t, 3t...
def creaBloque(b,t):
	bloque = entrada2[b]
	i = 1
	j = t+b
	while j<n:
		bloque += entrada2[j]
		i += 1
		j = t*i + b

	return bloque
#Fin de creaBloque

#Calcula la frecuencia relativa de apariciones de cada letra.
#Es decir, el número de veces que aparece una letra dividido en el tamaño de la entrada.
def frecuencia(cadena):
	apariciones = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

	for c in cadena:
		indice = alfabeto.index(c)
		apariciones[indice] += 1

	for i in range(0,len(apariciones)):
		apariciones[i] = apariciones[i]/len(cadena)

	return apariciones
#Fin de frecuencia

#Calcula el índice de coincidencias
def indCoin(lista):
	ic = 0

	for e in lista:
		ic += e*e

	return ic
#fin de indCoin

#Recibe un bloque, y le devuelve el desplazamiento más óptimo.
def getDes(bloque):
	d = 0 #Guardará el valor de desplazamiento(la mejor k)
	minimo = 10 #Guarda la distancia mínima entre el ic y 0.0741
	for k in range(0,26):
		fb = frecuencia(bloque) #Calculo la frecuencia relativa en el bloque.
		ic = 0 #índice de coincidencias.
		for l in range(0,26):
			ic+=frecEsp[l]*fb[(l+k) % 27]

		if math.fabs(ic - 0.0741) < minimo:
			d = k
			minimo = math.fabs(ic - 0.0741)

	return d
#Fin getDes

#Módulo inverso
def modInverso(num,modulo):
	while num<0:
		num+=modulo

	return num

#Algoritmo que descifra un código, teniendo la clave.
def descifra(texto, key):
	salida = ""
	tkey = len(key) #Tamaño de la clave
	ttexto = len(texto) #Tamaño del texto
	i = -1

	for l in texto:
		if l in alfabeto:
			i+=1
			desp = alfabeto.index(key[i % tkey])
			indLetra = alfabeto.index(l)
			salida += alfabeto[modInverso(indLetra - desp, 27)]
		else:
			salida += l

	return salida
#Fin descifra

def mayor(e):
	return e[1]

#Algoritmo que aproxima el tamaño de la clave, y devuelve los 3 mejores resultados.
def getTamanioClave():
	tuplas = []
	for i in range(1,30): #Solo probaremos los primeros 30 tamaños, para fines prácticos
		block = creaBloque(0,i) #Calculo el bloque
		frec = frecuencia(block) #Calculo las frecuencias relativas
		ic = indCoin(frec) #Calculo el índice de coincidencias
		dist = math.fabs(ic - 0.0741) #Calculo la distancia a 0.0741
		tuplas.append((i,dist)) #Guardo la tupla (tamaño, distancia)

	tuplas.sort(key = mayor) #Ordeno las tuplas de acuerdo a la distancia.
	retorno = []
	p = tuplas[0]
	s = tuplas[1]
	t = tuplas[2]
	#Agrego los 3 mejores resultados.
	retorno.append(p[0])
	retorno.append(s[0])
	retorno.append(t[0])

	return retorno
#Fin de getTamanioClave

#Función que devuelve una clave, dependiendo del tamaño que recibe.
def getClave(tam):
	retVal = ""
	for i in range(0,tam):
		bn = creaBloque(i,tam)
		retVal += alfabeto[getDes(bn)]

	return retVal


###################################################################################################################
tamanios = getTamanioClave()

for elem in tamanios:
	clave = getClave(elem)
	textoOriginal = descifra(entrada, clave)
	print("Clave: "+clave)
	print("Texto: "+textoOriginal[0:50]+"\n")