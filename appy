import streamlit as st
from streamlit_folium import folium_static
import folium
import requests
import json

# Configuração da página
st.set_page_config(
    page_title="Aplicação de Mapas",
    page_icon=":world_map:",
    layout="centered"
)

def main():
    st.title("Como adicionar mapas no Streamlit")
    st.subheader("Cabe nos cadernos do Colab")
    
    menu = ["Menu", "Mapa"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Menu":
        st.subheader("Página inicial")
    elif choice == "Mapa":
        st.subheader("Visualizar Mapa")

        # Carregar GeoJSON a partir de um link público do GitHub
        geojson_url = "https://raw.githubusercontent.com/SEU_USUARIO/SEU_REPOSITORIO/main/dados_SB.geojson"
        response = requests.get(geojson_url)
        geojson_data = response.json()

        # Criar o mapa
        m = folium.Map(location=[-25.5, -49.3], zoom_start=12)
        folium.GeoJson(geojson_data, name='Sistema Bancário').add_to(m)

        # Exibir o mapa no Streamlit
        folium_static(m)

if __name__ == "__main__":
    main()
