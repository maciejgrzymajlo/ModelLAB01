import joblib
import numpy as np

# Wczytanie modelu
model = joblib.load('model_v1.joblib')

# Przykładowy rekord (dane iris)
sample = np.array([[5.1, 3.5, 1.4, 0.2]])  # cechy sepal length, sepal width, petal length, petal width

# Predykcja
prediction = model.predict(sample)
print("Przewidywana klasa:", prediction[0])