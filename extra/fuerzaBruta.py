from itertools import permutations


def pesos_ruta(ruta, nodos, matriz):
    peso = []
    for i in range(0, len(ruta)-1):
        a = nodos.index(ruta[i])
        b = nodos.index(ruta[i+1])
        peso.append(matriz[a][b])
    return peso


def validar_camino(ruta, Ni, Nf, matriz, nodos):
    if (ruta[0] == Ni and ruta[-1] == Nf) or (ruta[0] == Nf and ruta[-1] == Ni):
        for i in range(0, len(ruta)-1):
            a = nodos.index(ruta[i])
            b = nodos.index(ruta[i+1])
            if matriz[a][b] == 0:
                return False
        return True
    return False


def siguiente(caso, N_combinaciones):
    caso += 1
    if caso == N_combinaciones:
        return -1
    return caso


def fuerza_bruta(matriz, nodos, Ni, Nf):
    combinaciones = []
    for comb in permutations(nodos, len(nodos)):
        combinaciones.append(comb)
    caso = 0
    valido = []
    N_combinaciones = len(combinaciones)
    while caso != -1:
        ruta = combinaciones[caso]
        if validar_camino(ruta, Ni, Nf, matriz, nodos):
            temporal = [ruta]
            temporal.append(pesos_ruta(ruta, nodos, matriz))
            valido.append(temporal)
        caso = siguiente(caso, N_combinaciones)
    return valido, N_combinaciones
