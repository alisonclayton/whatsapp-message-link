import streamlit as st

countries = ['Brasil']

wapp_number = ''
message = ''

country_select = st.selectbox("Select the countrie: ", countries)
wapp_number = st.text_input("Whatsapp phone number (just numbers with DDD): ")
message = st.text_input("Message: ")

message_list = message.split()
link_out = 'Please, copy your generated [link to whatsapp with message here!](https://wa.me//55'

try:
    link_out += wapp_number + '/?text=' + message_list[0]
except (IndexError):
    st.write("Please, fill in the fields correctly and press <ENTER> to get your link!")

for i in range(len(message_list)):
    if i < len(message_list) - 1: link_out += '%20' + message_list[i + 1]
    elif i == len(message_list): link_out += '%20' + message_list[i]

link_out += ')'

if wapp_number != '' and message != '':
    st.markdown(link_out,unsafe_allow_html=True)