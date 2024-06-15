import pandas as pd
import streamlit as st
import ipeadatapy as ip
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Lista 4",
    page_icon="👋",
)

st.subheader("Exercício Projetos")

code = '''
df = pd.read_csv("https://raw.githubusercontent.com/nathalycordsil/lista4/main/projetos.csv", sep=";") 
st.dataframe(df.head(23))
'''
st.code(code, language='python')

df = pd.read_csv("https://raw.githubusercontent.com/nathalycordsil/lista4/main/projetos.csv", sep=";") 
st.dataframe(df.head(23))

st.write("O dataframe foi atualizado adicionando mais uma linha ao final com os dados referentes ao mês de dezembro de 2023.")
st.write("obs: a partir deste ponto, utilize a df atualizada, agora com 24 meses de dados")

code = '''
df1 = pd.DataFrame({'mes': [12], 'ano': [2023], 'Projeto1': [29376], 'Projeto2': [40392], 'Projeto3': [63648], 'Projeto4': [29376], 'Projeto5': [25704] })
df = pd.concat([df, df1])
print(df.tail())
'''
st.code(code, language='python')

df1 = pd.DataFrame({'mes': [12], 'ano': [2023], 'Projeto1': [29376], 'Projeto2': [40392], 'Projeto3': [63648], 'Projeto4': [29376], 'Projeto5': [25704] })
df = pd.concat([df, df1])
st.write(df.tail())

st.write("Apresentação da soma dos valores de cada projeto agrupado por ano")

code = '''
colunas = ['Projeto1', 'Projeto2', 'Projeto3', 'Projeto4', 'Projeto5']
st.write(df.groupby('ano')[colunas].sum())
'''
st.code(code, language='python')

colunas = ['Projeto1', 'Projeto2', 'Projeto3', 'Projeto4', 'Projeto5']
st.write(df.groupby('ano')[colunas].sum())

st.write("Gráfico de dispersão cruzando os dados do Projeto1 e Projeto2, com marcadores verdes e em formato de estrela")

code = '''
fig, ax = plt.subplots()
df.plot(kind = 'scatter', x = 'Projeto1', y = 'Projeto2', color='darkgreen', marker='*', ax=ax)
st.pyplot(fig)
'''
st.code(code, language='python')

fig, ax = plt.subplots()
df.plot(kind = 'scatter', x = 'Projeto1', y = 'Projeto2', color='darkgreen', marker='*', ax=ax)
st.pyplot(fig)

st.write("Gráfico do tipo histograma com os dados do Projeto 1 e Projeto4")
st.write("Dica: Ao criar dois histograma em sequência, o python agrupa em apenas um desenho")

code = '''
fig, ax = plt.subplots()
df["Projeto1"].plot(kind='hist', ax=ax)
df["Projeto4"].plot(kind='hist', ax=ax)
st.pyplot(fig)
'''
st.code(code, language='python')

fig, ax = plt.subplots()
df["Projeto1"].plot(kind='hist', ax=ax)
df["Projeto4"].plot(kind='hist', ax=ax)
st.pyplot(fig)

st.subheader("Exercício IPEADATA")

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