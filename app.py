import streamlit as st

st.markdown("# Message Link to Wahtsapp")

st.markdown("### GET LINK")

countries = ['Brazil', 'USA', 'Portugal', 'Switzerland']

wapp_number = ''
message = ''

country_select = st.selectbox("Select the countrie: ", countries)
wapp_number = st.text_input("Whatsapp phone number (just numbers with DDD): ")
message = st.text_input("Message: ")

message_list = message.split()
link_out = 'https://wa.me//55'
msg_out = 'Please, copy your generated [link to whatsapp with message below!]('
final_out = 'Please, fill in the fields correctly and press <ENTER> to get your link!'

try:
    link_out += wapp_number + '/?text=' + message_list[0]
except (IndexError):
    final_out = "Please, fill in the fields correctly and press <ENTER> to get your link!"

for i in range(len(message_list)):
    if i < len(message_list) - 1: link_out += '%20' + message_list[i + 1]
    elif i == len(message_list): link_out += '%20' + message_list[i]

if st.button('Get Link'):
    if wapp_number != '' and message != '': 
        final_out = msg_out + link_out + ')'
        st.markdown(final_out, unsafe_allow_html=True)
        st.code(link_out)
    else: st.markdown(final_out, unsafe_allow_html=True)

st.markdown("### ABOUT")

st.markdown("This application is a simple and quick solution to a small problem encountered by those who want to quickly create a contact link via WhatsApp, to be able to distribute or publish it to people they may want to contact, without having to deal with slow problems like having to create an account or reject countless ads and advertisements, even you don't have to deal with character limitations.")
