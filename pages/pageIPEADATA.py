import pandas as pd
import streamlit as st
import ipeadatapy as ip
import matplotlib.pyplot as plt

st.markdown("# IPEADATA")
st.sidebar.markdown("# IPEADATA")

#cabeçalho
st.write('Busca na base do IPEADATA os indicadores relacionados a taxa de juros Selic. O objetivo é encontrar o código correspondente ao indicador "Taxa de juros - Over / Selic - acumulada no mês"')

code = '''
st.write(ip.list_series('Selic'))
'''
st.code(code, language='python')

st.write(ip.list_series('Selic'))

st.write('Utilização da biblioteca do IPEADATA para apresentar os valores do indicador "Taxa de juros - Over / Selic - acumulada no mês" dos anos de 2022 e 2023"')

code = '''
selic = ip.timeseries('BM12_TJOVER12', yearGreaterThan=2021, yearSmallerThan=2024)
st.write(selic)
'''
st.code(code, language='python')

selic = ip.timeseries('BM12_TJOVER12', yearGreaterThan=2021, yearSmallerThan=2024)
st.write(selic)

st.write("Gráficos de linha, apresentando os meses e valores das taxas, um para o ano de 2022 e outro para o ano de 2023")

code = '''
fig, ax = plt.subplots()
ip.timeseries('BM12_TJOVER12', year=2021).plot("MONTH", "VALUE ((% a.m.))", ax=ax)
ip.timeseries('BM12_TJOVER12', year=2022).plot("MONTH", "VALUE ((% a.m.))", ax=ax)
st.pyplot(fig)
'''
st.code(code, language='python')

fig, ax = plt.subplots()
ip.timeseries('BM12_TJOVER12', year=2021).plot("MONTH", "VALUE ((% a.m.))", ax=ax)
ip.timeseries('BM12_TJOVER12', year=2022).plot("MONTH", "VALUE ((% a.m.))", ax=ax)
st.pyplot(fig)