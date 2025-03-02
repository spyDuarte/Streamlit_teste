import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Configuração da página
st.set_page_config(page_title="Análise de Dados", page_icon="📈", layout="wide")

# Título principal
st.title("Analisador de Dados CSV")
st.write("Carregue seu arquivo CSV para começar a análise.")

# Upload de arquivo
arquivo = st.file_uploader("Escolha um arquivo CSV", type=["csv"])

if arquivo is not None:
    # Carregar dados
    try:
        df = pd.read_csv(arquivo)
        
        # Mostrar estatísticas gerais
        st.header("Visão Geral dos Dados")
        st.write(f"Número de linhas: {df.shape[0]}")
        st.write(f"Número de colunas: {df.shape[1]}")
        
        # Mostrar primeiras linhas
        st.subheader("Amostra dos Dados")
        st.dataframe(df.head())
        
        # Estatísticas descritivas
        st.subheader("Estatísticas Descritivas")
        st.dataframe(df.describe())
        
        # Seleção de colunas para análise
        colunas_numericas = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
        if colunas_numericas:
            st.header("Análise de Colunas Numéricas")
            coluna_selecionada = st.selectbox("Selecione uma coluna para análise:", colunas_numericas)
            
            # Criar visualizações para a coluna selecionada
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader(f"Histograma - {coluna_selecionada}")
                fig_hist = px.histogram(df, x=coluna_selecionada)
                st.plotly_chart(fig_hist, use_container_width=True)
            
            with col2:
                st.subheader(f"Box Plot - {coluna_selecionada}")
                fig_box = px.box(df, y=coluna_selecionada)
                st.plotly_chart(fig_box, use_container_width=True)
            
            # Correlação entre variáveis numéricas
            st.subheader("Matriz de Correlação")
            corr = df[colunas_numericas].corr()
            fig_corr = px.imshow(corr, text_auto=True)
            st.plotly_chart(fig_corr, use_container_width=True)
            
    except Exception as e:
        st.error(f"Erro ao processar o arquivo: {e}")
else:
    # Mostrar dados de exemplo quando nenhum arquivo for carregado
    st.info("Nenhum arquivo carregado. Aqui está um exemplo de como seu aplicativo funcionará:")
    
    # Dados de exemplo
    exemplo_df = pd.DataFrame({
        'x': range(1, 11),
        'y': np.random.randn(10),
        'z': np.random.randn(10) * 2 + 5
    })
    
    st.dataframe(exemplo_df.head())
    
    # Gráfico de exemplo
    st.line_chart(exemplo_df)
