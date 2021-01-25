
import random

# Convierte un número decimal a binario
def decToBin(n):
    binario = []
    while n>0:
        binario.insert(0,(n%2))
        n = n//2        
    return binario
# Fin decToBin


# Calcula el exponente b^pot mod n en tiempo log(pot). (Página 283, Stallings).
def modPot(b,pot,n):
    f = 1
    binPot = decToBin(pot) #Representación binaria de pot.
    for bit in binPot:
        f = (f*f) % n
        if bit == 1:
            f = (f*b) % n
    #print('$'+str(b)+'^{'+str(pot)+'} \cong '+str(f)+' \mod '+str(n)+'$')
    #print('('+str(pot)+','+str(f)+')')
    return f
# Fin modPot


# Calcula el periodo de b módulo n. Esto es, el número más pequeño per tal que b^per = 1 mod n.
def periodo(b, n):
    residuo = 100000
    per = 0
    while residuo > 1:
        per = per+1
        residuo = modPot(b,per,n)
    return per
# Fin periodo


# Encuentra una lista de todas las raices primitivas módulo n.
def primRoot(n):
    raices = []
    for i in range(2, n):
        if(periodo(i,n) == n-1):
            raices.append(i)
    return raices
#Fin primRoot


# Calcula el inverso multiplicativo de i módulo n. Si no existe devuelve 0.
# Se utiliza el algoritmo de Euclides extendido.
def inversoMult(i,n):
    x0 = 1
    x1 = 0
    x2 = 0
    y0 = 0
    y1 = 1
    y2 = 0

    a = n
    b = i % n
    r = 1
    q = 0

    while r > 0 :
        r = a % b
        q = a // b
        x2 = x0 - x1*q
        y2 = y0 - y1*q

        # Actualización de variables para la siguiente iteración.
        a = b
        b = r
        x0 = x1
        x1 = x2
        y0 = y1
        y1 = y2

    if a==1 :
        if(y0 < 0):
            y0 = y0 + n
        return y0
    else:
        return 0
#Fin inversoMult


# Calcula el logaritmo discreto de un número por fuerza bruta.
def logBruto(base, numero, modulo):
    residuo = -1
    i = 0
    while residuo != numero and i <= modulo:
        i = i+1
        residuo = modPot(base, i, modulo)
        
    if i >= modulo:
        return -1
    else:
        return i
# Fin logBruto.

# Función que factoriza un número n.
def factoriza(n):
    factores = []
    i = 2
    while n>1:
        if(n%i == 0):
            factores.append(i)
            n = n//i
        else:
            i = i+1
    return factores
#Fin factoriza


# Devuelve verdadero si algun elemento de la lista es mayor a n.
def algunMayor(lista, n):
    for elemento in lista:
        if elemento > n:
            return True
    return False
# Fin algun mayor.


# Calcula el máximo común divisor de dos números.
def mcd(n,m):
    if n<m:
        a = m
        b = n
    else:
        a = n
        b = m
    
    r=1
    while r > 0:
        r = a % b
        a = b
        b = r

    return a
# Fin mcd

# Calcula el símbolo de jacobi de a y n.
def jacobi(a,n):
    if n%2 == 0:
        return 2
    
    if a >= n:
        a = a%n
    if a == 0:
        return 0
    if a == 1:
        return 1
    
    if a<0:
        if ((n-1) // 2) % 2 == 0:
            return jacobi(-a,n)
        else:
            return -jacobi(a,n)

    if a%2 == 0:
        if ((n*n-1) // 8) % 2 == 0:
            return jacobi(a//2,n)
        else:
            return -jacobi(a//2,n)

    g = mcd(a,n)
    if a == g:
        return 0
    elif g != 1:
        return jacobi(g,n)*jacobi(a//g,n)
    elif (((a-1)*(n-1))//4) % 2 == 0:
        return jacobi(n,a)
    else:
        return -jacobi(n,a)
# Fin jacobi


print(modPot(6,16,17))



