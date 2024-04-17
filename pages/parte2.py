import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

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

treino = carregar_dados()

# Título da página
st.title('Análise Detalhada de Manutenção Preditiva de Motores')

# Estatísticas descritivas
st.header('Estatísticas Descritivas dos Dados')
st.write('Estatísticas descritivas do dataset:')
st.dataframe(treino.describe())

# Visualização da transposição de estatísticas descritivas para sensores
st.write('Estatísticas descritivas transpostas para os sensores:')
st.dataframe(treino[sensores_lista].describe().transpose())

# Heatmap de correlação
st.header('Heatmap de Correlação dos Dados')
fig, ax = plt.subplots(figsize=(15, 10))
corrmat = treino.corr()
sns.heatmap(corrmat, cmap="RdBu_r", ax=ax)
st.pyplot(fig)

# Gráficos de distribuição para algumas colunas
st.header('Gráficos de Distribuição para Colunas Selecionadas')
colunas_selecionadas = st.multiselect('Selecione colunas para visualizar distribuição', treino.columns, default=['sensor_1', 'sensor_2'])
for coluna in colunas_selecionadas:
    fig, ax = plt.subplots()
    sns.histplot(treino[coluna], kde=True, ax=ax)
    st.pyplot(fig)
