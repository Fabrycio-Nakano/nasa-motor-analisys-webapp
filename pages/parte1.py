import streamlit as st
import pandas as pd

# Caminho base onde os datasets estão armazenados
caminho_diretorio = 'https://raw.githubusercontent.com/andressaapio/nasa_dataset/main/CMAPSSData/'

# Nome dos arquivos dos datasets
datasets = {
    'Treino': 'train_FD001.txt',
    'Teste': 'test_FD001.txt',
    'RUL': 'RUL_FD001.txt'
}

# Escolha do dataset pelo usuário
opcao_dataset = st.sidebar.selectbox('Escolha o dataset:', list(datasets.keys()))

# Carregar o dataset selecionado
@st.cache
def carregar_dados(nome_arquivo):
    colunas = ['motor', 'ciclo_tempo', 'config_1', 'config_2', 'config_3'] + [f'sensor_{n}' for n in range(1, 22)]
    url = caminho_diretorio + nome_arquivo
    data = pd.read_csv(url, sep='\\s+', header=None, names=colunas)
    return data

dados = carregar_dados(datasets[opcao_dataset])

# Mostrar os dados no app
st.write(f'Dataset escolhido: {opcao_dataset}')
st.write(dados.head())
