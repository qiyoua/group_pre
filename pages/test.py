# -*- coding: utf-8 -*-
# import  streamlit as st

from pyecharts.charts import Bar
from pyecharts import options as opts

# 2.实例化图表对象
bar = Bar(init_opts=opts.InitOpts(width='600px',height='400px'))

# 3.给图表添加数据
bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])

# 4.渲染图表
bar.render('../results/render.html')