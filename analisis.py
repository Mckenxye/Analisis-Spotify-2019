import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
st.set_page_config (page_icon= 'spotify.png', 
                    page_title= 'Top 50 Spotify - 2019',
                    layout= 'centered')

df= pd.read_csv("top50.csv", encoding='latin-1')
df = df.drop(['Beats.Per.Minute', 'Energy', 'Danceability', 'Liveness', 'Loudness..dB..', 'Valence.', 'Length.', 'Acousticness..', 'Speechiness.'], axis=1)
df = df.rename(columns={'Track.Name': 'Cancion', 'Artist.Name': 'Artista', 'Genre': 'Genero', 'Unnamed: 0':'Codigo', 'Popularity':'Popularidad'})

# Menu de Navegacion
with st.sidebar: 
  st.image ('spotify.png', use_column_width= True)
  st.header('Opciones', divider= 'green')
  numhead = st.slider ('Digite rango para analizar las distintas opciones', min_value= 5,max_value=50)



# Título de la aplicación Streamlit
st.title(':green[Top 50 Canciones Spotify - 2019] 🎧')
st.dataframe(df, hide_index= True ,use_container_width=True)

# Crear la gráfica para popularidad de genero
df_gen = df.groupby('Genero')['Popularidad'].sum().reset_index()
df_gen = df_gen.sort_values(by='Genero', ascending= False)
st.header('Generos mas Escuchados', divider='green')
st.bar_chart(df_gen.set_index('Genero')['Popularidad'].head(numhead))

# Crear grafica para Artista mas escuchado
df_art = df.groupby('Artista')['Popularidad'].sum().reset_index()
df_art = df_art.sort_values(by='Artista', ascending= False)
st.header('Artistas mas Escuchados', divider= 'green')
st.bar_chart(df_art.set_index('Artista')['Popularidad'].head(numhead))

# Crear grafica para las 10 canciones mas escuchadas
df_song = df.groupby('Cancion')['Popularidad'].sum().reset_index()
df_song = df_song.sort_values(by='Cancion', ascending= False)
st.header('Top 10 Canciones mas Escuchados', divider= 'green')
st.bar_chart(df_song.set_index('Cancion')['Popularidad'].head(numhead))




