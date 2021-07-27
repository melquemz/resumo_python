import streamlit as st
from app_resumo import sumarizar

st.markdown('<h1>MZ Resumos</h1>', unsafe_allow_html=True)

texto = st.text_area('Digite o texto que deve ser resumido')
if st.button('resumir'):

    lista_sentencas, melhores_sentencas, frequencia_palavras, nota_sentencas = sumarizar(texto, 5)

    for linha in melhores_sentencas:
        st.write(linha)

    


