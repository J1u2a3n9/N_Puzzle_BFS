import timeit
# import numpy as np
from math import factorial
from collections import deque
from estado import Estado
from random import randint

lista_vacia=[0,0,0,0]
estado_inicial = list()
estado_objetivo = list()
nodo_objetivo = Estado
nodo_comparativo=Estado(lista_vacia,None,None)
movimientos = list()
lenght = 0
side = 0
nodos_expandidos = 0



def reiniciar_valores():
    global lista_vacia,estado_inicial,estado_objetivo,nodo_objetivo,nodo_comparativo,movimientos,lenght,side,nodos_expandidos
    lista_vacia=[0,0,0,0]
    estado_inicial = list()
    estado_objetivo = list()
    nodo_objetivo = Estado
    nodo_comparativo=Estado(lista_vacia,None,None)
    movimientos = list()
    lenght = 0
    side = 0
    nodos_expandidos = 0

def mover(estado, posicion):
    nuevo_estado = estado[:]
    indice = nuevo_estado.index(0)
    if posicion == 1:  # Arriba
        if indice not in range(0, side):
            auxiliar = nuevo_estado[indice - side]
            nuevo_estado[indice - side] = nuevo_estado[indice]
            nuevo_estado[indice] = auxiliar
            return nuevo_estado
        else:
            return None
    if posicion == 2:  # Abajo
        if indice not in range(lenght - side, lenght):
            auxiliar = nuevo_estado[indice + side]
            nuevo_estado[indice + side] = nuevo_estado[indice]
            nuevo_estado[indice] = auxiliar
            return nuevo_estado
        else:
            return None
    if posicion == 3:  # Izquierda
        if indice not in range(0, lenght, side):
            auxiliar = nuevo_estado[indice - 1]
            nuevo_estado[indice - 1] = nuevo_estado[indice]
            nuevo_estado[indice] = auxiliar
            return nuevo_estado
        else:
            return None
    if posicion == 4:  # Derecha
        if indice not in range(side - 1, lenght, side):
            auxiliar = nuevo_estado[indice + 1]
            nuevo_estado[indice + 1] = nuevo_estado[indice]
            nuevo_estado[indice] = auxiliar
            return nuevo_estado
        else:
            return None


def expandir(nodo):
    global nodos_expandidos
    nodos_expandidos += 1
    vecinos = list()
    vecinos.append(Estado(mover(nodo.estado, 1), nodo, 1))
    vecinos.append(Estado(mover(nodo.estado, 2), nodo, 2))
    vecinos.append(Estado(mover(nodo.estado, 3), nodo, 3))
    vecinos.append(Estado(mover(nodo.estado, 4), nodo, 4))
    nodos = [vecino for vecino in vecinos if vecino.estado]
    return nodos

def sacar_estados_totales(estado_inicial):
    tamanio=len(estado_inicial)
    return factorial(tamanio)

def modificar_estado_inicial(estado_inicial):
    estado=Estado(estado_inicial,None,None)
    i=1
    while i<=4:
        estado_aux=mover(estado.estado,i)
        if estado_aux!=None:
            i=5
        else:
            i+=1
    return estado_aux

def modificar_estado_oficial(estado_inicial):
    estado_inicial += [estado_inicial.pop(0)]
    estado_inicial += [estado_inicial.pop(1)]
    return estado_inicial

def espacio_de_estados(estado_inicial):
    global nodo_objetivo,nodos_expandidos
    explorado = set()
    cola = deque([Estado(estado_inicial, None, None)])
    limite=sacar_estados_totales(estado_inicial)
    while cola and nodos_expandidos<limite:
        nodo = cola.pop()
        explorado.add(nodo.map)
        vecinos = expandir(nodo)
        for vecino in vecinos:
            if vecino.map not in explorado:
                cola.append(vecino)
                explorado.add(vecino.map)
    estado_perturbado=modificar_estado_oficial(estado_inicial)
    cola = deque([Estado(estado_perturbado, None, None)])
    while cola and nodos_expandidos<limite:
        nodo = cola.pop()
        explorado.add(nodo.map)
        vecinos = expandir(nodo)
        for vecino in vecinos:
            if vecino.map not in explorado:
                cola.append(vecino)
                explorado.add(vecino.map)
    



def bfs(estado_inicial, estado_objetivo):
    global nodo_objetivo
    explorado = set()
    cola = deque([Estado(estado_inicial, None, None)])
    while cola:
        nodo = cola.popleft()
        explorado.add(nodo.map)
        if nodo.estado == estado_objetivo:
            nodo_objetivo = nodo
            return cola
        vecinos = expandir(nodo)
        for vecino in vecinos:
            if vecino.map not in explorado:
                cola.append(vecino)
                explorado.add(vecino.map)


def dfs(estado_inicial, estado_objetivo):
    global nodo_objetivo
    explorado = set()
    pila = list([Estado(estado_inicial, None, None)])
    while pila:
        nodo = pila.pop()
        explorado.add(nodo.map)
        if nodo.estado == estado_objetivo:
            nodo_objetivo = nodo
            return pila
        vecinos = reversed(expandir(nodo))
        for vecino in vecinos:
            if vecino.map not in explorado:
                pila.append(vecino)
                explorado.add(vecino.map)


def dls_no_recursivo(estado_inicial, estado_objetivo, limite):
    global nodo_objetivo
    explorado = set()
    pila = list([Estado(estado_inicial, None, None)])
    cont = 0
    while pila:
        nodo = pila.pop()
        explorado.add(nodo.map)
        if nodo.estado == estado_objetivo:
            nodo_objetivo = nodo
            return pila 
        if cont < limite:
            vecinos = reversed(expandir(nodo))
            for vecino in vecinos:
                if vecino.map not in explorado:
                    pila.append(vecino)
                    explorado.add(vecino.map)
        cont += 1
        if cont == limite:
            pila = []
            return "CUTOFF"


def id(estado_inicial, estado_objetivo):
    global nodo_objetivo
    i = 1000000000
    while i < 100000000000:
        resultado = dls_no_recursivo(estado_inicial, estado_objetivo, i)
        if resultado == 'CUTOFF':
            i += 1
        else:
            i = 100000000000
    return resultado


def camino():
    nodo_actual = nodo_objetivo
    while estado_inicial != nodo_actual.estado:
        if nodo_actual.movimiento == 1:
            movimiento = 'Arriba'
        elif nodo_actual.movimiento == 2:
            movimiento = 'Abajo'
        elif nodo_actual.movimiento == 3:
            movimiento = 'Izquierda'
        else:
            movimiento = 'Derecha'
        movimientos.insert(0, movimiento)
        nodo_actual = nodo_actual.padre
    return movimientos


    



def mostrar_resultados(time):
    global movimientos
    if nodo_objetivo != nodo_comparativo:
        movimientos = camino()
        print("---------------------------------------------------------------------------------------------------------------------------")
        print()
        print("RESULTADOS")
        print("Pasos: "+str(movimientos))
        print("Numero de pasos: "+str(len(movimientos)))
        print("Numero de nodos expandidos: "+str(nodos_expandidos))
        print("Tiempo de ejecucion: " + format(time, '.8f'))
        print()
        print("---------------------------------------------------------------------------------------------------------------------------")
    else :
        print("No existe solucion")


    

def leer_estado_aleatorio(inicial):
    global lenght, side
    estado_inicial.clear()
    estado_objetivo.clear()
    for elemento in inicial:
        estado_inicial.append(int(elemento))
    lenght = len(estado_inicial)
    side = int(lenght**0.5)
    cont = 0
    while cont < lenght:
        estado_objetivo.append(int(cont))
        cont += 1


def leer_estados(inicial, final):
    global lenght, side
    estado_inicial.clear()
    estado_objetivo.clear()
    for elemento in inicial:
        estado_inicial.append(int(elemento))
    lenght = len(estado_inicial)
    side = int(lenght**0.5)
    for elementoII in final:
        estado_objetivo.append(int(elementoII))


def mapear_lista(lista):
    return list(map(int, lista))


def leer_archivo_txt(nombre, limite):
    datos = []
    aux = 1
    with open(str(nombre)+'.txt') as fname:
        for lineas in fname:
            if limite == aux:
                datos.extend(lineas.split())
            aux += 1
    return datos


def leer_de_archivo(nombre):
    estado_inicial = []
    estado_objetivo = []
    i = 0
    while i < 2:
        if i == 0:
            estado_inicial = leer_archivo_txt(nombre, 1)
        if i == 1:
            estado_objetivo = leer_archivo_txt(nombre, 2)
        i += 1
    estado_inicial = mapear_lista(estado_inicial)
    estado_objetivo = mapear_lista(estado_objetivo)
    leer_estados(estado_inicial, estado_objetivo)


def generar_tablero_aleatorio(tamanio):
    estado_inicial_aux = []
    cont = 0
    while cont <= (tamanio*tamanio-1):
        num_aleatorio = randint(0, (tamanio*tamanio)-1)
        if num_aleatorio in estado_inicial_aux:
            pass
        else:
            estado_inicial_aux.append(num_aleatorio)
            cont += 1
    return estado_inicial_aux


# def mostrar_puzzle(puzzle):
    if lenght == 16:
        puzzle_nuevo = np.array(puzzle).reshape(4, 4)
    if lenght == 9:
        puzzle_nuevo = np.array(puzzle).reshape(3, 3)
    if lenght == 4:
        puzzle_nuevo = np.array(puzzle).reshape(2, 2)
    if lenght == 0:
        puzzle_nuevo = []
    print(puzzle_nuevo)


def sub_main(tamanio):
    opcion = 0
    aleatorio = generar_tablero_aleatorio(tamanio)
    leer_estado_aleatorio(aleatorio)
    print("Puzzle a resolver")
    print(estado_inicial)
    # mostrar_puzzle(estado_inicial)
    print("Estado Objetivo si se elige una funcion de busqueda")
    print(estado_objetivo)
    # mostrar_puzzle(estado_objetivo)
    generar_tablero_aleatorio(tamanio)
    print("Escoger una opcion")
    print("1)Resolver por BFS")
    print("2)Resolver por DLS")
    print("3)Resolver por dfs")
    print("4)Resolver por Iterative Deepening")
    print("5)Sacar numero total de estados")
    print("Por favor ingrese una opcion: ")
    opcion = int(input())
    if opcion == 1:
        inicio = timeit.default_timer()
        bfs(estado_inicial, estado_objetivo)
        final = timeit.default_timer()
        mostrar_resultados(final-inicio)
    if opcion == 2:
        inicio = timeit.default_timer()
        respuesta = dls_no_recursivo(estado_inicial, estado_objetivo, 181440)
        if respuesta == "CUTOFF":
            print("No se encontro una solucion en el limite")
        else:
            final = timeit.default_timer()
            mostrar_resultados(final-inicio)
    if opcion == 3:
        inicio = timeit.default_timer()
        dfs(estado_inicial, estado_objetivo)
        final = timeit.default_timer()
        mostrar_resultados(final-inicio)
    if opcion == 4:
        inicio = timeit.default_timer()
        respuesta = id(estado_inicial, estado_objetivo)
        if respuesta == "CUTOFF":
            print("No se encontro una solucion en el limite")
        else:
            final = timeit.default_timer()
            mostrar_resultados(final-inicio)
    if opcion==5:
        inicio = timeit.default_timer()
        espacio_de_estados(estado_inicial)
        final = timeit.default_timer()
        print("El numero de estados es: "+str(nodos_expandidos))
        print("Tiempo de ejecucion: " + format(final-inicio, '.8f'))




def main():
    
    opcion = 1
    while opcion >= 1 and opcion <= 6:
        
        print("Bienvenido a N puzzle")
        print("1)Leer por archivo estado inicial y objetivo")
        print("2)Resolver por BFS")
        print("3)Resolver por DLS")
        print("4)Resolver por dfs")
        print("5)Resolver por Iterative Deepening")
        print("6)Probar Aleatoriamente")
        print("Por favor ingrese una opcion: ")
        opcion = int(input())
        if opcion == 1:
            print("Ingrese el nombre del archivo")
            nombre = input()
            leer_de_archivo(nombre)
        if opcion == 2:
            inicio = timeit.default_timer()
            bfs(estado_inicial, estado_objetivo)
            final = timeit.default_timer()
            mostrar_resultados(final-inicio)
        if opcion == 3:
            inicio = timeit.default_timer()
            respuesta = dls_no_recursivo(
                estado_inicial, estado_objetivo, 181440)
            if respuesta == "CUTOFF":
                print("No se encontro una solucion en el limite")
            else:
                final = timeit.default_timer()
                mostrar_resultados(final-inicio)
        if opcion == 4:
            inicio = timeit.default_timer()
            dfs(estado_inicial, estado_objetivo)
            final = timeit.default_timer()
            mostrar_resultados(final-inicio)
        if opcion == 5:
            inicio = timeit.default_timer()
            respuesta = id(estado_inicial, estado_objetivo)
            if respuesta == "CUTOFF":
                print("No se encontro una solucion en el limite")
            else:
                final = timeit.default_timer()
                mostrar_resultados(final-inicio)
        if opcion == 6:
            print("Ingrese el tamanio de la matriz: ")
            tamanio = int(input())
            sub_main(tamanio)


if __name__ == '__main__':
    main()

