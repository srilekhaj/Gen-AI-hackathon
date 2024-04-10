import streamlit as st
from routingprompt import navigator
 
@st.cache_resource
def initialize():
    pass
 
st.session_state.chat=initialize()
 
st.title("Customer Support Chatbot")
 
if "messages" not in st.session_state:
    st.session_state.messages = []
 
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
 
if prompt := st.chat_input("Enter Question"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
 
    response = navigator(prompt) # Backend
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
 
 
