# Librerias
from fuerzaBruta import fuerza_bruta
import matplotlib.pyplot as plt
import grafos_basico

def buscar_columnas(datos):
    columnas = []
    columnas.append(datos[0][0])
    for i in range(len(datos)):
        try:
            columnas.index(datos[i][0])
        except ValueError:
            columnas.append(datos[i][0])
        try:
            columnas.index(datos[i][1])
        except ValueError:
            columnas.append(datos[i][1])
    return columnas


def crear_matriz(datos):
    columnas = buscar_columnas(datos)
    matriz = []
    for i in range(len(columnas)):
        matriz.append([0]*len(columnas))
    for nodo in datos:
        a = columnas.index(nodo[0])
        b = columnas.index(nodo[1])
        matriz[a][b] = matriz[b][a] = nodo[2]
    return matriz, columnas


def validar_nodos(Ni, Nf, columnas):
    try:
        columnas.index(Ni)
    except ValueError:
        print("Nodo no valido")
        return True
    try:
        columnas.index(Nf)
    except ValueError:
        print("Nodo no valido")
        return True
    if Ni == Nf:
        print("Nodo repetido")
        return True
    return False


def leer_nodos(columnas,datos):
    valido = True
    G=grafos_basico.crear_Grafo(datos)
    while valido:
        plt.title("Rutas")
        grafos_basico.imprimir_Grafo(G)
        print("Nodos: {}".format(columnas))
        Ni = input("Nodo de inicio: ")
        Nf = input("Nodo destino: ")
        valido = validar_nodos(Ni, Nf, columnas)
    return Ni, Nf


def imprimir_rutas(rutas_validas, N_rutas_universo):
    if N_rutas_universo != 0:
        print("Existen {} combinaciones de rutas".format(N_rutas_universo))
        if len(rutas_validas) != 0:
            print("Existen {} rutas validas entre {} y {}".format(
                len(rutas_validas), rutas_validas[0][0][0], rutas_validas[0][0][-1]))
            print("Rutas validas:")
            rutas_validas = sorted(rutas_validas, key=lambda ruta: sum(ruta[1]))
            for ruta in rutas_validas:
                print("\tRuta valida->{} costo: {}".format(ruta[0], round(sum(ruta[1]), 2)))
            print("\nMejor ruta->{}, costo: {}".format(rutas_validas[0][0], sum(rutas_validas[0][1])))
            print("Peor ruta->{}, costo: {}".format(rutas_validas[-2][0], sum(rutas_validas[-2][1])))
            G = grafos_basico.crear_GrafoD(rutas_validas[0])
            plt.title("Mejor Ruta")
            grafos_basico.imprimir_Grafo(G)
            plt.show()
        else:
            print("No existen rutas validas")
    else:
        print("No se pudieron generar rutas")


def main():
    datos = [["1","2",10],["1","3",55],["1","4",25],["1","5",45],["2","3",20],["2","4",25],["2","5",40],["3","4",15],["3","5",30],["4","5",50]]
    
    G=grafos_basico.crear_Grafo(datos)
    grafos_basico.imprimir_Grafo(G)
    matriz, nodos = crear_matriz(datos) 
    Ni, Nf = leer_nodos(nodos, datos)
    
    rutas_validas, N_rutas_universo = fuerza_bruta(matriz, nodos, Ni, Nf)
    imprimir_rutas(rutas_validas, N_rutas_universo)


main()
