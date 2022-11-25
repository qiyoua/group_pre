import streamlit as st
import streamlit.components.v1 as cp
from streamlit_option_menu import option_menu
import base64

st.set_page_config(layout='wide',initial_sidebar_state='collapsed')

def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''
    file_ = open("./results/bk1.jpg", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("data:image/gif;base64,{data_url}");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
set_bg_hack_url()
st.markdown("""
<br></br>
<br></br>
<br></br>
<br></br>
<h1><center>基于pyecharts数据包的使用和可视化分析</center></h1>
<br></br>
<h3 style="text-align:right">小组成员:车晴 刘雨纯 徐冉 贾吉舒 邱伟明</h3>
""",unsafe_allow_html=True)
# with open('./results/GuangZhou.html') as f:
#     cp.html(f.read(),width=2000,height=2000,scrolling=True)