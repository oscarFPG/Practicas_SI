import pandas as pd
import numpy as np
from IPython.display import display

movies = pd.read_csv('movies_metadata.csv', dtype={ 10: 'str'})
credit = pd.read_csv('credits.csv')
ratings = pd.read_csv('ratings_small.csv')
tested = 'lion king'

actor = "bruce willis"
#Hacemos una subselección de los dos campos que nos interesan y los copiamos a otro dataframe
creditCast = credit["cast"].copy()

# Nos creamos una máscara con el método applymap que nos indica que campos contienen una condición que establecemos mediante una lambda
mask = (creditCast.map(lambda x: actor in str(x).lower()))
display(mask)


BW = creditCast[mask]
display(BW)

#CastID = int(BW["id"].loc[BW.index[0]])
#lionId = movies[movies["title"] == "The Lion King"]["id"]
#print(BW)

#film = movies[movies["movieId"] == BW]
#display(film)

