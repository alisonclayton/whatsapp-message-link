import streamlit as st
# import pandas as pd
# from datetime import datetime, timedelta
# import plotly.graph_objs as go

wapp_link_model = "https://wa.me//55XXXXXXXXXXX?text=Tenho%20interesse%20em%20comprar%20seu%20carro"

countries = ['Brasil']

# @st.cache  ### vem sempre antes de uma função para poder trabalhar a memória cache durante a operação da função
# CRIANDO UMA BARA LATERAL
# side_bar = st.sidebar.empty()
# country_select = st.sidebar.selectbox("Selecione o país: ", countries)

wapp_number = ''
message = ''

country_select = st.selectbox("Select the countrie: ", countries)
wapp_number = st.text_input("Whatsapp phone number (just numbers with DDD): ")
message = st.text_input("Message: ")

# link_out = st.write("check out this [This is your generated link to whatsapp. Please, copy it!](https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py)")

message_list = message.split()
link_out = 'Please, copy your generated [link to whatsapp with message here!](https://wa.me//55'
link_out += wapp_number + '/?text=' + message_list[0]

for i in range(len(message_list)):
    if i < len(message_list) - 1: link_out += '%20' + message_list[i + 1]
    elif i == len(message_list): link_out += '%20' + message_list[i]

if wapp_number == '' or message == '':
    st.write("Please, fill in the fields correctly and press <ENTER>, to get your link!")
else:
    link_out += ')'
    st.markdown(link_out,unsafe_allow_html=True)
