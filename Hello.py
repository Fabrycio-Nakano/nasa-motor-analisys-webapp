# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.ensemble import RandomForestRegressor

# Configurações iniciais do Seaborn
sns.set()

# Título do aplicativo
st.title("Análise Preditiva com dados públicos de motores da NASA")

# Definição do caminho dos arquivos para ler os dados
caminho_diretorio = 'https://raw.githubusercontent.com/andressaapio/nasa_dataset/main/CMAPSSData/'

# Lista de arquivos disponíveis (ajustável conforme o conteúdo do diretório)
arquivos = ["train_FD001.txt", "test_FD001.txt", "RUL_FD001.txt"]

# Selecionador de arquivo na barra lateral
arquivo_selecionado = st.sidebar.selectbox("Escolha um arquivo para análise:", arquivos)

# Carregamento dos dados
if arquivo_selecionado:
    url_completa = caminho_diretorio + arquivo_selecionado
    data = pd.read_csv(url_completa, sep=" ", header=None)  # Ajuste o delimitador conforme necessário
    
    if st.checkbox('Dataframe'):
        st.write("Dados Carregados do arquivo:", arquivo_selecionado)
        st.dataframe(data.head())

    # Algum processamento de dados, modelagem ou visualização
    if st.checkbox('Descrição Estatística'):
        st.dataframe(data.describe())

    # Visualização com Seaborn ou Matplotlib
    st.write("Visualização de Dados:")
    fig, ax = plt.subplots()
    sns.histplot(data[data.columns[0]], ax=ax, kde=True)
    st.pyplot(fig)

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


    # Implementação de algum modelo de machine learning
    # Aqui seria adicionado o treinamento e teste do modelo

# Instruções ou informações adicionais
st.sidebar.write("Instruções: Selecione um arquivo do dataset para análise.")