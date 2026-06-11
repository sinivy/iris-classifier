from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# carregar dataset
iris = load_iris()

X = iris.data
y = iris.target

# separar treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# criar modelo
modelo = RandomForestClassifier(random_state=42)

# treinar
modelo.fit(X_train, y_train)

# prever
previsoes = modelo.predict(X_test)

# avaliar
acuracia = accuracy_score(y_test, previsoes)

print(f"Acurácia: {acuracia:.2f}")

for i in range(5):
    print(
        "Real:",
        iris.target_names[y_test[i]],
        "| Previsto:",
        iris.target_names[previsoes[i]]
    )

from sklearn.metrics import classification_report

print(classification_report(y_test, previsoes))

import matplotlib.pyplot as plt

plt.bar(["Acurácia"], [acuracia])
plt.title("Desempenho do Modelo")
plt.savefig("resultados/acuracia.png")

from sklearn.metrics import confusion_matrix
matriz = confusion_matrix(y_test, previsoes)

print(matriz)

flor = [[5.1, 3.5, 1.4, 0.2]]

resultado = modelo.predict(flor)

print(
    "Espécie:",
    iris.target_names[resultado[0]]
)