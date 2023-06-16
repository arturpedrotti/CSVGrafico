import pandas as pd
import streamlit as st
import plotly.graph_objects as go

# Carregando o arquivo csv
@st.cache_resource  # Esta função guarda os resultados de load_data() no cache, assim, o arquivo csv não é recarregado toda vez que a função é chamada.
# No Streamlit, cada vez que um usuário interage com algo, o script é executado novamente. Por isso, o cache é útil.
def load_data():
    df = pd.read_csv('mars-weather.csv', parse_dates=['terrestrial_date'])
    df.set_index('terrestrial_date', inplace=True)
    return df

df = load_data()

# Mostrar apenas as primeiras linhas do DataFrame inicialmente
st.dataframe(df.head())

# Forneça uma opção de checkbox para mostrar o DataFrame completo
if st.checkbox('Mostrar dados completos'):
    # Disponibilizando dados em uma tabela sem o índice
    st.markdown(df.to_html(index=False), unsafe_allow_html=True)

# Desenhando o gráfico de linhas para a temperatura mínima, máxima e a pressão contra a data
fig = go.Figure()

# Adicionando as linhas de temperatura mínima, máxima e pressão no gráfico
fig.add_trace(go.Scatter(x=df.index, y=df['min_temp'], mode='lines', name='Temp Min'))
fig.add_trace(go.Scatter(x=df.index, y=df['max_temp'], mode='lines', name='Temp Max'))
fig.add_trace(go.Scatter(x=df.index, y=df['pressure'], mode='lines', name='Pressão'))

# Configurando os rótulos do gráfico em português
fig.update_layout(
    title='Dados de Temperatura e Pressão',
    xaxis_title='Data Terrestre',
    yaxis_title='Valor',
    hovermode="x"  # Define o modo de hover para mostrar as informações ao passar o mouse sobre o gráfico
)

# Mostrando o gráfico interativo no Streamlit
st.plotly_chart(fig)
