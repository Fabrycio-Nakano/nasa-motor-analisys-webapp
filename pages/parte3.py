import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.model_selection import train_test_split

# Definição das variáveis essenciais para a leitura dos dados
caminho_diretorio = 'https://raw.githubusercontent.com/andressaapio/nasa_dataset/main/CMAPSSData/'
indices_lista = ['motor', 'ciclo_tempo']
configuracao_lista = ['config_1', 'config_2', 'config_3']
sensores_lista = [f'sensor_{n}' for n in range(1, 22)]
colunas = indices_lista + configuracao_lista + sensores_lista

# Função para carregar os dados usando cache para melhor performance
@st.cache
def carregar_dados():
    treino = pd.read_csv(caminho_diretorio+'train_FD001.txt', sep='\s+', header=None, names=colunas)
    return treino

# Carregar dados
dados = carregar_dados()

# Título da página
st.title('Treinamento e Avaliação de Modelo de Manutenção Preditiva de Motores')

# Preparação dos dados
st.header('Preparação dos Dados')
target = 'sensor_2'  # Define o sensor que será usado como target, por exemplo
X = dados.drop(columns=[target])  # Features
y = dados[target]  # Target

# Divisão dos dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
st.write('Dados divididos em conjuntos de treino e teste.')

# Treinamento do modelo
@st.cache(allow_output_mutation=True)
def treinar_modelo(X_train, y_train):
    modelo = RandomForestRegressor(n_estimators=100, random_state=42)
    modelo.fit(X_train, y_train)
    return modelo

modelo = treinar_modelo(X_train, y_train)
st.write('Modelo treinado.')

# Avaliação do modelo
y_pred = modelo.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

st.header('Avaliação do Modelo')
st.write(f'MSE: {mse}')
st.write(f'R²: {r2}')
st.write(f'MAE: {mae}')

# Gráfico de predições vs valores reais
st.header('Comparação de Valores Reais vs. Predições')
fig, ax = plt.subplots()
ax.scatter(y_test, y_pred, alpha=0.3)
ax.set_xlabel('Valores Reais')
ax.set_ylabel('Predições')
ax.set_title('Valores Reais vs. Predições')
st.pyplot(fig)

# Importância das características
st.header('Importância das Características')
importances = modelo.feature_importances_
indices = np.argsort(importances)[::-1]
fig, ax = plt.subplots()
ax.bar(range(X_train.shape[1]), importances[indices])
ax.set_xticks(range(X_train.shape[1]))
ax.set_xticklabels(X.columns[indices], rotation=90)
ax.set_title('Importância das Características (Features)')
st.pyplot(fig)
