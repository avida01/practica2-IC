# Árbol de Decisión ID3

Este proyecto implementa el algoritmo de clasificación ID3 para la construcción de árboles de decisión. Utiliza un conjunto de datos con atributos y ejemplos de entrenamiento para crear un árbol que predice la clase de nuevos ejemplos.

## Descripción

El algoritmo ID3 selecciona el atributo con la mayor ganancia de información en cada paso y divide el conjunto de ejemplos según los valores de ese atributo. Este proceso se repite recursivamente para cada partición hasta que se alcanzan condiciones de terminación, como todos los ejemplos pertenecientes a la misma clase o la profundidad máxima del árbol.

Este proyecto tiene como objetivo proporcionar una comprensión clara del funcionamiento del algoritmo ID3, desde la lectura de datos hasta la visualización del árbol de decisión generado.

## Requisitos

- Python 3.x
- Bibliotecas:
  - `math`
  - `collections`
  - `networkx`
  - `matplotlib`

## Archivos del Proyecto

- **`AtributosJuego.txt`**: Contiene los nombres de los atributos en formato CSV.
- **`Juego.txt`**: Contiene los ejemplos de entrenamiento, donde cada línea tiene los valores de los atributos seguidos por la clase objetivo.
- **`id3_arbol.py`**: El archivo principal con la implementación del algoritmo ID3 y la visualización del árbol de decisión.

## Estructura de los Datos

- **AtributosJuego.txt**: Archivo con los nombres de los atributos separados por comas. Ejemplo:
TiempoExterior,Temperatura,Humedad,Viento

- **Juego.txt**: Archivo con los ejemplos de entrenamiento en formato CSV. La última columna es la clase objetivo (por ejemplo, "Jugar"). Ejemplo:

## Ejecución

1. Descarga el proyecto y coloca los archivos `id3_arbol.py`, `AtributosJuego.txt` y `Juego.txt` en la misma carpeta.
2. Abre una terminal en esa carpeta.
3. Ejecuta el siguiente comando:

 ```bash
 python id3_arbol.py

