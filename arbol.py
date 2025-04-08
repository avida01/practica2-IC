from collections import Counter
import math
import copy
import matplotlib.pyplot as plt
import networkx as nx

class Atributo:
    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id
        self.valores = []

    def set_valores(self, valores):
        self.valores = valores

    def calcular_ganancia(self, ejemplos, atributo_clase):
        total = len(ejemplos)
        entropia_total = calcular_entropia(ejemplos)

        particiones = {valor: [] for valor in self.valores}
        for e in ejemplos:
            particiones[e.valores[self.id]].append(e)

        entropia_condicional = sum(
            (len(part)/total) * calcular_entropia(part)
            for part in particiones.values() if part
        )

        return entropia_total - entropia_condicional


class Ejemplo:
    def __init__(self, valores, tipo):
        self.valores = valores  # Lista de valores del ejemplo
        self.tipo = tipo        # Clase a la que pertenece

    def get_valor(self, atributo_id):
        return self.valores[atributo_id]


class Nodo:
    def __init__(self, atributo=None, valor=None, tipo=None):
        self.atributo = atributo
        self.valor = valor
        self.tipo = tipo
        self.hijos = []

    def es_hoja(self):
        return self.tipo is not None

    def agregar_hijo(self, nodo):
        self.hijos.append(nodo)

    def imprimir(self, indent=""):
        if self.valor is not None:
            print(f"{indent}[{self.atributo.nombre} = {self.valor}]")
            indent += "  "

        if self.es_hoja():
            print(indent + f"-> {self.tipo}")
        else:
            for hijo in self.hijos:
                hijo.imprimir(indent)


class AlgoritmoID3:
    def __init__(self):
        self.posibles_valores_clase = []

    def set_posibles_valores(self, atributo_clase, ejemplos):
        valores = list(set(e.tipo for e in ejemplos))
        self.posibles_valores_clase = valores
        atributo_clase.set_valores(valores)

    def obtener_tipo_mas_comun(self, ejemplos):
        conteo = Counter(e.tipo for e in ejemplos)
        return conteo.most_common(1)[0][0]

    def obtener_ganancia_maxima(self, atributos, ejemplos, atributo_clase):
        max_ganancia = -1
        mejor = None
        for atributo in atributos[:-1]:
            if not atributo.valores:
                self.insertar_posibles_valores(atributo, ejemplos)
            ganancia = atributo.calcular_ganancia(ejemplos, atributo_clase)
            if ganancia > max_ganancia:
                max_ganancia = ganancia
                mejor = atributo
        return mejor

    def insertar_posibles_valores(self, atributo, ejemplos):
        valores = list(set(e.get_valor(atributo.id) for e in ejemplos))
        atributo.set_valores(valores)

    def filtrar_ejemplos(self, ejemplos, atributo, valor):
        return [e for e in ejemplos if e.get_valor(atributo.id) == valor]

    def id3(self, atributos, ejemplos):
        if not ejemplos:
            return None

        tipo_comun = self.obtener_tipo_mas_comun(ejemplos)
        if all(e.tipo == tipo_comun for e in ejemplos) or len(atributos) <= 1:
            return Nodo(tipo=tipo_comun)

        atributo_clase = atributos[-1]
        mejor_atributo = self.obtener_ganancia_maxima(atributos, ejemplos, atributo_clase)
        nodo = Nodo(atributo=mejor_atributo)

        for valor in mejor_atributo.valores:
            ejemplos_filtrados = self.filtrar_ejemplos(ejemplos, mejor_atributo, valor)
            atributos_restantes = [a for a in atributos if a != mejor_atributo]

            hijo = Nodo(atributo=mejor_atributo, valor=valor)
            subarbol = self.id3(copy.deepcopy(atributos_restantes), ejemplos_filtrados)

            if subarbol:
                hijo.agregar_hijo(subarbol)
            else:
                hijo.tipo = tipo_comun  
            nodo.agregar_hijo(hijo)

        return nodo


# Funciones de Utilidad

def calcular_entropia(ejemplos):
    total = len(ejemplos)
    conteo = Counter(e.tipo for e in ejemplos)
    return -sum((c/total) * math.log2(c/total) for c in conteo.values() if c != 0)

def dibujar_arbol(arbol, G=None, parent=None, node_name="root", pos_x=0, pos_y=0, layer=1):
    if G is None:
        G = nx.DiGraph()

    G.add_node(node_name, pos=(pos_x, pos_y))

    if parent:
        G.add_edge(parent, node_name)

    if arbol.es_hoja():
        G.nodes[node_name]["label"] = arbol.tipo
    else:
        if arbol.valor is not None:
            label = f"{arbol.atributo.nombre} = {arbol.valor}"
        else:
            label = f"{arbol.atributo.nombre}"
        G.nodes[node_name]["label"] = label

    # Recursivamente agregar hijos
    y_offset = 1.5
    for i, hijo in enumerate(arbol.hijos):
        if hijo is not None: 
            dibujar_arbol(hijo, G, node_name, node_name + f"_h{i}", pos_x + 1, pos_y - y_offset * (i + 1), layer + 1)

    return G



def mostrar_arbol(G):
    pos = nx.get_node_attributes(G, "pos")
    labels = nx.get_node_attributes(G, "label")

    # Mejora del estilo de la visualización
    plt.figure(figsize=(12, 12))
    nx.draw(G, pos, with_labels=False, node_size=3000, node_color="lightblue", font_size=10, font_weight="bold", arrows=False)
    nx.draw_networkx_labels(G, pos, labels=labels, font_size=8, font_weight="normal")  
    plt.axis('off')  
    plt.show()


# Cargar datos desde un archivo

def cargar_atributos(archivo):
    with open(archivo, 'r') as f:
        atributos = f.readline().strip().split(',')
    return [Atributo(nombre, idx) for idx, nombre in enumerate(atributos)]

def cargar_datos(archivo, atributos):
    ejemplos = []
    with open(archivo, 'r') as f:
        for linea in f:
            valores = linea.strip().split(',')
            tipo = valores[-1]
            ejemplo = Ejemplo(valores[:-1], tipo)
            ejemplos.append(ejemplo)
    return ejemplos


# Ejemplo de uso

if __name__ == "__main__":
    # Cargar atributos y datos desde los archivos
    atributos = cargar_atributos('AtributosJuego.txt')
    datos = cargar_datos('Juego.txt', atributos)

    id3 = AlgoritmoID3()
    id3.set_posibles_valores(atributos[-1], datos)

    arbol = id3.id3(atributos, datos)
    print("Árbol de decisión generado:\n")
    arbol.imprimir()

    # Dibuja el árbol de decisión
    G = dibujar_arbol(arbol)
    mostrar_arbol(G)
