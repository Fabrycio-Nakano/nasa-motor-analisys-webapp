import streamlit as st

# Configuração da página
st.set_page_config(page_title='Readme - Projeto de Manutenção Preditiva')

# Título da página
st.title('Projeto de Manutenção Preditiva de Motores')

# Descrição do projeto
st.header('Sobre o Projeto')
st.write("""
Este projeto consiste em uma análise preditiva de manutenção de motores aeronáuticos utilizando dados históricos 
para treinar modelos de machine learning. O objetivo é prever o Tempo de Vida Útil Remanescente (RUL) de componentes 
de motores antes de uma falha potencial, permitindo a manutenção proativa e redução de custos e tempo de inatividade.
""")

# Componentes do projeto
st.header('Componentes do Projeto')
st.write("""
- **Parte 1: Análise Exploratória de Dados (EDA)**: Exploração inicial dos dados para entender as características 
  e a distribuição das variáveis. Inclui visualizações de estatísticas descritivas e gráficos básicos.
- **Parte 2: Análise Avançada**: Análises mais profundas incluindo correlações e visualizações avançadas para 
  identificar padrões ou anomalias.
- **Parte 3: Modelagem Preditiva**: Desenvolvimento e treinamento de modelos de machine learning para prever o RUL. 
  Inclui a avaliação de performance do modelo e visualizações de importância de características e comparação 
  de predições.
""")

# Propostas e Melhorias Futuras
st.header('Propostas para Melhorias Futuras')
st.write("""
- **Incorporação de mais dados**: Ampliar o dataset para incluir mais ciclos de vida e outros tipos de motores 
  para melhorar a robustez do modelo.
- **Exploração de novos modelos e técnicas**: Testar diferentes algoritmos de machine learning e técnicas de 
  processamento de dados para melhorar a acurácia das predições.
- **Desenvolvimento de um dashboard interativo**: Criar um dashboard mais interativo para que os usuários 
  possam executar suas próprias análises e visualizações.
- **Implementação de feedback em tempo real**: Integrar o sistema com feedback em tempo real para monitoramento 
  contínuo de condições e ajustes de manutenção.
""")

# Instruções para rodar
st.info('Para navegar pelas outras partes do projeto, utilize a barra lateral para selecionar a análise desejada.')
