import streamlit as st
import requests

esp_ip = "http://192.168.175.114/"

try:
    response = requests.get(esp_ip, timeout=2)
    st.write("Resposta do ESP:", response.text)
except requests.exceptions.RequestException as e:
    st.write("Erro ao conectar ao ESP:", e)
