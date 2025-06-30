import streamlit as st
import requests

# IP do seu ESP na rede local
esp_ip = "http://192.168.175.114/"

st.title("Conexão com ESP8266")

try:
    # Requisição GET para o ESP
    response = requests.get(esp_ip, timeout=5)
    response.raise_for_status()  # Lança erro para status HTTP != 200
    st.success("Conectado com sucesso!")
    st.text("Resposta do ESP:")
    st.code(response.text)
except requests.exceptions.Timeout:
    st.error("Tempo de conexão esgotado. O ESP pode estar offline ou inacessível.")
except requests.exceptions.ConnectionError:
    st.error("Erro de conexão. Verifique se o ESP está ligado e na mesma rede.")
except requests.exceptions.HTTPError as err:
    st.error(f"Erro HTTP: {err}")
except Exception as e:
    st.error(f"Erro inesperado: {e}")
