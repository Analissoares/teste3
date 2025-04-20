import streamlit as st
from streamlit_folium import folium_static
import folium
import requests

# Configuração da página
st.set_page_config(
    page_title="Aplicação de Mapas",
    page_icon=":world_map:",
    layout="centered"
)

def main():
    st.title("Mapas no Streamlit")
    st.subheader("AULA4")

    menu = ["Menu", "Mapa"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Menu":
        st.subheader("Página inicial")
        st.write("Bem-vindo à aplicação de mapas com Streamlit e Folium!")

    elif choice == "Mapa":
        st.subheader("Visualizar Mapa")

        # URL do arquivo GeoJSON hospedado no seu GitHub
        geojson_url = "https://raw.githubusercontent.com/Analissoares/teste3/main/data/dados_SB.geojson"

        try:
            response = requests.get(geojson_url)
            response.raise_for_status()  # Gera erro se o download falhar
            geojson_data = response.json()

            # Criar o mapa
            m = folium.Map(location=[-25.5, -49.3], zoom_start=12)
            folium.GeoJson(geojson_data, name='Sistema Bancário').add_to(m)

            # Exibir o mapa no Streamlit
            folium_static(m)

        except requests.exceptions.RequestException as e:
            st.error(f"Erro ao carregar o arquivo GeoJSON: {e}")

if __name__ == "__main__":
    main()
