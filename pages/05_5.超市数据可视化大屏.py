import streamlit
import streamlit.components.v1 as cp

with open('./results/数据大屏.html','r') as f:
    cp.html(f.read(),height=1000,width=3000,scrolling=True)