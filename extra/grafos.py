import networkx as nx
import matplotlib.pyplot as plt

nodos = ['Arquitectura', 'FFyL', 'Derecho', 'Ingenieria',
         'Medicina', 'Quimica', 'Anexo Ingenieria']
posiciones = [(4.54, 3.08), (4.26, 4.24), (6.26, 4.08),
              (5.8, 3.03), (7.55, 3.65), (6.82, 2.38), (5.88, 0.42)]


def imprimir_Grafo(G):
    pos = nx.get_node_attributes(G, 'pos')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, with_labels=True, pos=pos)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show(block=False)


def crear_Grafo(datos):
    G = nx.Graph()
    for i in range(len(nodos)):
        G.add_node(nodos[i], pos=posiciones[i])
    for edge in datos:
        G.add_edge(edge[0], edge[1], weight=edge[2])
    return G


def crear_GrafoD(ruta):
    G = nx.DiGraph(directed=True)
    for i in range(len(nodos)):
        G.add_node(nodos[i], pos=posiciones[i])
    for i in range(len(ruta[1])):
        G.add_edge(ruta[0][i], ruta[0][i+1], weight=ruta[1][i])
    return G
