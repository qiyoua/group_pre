import streamlit as st
import streamlit.components.v1 as cp
from streamlit_option_menu import option_menu

st.set_page_config(layout='wide')

def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://cdn.pixabay.com/photo/2020/06/19/22/33/wormhole-5319067_960_720.jpg");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
set_bg_hack_url()
st.markdown("sdfsafasfasdfasdfssfsafasfsfasfs")
# with open('./results/GuangZhou.html') as f:
#     cp.html(f.read(),width=2000,height=2000,scrolling=True)