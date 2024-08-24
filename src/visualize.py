import os
import json
import pandas as pd
import matplotlib.pyplot as plt

def carregarResultados(diretorio="resultadosJson"):
    resultados = []
    for filename in os.listdir(diretorio):
        if filename.endswith(".json"):
            with open(os.path.join(diretorio, filename), "r") as f:
                data = json.load(f)
                resultados.append(data)
    return resultados

resultados = carregarResultados()
df = pd.DataFrame(resultados)
print(df)
print(df.columns)  # Debug print to check column names

def visualizarResultados(df):
    df['tempo'] = df['tempo'].apply(lambda x: float(x))
    df['memoria'] = df['memoria'].apply(lambda x: float(x))

    df.plot(x='algoritmo', y='tempo', kind='bar', title='Tempo de Execução por Algoritmo')
    plt.show()

    df.plot(x='algoritmo', y='memoria', kind='bar', title='Memória Utilizada por Algoritmo')
    plt.show()

visualizarResultados(df)