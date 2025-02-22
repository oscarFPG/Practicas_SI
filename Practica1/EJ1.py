import pandas as pd
import numpy as np
from IPython.display import display

movies = pd.read_csv('movies_metadata.csv', dtype={ 10: 'str'})
credit = pd.read_csv('credits.csv')
ratings = pd.read_csv('ratings_small.csv')


actor = "bruce willis"
# Hacemos una subselección de los dos campos que nos interesan y los copiamos a otro dataframe
creditCast = credit["cast"].copy()

# Nos creamos una máscara con el método applymap que nos indica que campos contienen una condición que establecemos mediante una lambda
mask = (creditCast.map(lambda x: actor in str(x).lower()))

# Cast de las peliculas en las que aparece 'actor'
matches = creditCast[mask]

# Obtener el ID de las filas en 'credit' segun 'matches'
IDs = credit["id"].loc[matches.index]
display(IDs)

# Obtener dataframe segun la posicion ¿?¿?
films = movies["original_title"].loc[IDs.index]
display(films)