# 🌸 Classificador de Espécies de Flores com Machine Learning

Projeto desenvolvido em Python utilizando técnicas de Machine Learning para classificação automática de flores do dataset Iris.

O sistema utiliza algoritmos de aprendizado supervisionado para identificar a espécie de uma flor com base em medidas de sépalas e pétalas, além de fornecer métricas de desempenho e previsões interativas.

---

## Objetivo

Este projeto foi desenvolvido para praticar conceitos fundamentais de Inteligência Artificial e Machine Learning, incluindo:

- Aprendizado Supervisionado
- Treinamento de Modelos
- Avaliação de Desempenho
- Classificação Multiclasse
- Geração de Previsões
- Análise de Resultados

---

## 🌺 Dataset Utilizado

O projeto utiliza o **Iris Dataset**, um dos conjuntos de dados mais conhecidos da área de Machine Learning.

O dataset contém **150 amostras** distribuídas entre três espécies:

- Setosa
- Versicolor
- Virginica

Cada amostra possui quatro características:

- Comprimento da sépala
- Largura da sépala
- Comprimento da pétala
- Largura da pétala

---

## Tecnologias Utilizadas

- Python
- Scikit-Learn
- Pandas
- Matplotlib
- Git
- GitHub

---

## Estrutura do Projeto

```text
iris-classifier/
│
├── main.py
├── prever.py
├── requirements.txt
├── README.md
│
├── resultados/
│   └── acuracia.png
│
└── imagens/
    ├── main_execucao.png
    └── prever_execucao.png
```

---

## Funcionalidades

### Treinamento e Avaliação do Modelo

O arquivo `main.py` realiza:

- Carregamento do dataset Iris
- Separação dos dados em treino e teste
- Treinamento do modelo Random Forest
- Geração de previsões
- Cálculo da acurácia
- Exibição das previsões realizadas
- Relatório de classificação
- Matriz de confusão
- Geração de gráfico de desempenho

---

### Previsão Interativa

O arquivo `prever.py` permite que o usuário informe manualmente as características de uma flor.

Com base nesses valores, o sistema:

- Classifica a espécie da flor
- Exibe a acurácia do modelo
- Mostra as probabilidades de cada espécie

---

## Conceitos Aplicados

Durante o desenvolvimento foram aplicados os seguintes conceitos:

- Machine Learning
- Aprendizado Supervisionado
- Classificação Multiclasse
- Treinamento e Teste de Modelos
- Random Forest
- Accuracy Score
- Precision
- Recall
- F1-Score
- Matriz de Confusão
- Inferência de Modelos

---

## Como Executar

### 1. Clonar o repositório

```bash
git clone github.com/sinivy/iris-classifier
```

### 2. Acessar a pasta

```bash
cd iris-classifier
```

### 3. Criar ambiente virtual

```bash
python -m venv venv
```

### 4. Ativar ambiente virtual

Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### 5. Instalar dependências

```bash
pip install -r requirements.txt
```

---

## Executar Treinamento

```bash
python main.py
```

Exemplo de saída:

```text
Acurácia: 1.00

Real: versicolor | Previsto: versicolor
Real: setosa | Previsto: setosa
...
```

---

## Executar Previsão Interativa

```bash
python prever.py
```

Exemplo:

```text
Comprimento da sépala (cm): 5.1
Largura da sépala (cm): 3.5
Comprimento da pétala (cm): 1.4
Largura da pétala (cm): 0.2

Acurácia do modelo: 100.00%

Espécie prevista: Setosa

Probabilidades:

setosa: 98.00%
versicolor: 2.00%
virginica: 0.00%
```

---

## Resultados

O modelo apresentou desempenho superior a 95% de acurácia no conjunto de teste, demonstrando a capacidade de classificar corretamente espécies de flores a partir de características morfológicas.

---

## Demonstração

### Execução do Treinamento

![Execução do Treinamento](imagens/main_execução.jpeg)

### Previsão Interativa

<img width="930" height="288" alt="prever-iris" src="https://github.com/user-attachments/assets/9e32ed3e-d2c4-4519-a1fc-79ed5949eb01" />

![Previsão Interativa](imagens/prever_execução.jpeg)

---

## Autora

Projeto desenvolvido como prática de Machine Learning utilizando Python e Scikit-Learn por Sinivy.
