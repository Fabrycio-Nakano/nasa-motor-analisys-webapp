import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

# Caminho base onde os datasets estão armazenados
caminho_diretorio = 'https://raw.githubusercontent.com/andressaapio/nasa_dataset/main/CMAPSSData/'



# Função para preparar o y_test alinhado ao X_test
def preparar_y_test(dados_teste, dados_rul):
    # Identificar o último ciclo de cada motor em dados_teste
    ultimo_ciclo = dados_teste.groupby('motor').max().reset_index()[['motor', 'ciclo_tempo']]
    # Mesclar com os dados_rul para alinhar o RUL com o último ciclo de cada motor
    y_test_preparado = pd.merge(ultimo_ciclo, dados_rul, on='motor', how='left')
    return y_test_preparado['RUL']

# Definindo uma função para carregar dados
@st.cache
def carregar_dados(nome_arquivo):
    colunas = ['motor', 'ciclo_tempo', 'config_1', 'config_2', 'config_3'] + [f'sensor_{n}' for n in range(1, 22)]
    url = caminho_diretorio + nome_arquivo
    data = pd.read_csv(url, sep='\\s+', header=None, names=colunas)
    return data

# Carregar datasets
dados_treino = carregar_dados('train_FD001.txt')
dados_teste = carregar_dados('test_FD001.txt')
dados_rul = carregar_dados('RUL_FD001.txt')

# Preparar os dados (simplificação para exemplo)
X_train = dados_treino.iloc[:, 2:]  # Excluindo identificadores
y_train = dados_treino['ciclo_tempo']
X_test = dados_teste.iloc[:, 2:]
y_test = dados_rul.iloc[:, 0]  # RUL real

# Construindo e treinando o modelo
@st.cache(allow_output_mutation=True)
def treinar_modelo(X, y):
    modelo = RandomForestRegressor(n_estimators=100)
    modelo.fit(X, y)
    return modelo

modelo = treinar_modelo(X_train, y_train)

# Fazendo previsões
predicoes = modelo.predict(X_test)

# Métricas de desempenho
mse = mean_squared_error(y_test, predicoes)
r2 = r2_score(y_test, predicoes)
mae = mean_absolute_error(y_test, predicoes)

# Mostrar os resultados no app
st.write("Métricas de Desempenho do Modelo:")
st.write(f"MSE: {mse}")
st.write(f"R2: {r2}")
st.write(f"MAE: {mae}")
