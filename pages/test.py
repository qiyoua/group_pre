import streamlit as st
from streamlit_option_menu import option_menu


selected = option_menu("", ["Home", 'Settings'], 
    icons=['house', 'gear'], menu_icon="cast", default_index=1)
selected