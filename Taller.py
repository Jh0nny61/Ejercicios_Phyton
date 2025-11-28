from pandas import Series
import numpy as np
import random
 
list_random = [random.randint(1, 100) for _ in range(10)]
serie = Series(list_random, index=range(1, 11), name="Numero aleatorio")
serie.index.name = "idx"
serie_cuad = serie ** 2
ultm_4 = serie_cuad.tail(4)
may500 = serie_cuad[serie_cuad > 500].tolist()
print("La lista aleatoria es:", list_random)
print("\nSu serie original:\n", serie)
print("\nSerie de cuadrados:\n", serie_cuad)
print("\nLos ultimos 4 elementos son:\n", ultm_4)
print("\nLos valores mayores a 500 (como lista):", may500)