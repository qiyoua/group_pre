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
             background: url("https://ts1.cn.mm.bing.net/th/id/R-C.773df84f18ad88b4c92d7875f9f26130?rik=o%2bndsKTQORcCZA&riu=http%3a%2f%2fwww.686ppt.com%2fd%2ffile%2fp%2flouyujing%2f2020nian%2f6.19%2f36_7.jpg&ehk=nX9exFQDWmUW%2bPKRLEJqV9v%2bzdyxS2ckXOPnrp%2fLk9s%3d&risl=&pid=ImgRaw&r=0");
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
<h1><center>这里是小组标题,还没想好</center></h1>
<br></br>
<h3 style="text-align:right">小组成员:车晴 刘雨纯 徐冉 贾吉舒 邱伟明</h3>
""",unsafe_allow_html=True)
# with open('./results/GuangZhou.html') as f:
#     cp.html(f.read(),width=2000,height=2000,scrolling=True)