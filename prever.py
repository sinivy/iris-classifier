from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Carregar dataset
iris = load_iris()

X = iris.data
y = iris.target

# Separar treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Criar e treinar modelo
modelo = RandomForestClassifier(random_state=42)
modelo.fit(X_train, y_train)

print("=== Classificador de Flores Iris ===\n")

# Entrada do usuário
sepala_comprimento = float(input("Comprimento da sépala (cm): "))
sepala_largura = float(input("Largura da sépala (cm): "))
petala_comprimento = float(input("Comprimento da pétala (cm): "))
petala_largura = float(input("Largura da pétala (cm): "))

# Dados da flor
flor = [[
    sepala_comprimento,
    sepala_largura,
    petala_comprimento,
    petala_largura
]]

# Previsão
resultado = modelo.predict(flor)

# Nome da espécie
especie = iris.target_names[resultado[0]]

# Acurácia
acuracia = modelo.score(X_test, y_test)

print(f"\nAcurácia do modelo: {acuracia:.2%}")
print(f"\nEspécie prevista: {especie.capitalize()}")

probabilidades = modelo.predict_proba(flor)

print("\nProbabilidades:")

for nome, prob in zip(
    iris.target_names,
    probabilidades[0]
):
    print(f"{nome}: {prob:.2%}")