# Árbol de Decisión ID3

Este proyecto implementa el algoritmo de clasificación ID3 para la construcción de árboles de decisión. Utiliza un conjunto de datos con atributos y ejemplos de entrenamiento para crear un árbol que predice la clase de nuevos ejemplos.

## Descripción

El algoritmo ID3 selecciona el atributo con la mayor ganancia de información en cada paso y divide el conjunto de ejemplos según los valores de ese atributo. Este proceso se repite recursivamente para cada partición hasta que se alcanzan condiciones de terminación, como todos los ejemplos pertenecientes a la misma clase o la profundidad máxima del árbol.

Este proyecto tiene como objetivo proporcionar una comprensión clara del funcionamiento del algoritmo ID3, desde la lectura de datos hasta la visualización del árbol de decisión generado.

## Requisitos

- Python 3.x
- Bibliotecas necesarias:
  - `math` (incluida en la biblioteca estándar)
  - `collections` (incluida en la biblioteca estándar)
  - `networkx`
  - `matplotlib`

## Instalación de dependencias y ejecución

Puedes instalar las dependencias necesarias y ejecutar el proyecto con los siguientes comandos:

```bash
pip install networkx matplotlib
python arbol.py
