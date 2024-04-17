import streamlit as st

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
