import streamlit as st

st.title('Mubify')

name = st.text_input('Introduce your name', 'John Doe')

if st.button('Submit'):
    st.write(f'Hello, {name}!')