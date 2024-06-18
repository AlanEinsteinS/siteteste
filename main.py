import streamlit as st

st.title(body="CARACOLEEEEESSSSS!!")

name = st.text_input(label="nome",placeholder="digite seu nome")

is_clicked = st.button(label="ese é meu nome",use_container_width= True) 

if is_clicked:
    st.toast(body=f"salve, {name}")