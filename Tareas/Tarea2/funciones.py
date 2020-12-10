

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


print(5575 % 162)
#print(((19*106)**2) % 163)
#print(logBruto(58,104,163))



