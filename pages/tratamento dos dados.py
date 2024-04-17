import streamlit as st
import pandas as pd

# Título do aplicativo
st.title("Lista de Sensores")

# Definição dos nomes das colunas para os índices
indices_lista = ['motor', 'ciclo_tempo']
configuracao_lista = ['config_1', 'config_2', 'config_3']

# Geração da lista de sensores usando compreensão de lista
sensores_lista = [f'sensor_{i}' for i in range(1, 22)]

# Exibindo as listas
st.write("Índices de Monitoramento:")
st.write(indices_lista)
st.write("Configurações:")
st.write(configuracao_lista)
st.write("Sensores:")
st.write(sensores_lista)

# Título do aplicativo
st.title("Análise de Dados de Motores")

# Definição do caminho dos arquivos para ler os dados
caminho_diretorio = 'https://raw.githubusercontent.com/andressaapio/nasa_dataset/main/CMAPSSData/'

# Definição dos nomes das colunas para os índices e sensores
indices_lista = ['motor', 'ciclo_tempo']
configuracao_lista = ['config_1', 'config_2', 'config_3']
sensores_lista = [f'sensor_{i}' for i in range(1, 22)]
colunas = indices_lista + configuracao_lista + sensores_lista

# Escolha do arquivo para análise através de um seletor na barra lateral
arquivo_opcoes = {
    "Treino": "train_FD001.txt",
    "Teste": "test_FD001.txt",
    "RUL": "RUL_FD001.txt"
}
opcao_selecionada = st.sidebar.selectbox("Escolha o dataset para análise:", list(arquivo_opcoes.keys()))

# Carregamento dos dados
if opcao_selecionada:
    arquivo = arquivo_opcoes[opcao_selecionada]
    if arquivo == "RUL_FD001.txt":
        dados = pd.read_csv(caminho_diretorio + arquivo, sep='\s+', header=None, names=['RUL'])
    else:
        dados = pd.read_csv(caminho_diretorio + arquivo, sep='\s+', header=None, names=colunas)
    st.write(f"Dados Carregados do arquivo: {arquivo}")
    st.dataframe(dados.head())

    # Visualização estatística descritiva se o dataset não for o RUL
    if arquivo != "RUL_FD001.txt":
        st.write("Descrição Estatística:")
        st.dataframe(dados.describe())