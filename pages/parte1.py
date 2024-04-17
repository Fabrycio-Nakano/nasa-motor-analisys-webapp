import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

# Título da página
st.title('Análise de Manutenção Preditiva de Motores')

# definição do caminho dos arquivos para ler os dados
caminho_diretorio = 'https://raw.githubusercontent.com/andressaapio/nasa_dataset/main/CMAPSSData/' 

# definição dos nomes das colunas para os índices
indices_lista = ['motor', 'ciclo_tempo']
configuracao_lista = ['config_1', 'config_2', 'config_3']

# para não precisar escrever o nome dos 21 sensores, vamos utilizar o loop for
sensores_lista = []
for n in range(1, 22):
    sensores_lista.append(f'sensor_{n}')

colunas = indices_lista + configuracao_lista + sensores_lista

treino = pd.read_csv(caminho_diretorio+'train_FD001.txt', sep='\s+', header=None, names=colunas)

# Visualização de dados básicos usando Streamlit
st.header('Visualização dos Dados de Treino')
st.write('Visualização das primeiras 5 linhas dos dados de treino:')
st.dataframe(treino.head())

st.write('Visualização das últimas 5 linhas dos dados de treino:')
st.dataframe(treino.tail())

st.write('Médias das colunas dos dados de treino:')
st.dataframe(treino.mean())

# Gráfico de um sensor específico
st.header('Gráfico de um Sensor Específico')
sensor_escolhido = st.selectbox('Escolha um sensor para visualizar', sensores_lista)
st.line_chart(treino[sensor_escolhido])

# Executar: streamlit run seu_script.py
