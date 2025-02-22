import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

housing = datasets.fetch_california_housing()

# Ver propiedades del objeto -> Compilador no ofrece sugerencias
# print(dir(housing))

# Ver las columnas del dataset
# print(housing.feature_names)

# Valores de prueba
housing_x = housing.data[:, np.newaxis, 1]
train_x = housing_x[:-40]    # Todos menos los 40 ultimos -> Tener 20600
test_x = housing_x[-10:]     # Desde el puesto 10 hasta el final

# Valores esperados
train_y = housing.target[:-40]
test_y = housing.target[-10:]

# Crear recta de regresion linear
linear_regression = linear_model.LinearRegression()
linear_regression.fit(train_x, train_y)

# Predicción
prediccion = linear_regression.predict(test_x)


print("Mostramos los valores obtenidos por la regresión lineal")
print('Coeficientes: \n', linear_regression.coef_)
print("MSE: %.2f"% mean_squared_error(test_y, prediccion))
print('R2: %.2f' % r2_score(test_y, prediccion))