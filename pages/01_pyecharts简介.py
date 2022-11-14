import streamlit as st
import streamlit.components.v1 as cp

st.set_page_config(layout='wide')



tab1,tab2 = st.tabs(['1.pyecharts介绍','2.从一个图表看pyecharts的结构'])

with tab1:
    """
    ### 📣 概况

    ECharts是一个纯Javascript的图表库，可以流畅的运行在PC和移动设备上，兼容当前绝大部分浏览器,提供直观、生动、可交互、可高度个性化定制的数据可视化图表。ECharts提供了常规的折线图、柱状图、散点图、饼图、K线图，用于统计的盒形图，用于地理数据可视化的地图、热力图、线图，用于关系数据可视化的关系图、treemap，多维数据可视化的平行坐标，还有用于BI的漏斗图、仪表盘，并且支持图与图之间的混搭。

    [Echarts](https://github.com/ecomfe/echarts)是一个由百度开源的数据可视化，凭借着良好的交互性，精巧的图表设计，得到了众多开发者的认可。而 Python 是一门富有表达力的语言，很适合用于数据处理。当数据分析遇上数据可视化时，[pyecharts](https://github.com/pyecharts/pyecharts)诞生了。

    pyecharts 是一个用于生成 Echarts 图表的类库。实际上就是 Echarts 与 Python 的对接。使用 pyecharts 可以生成独立的网页，也可以在 flask ， Django 中集成使用。

    ### ✨ 特性

    - 简洁的 API 设计，使用如丝滑般流畅，支持链式调用

    - 囊括了 30+ 种常见图表，应有尽有

    - 支持主流 Notebook 环境，Jupyter Notebook 和 JupyterLab

    - 可轻松集成至 Flask，Django 等主流 Web 框架

    - 高度灵活的配置项，可轻松搭配出精美的图表

    - 详细的文档和示例，帮助开发者更快的上手项目

    - 多达 400+ 地图文件以及原生的百度地图，为地理数据可视化提供强有力的支持

    ### 示例

    [ECharts图表示例](https://echarts.apache.org/examples/zh/index.html)

    [pyeharts图表示例](https://gallery.pyecharts.org/#/README)

    ### ⏳ 版本

    pyecharts 分为 v0.5.X 和 v1 两个大版本，v0.5.X 和 v1 间不兼容，v1 是一个全新的版本，详见[ISSUE#892](https://github.com/pyecharts/pyecharts/issues/892)，[ISSUE#1033](https://github.com/pyecharts/pyecharts/issues/1033)。

    ### pip 安装

    ```
    pip(3) install pyecharts
    ```

    ### 查看版本号

    ```python
    import pyecharts

    print(pyecharts.__version__)
    ```
        """


with tab2:
    st.markdown('<h4><center>从简单的图表开始</center></h4>',unsafe_allow_html=True)
    col1,col2 = st.columns([1,1])
    with col1:
        st.markdown('<center>创建一个图表,做好以下五步即可</center>',unsafe_allow_html=True)
        st.code("""
# 1.导入该图表的对象
from pyecharts.charts import Bar

# 2.实例化图表对象
bar = Bar()

# 3.给图表添加数据
bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])

# 4.渲染图表
bar.render()
# render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# 也可以传入路径参数，如 bar.render("mycharts.html")

# 在notebook里面渲染图表
bar.render_notebook()

# 5.保存图表
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot

make_snapshot(snapshot, bar.render(), "bar.png")
    """)
        """其中几步也可以通过`.`来链式调用"""
        st.code("""
from pyecharts.charts import Bar

bar = (
    Bar()
    .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    .render('sample_bar.html')
)
    """)

    
        """也可以更改图表主题"""
        st.code("""
from pyecharts.charts import Bar
from pyecharts import options as opts
# 内置主题类型可查看 pyecharts.globals.ThemeType
from pyecharts.globals import ThemeType

bar = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    .add_yaxis("商家B", [15, 6, 45, 20, 35, 66])
    .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题")))
bar.render_notebook()
        """)

    with col2:
        # cp.html("<br></br>")
        with open('./results/sample_bar.html','r') as f:
            st.caption("""<center>由左边的代码生成的一个简单的柱状图</center>""",unsafe_allow_html=True)
            cp.html(f.read(),scrolling=True,height=500)
        st.image('图表.png')
        # cp.html("<br></br>")
        with open('./results/theme.html','r') as f:
            st.markdown("""<center>更改主题后的图表</center>""",unsafe_allow_html=True)
            cp.html(f.read(),scrolling=True,height=500)
        
    
        
            
    