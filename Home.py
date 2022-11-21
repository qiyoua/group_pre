import streamlit as st
import streamlit.components.v1 as cp


st.set_page_config(layout='wide')
with open('./results/GuangZhou.html') as f:
    cp.html(f.read(),width=2000,height=2000,scrolling=True)