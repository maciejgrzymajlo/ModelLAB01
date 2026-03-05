import pandas as pd
import numpy as np
import joblib as jl
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Wczytanie danych
data = load_iris()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

# Podział na zbiór treningowy i testowy
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Trenowanie modelu
model = LogisticRegression(max_iter=100)
model.fit(X_train, y_train)

# Predykcja
y_pred = model.predict(X_test)

# Metryki
print("\nDokładność (accuracy):", accuracy_score(y_test, y_pred))
print("\nRaport klasyfikacji:")
print (classification_report(y_test, y_pred))

# Zapis
jl.dump(model, 'model_v1.joblib')
