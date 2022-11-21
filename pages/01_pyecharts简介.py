import streamlit as st
import streamlit.components.v1 as cp
import streamlit_option_menu as som
from pyecharts import options as opts
from pyecharts.charts import Bar,Line
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType
from pyecharts.globals import RenderType
from pyecharts.faker import Faker 

st.set_page_config(layout='wide')

tab1,tab2,tab3 = st.tabs(['1.pyecharts介绍','2.从一个图表看pyecharts的结构','3.pyecharts图表的配置项'])

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

with tab3:
    st.code("""
    from pyecharts import options as opts
from pyecharts.charts import Bar,Line
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType
from pyecharts.globals import RenderType
from pyecharts.faker import Faker 
    """)
    st.markdown("""<h3><center>初始化配置项</center></h3>""",unsafe_allow_html=True)
    col1,col2 = st.columns([1,1])
    with col1:
        with st.echo():
            c = Bar(init_opts=opts.InitOpts(
                width='400px',
                height='400px',
                # chart_id='这里设置id,可选',
                renderer=RenderType.SVG,
                page_title='网页标题',
                theme='white',
                bg_color='white',
                animation_opts=opts.AnimationOpts()
            )
                )
            c = (
                c.add_xaxis(Faker.choose())
                .add_yaxis("商家A", Faker.values(), stack="stack1")
                .add_yaxis("商家B", Faker.values(), stack="stack1")
                )
            c.render('./results/opts1.html')
    with col2:
        with open('./results/opts1.html','r') as f:
            content = f.read()
            cp.html(content,width=500,height=400,scrolling=True)

    st.markdown("""<h3><center>动画配置项</center></h3>""",unsafe_allow_html=True)
    col1,col2 = st.columns([1,1])
    with col1:
        with st.echo():
            c = (
                Bar(init_opts=opts.InitOpts(width='400px',height='300px'
                ,animation_opts=opts.AnimationOpts(
                    animation=False)))
                .add_xaxis(Faker.choose())
                .add_yaxis("商家A", Faker.values(), stack="stack1")
                .add_yaxis("商家B", Faker.values(), stack="stack1")
                .set_global_opts()
                )
            c.render('./results/opts2.html')
    with col2:
        with open('./results/opts2.html','r') as f:
            content = f.read()
            cp.html(content,width=500,height=300,scrolling=True)
    
    st.markdown("""<h3><center>标题配置项</center></h3>""",unsafe_allow_html=True)
    col1,col2 = st.columns([1,1])
    with col1:
        with st.echo():
            c = (
                Bar(init_opts=opts.InitOpts(width='400px',height='400px'))
                .add_xaxis(Faker.choose())
                .add_yaxis("商家A", Faker.values(), stack="stack1")
                .add_yaxis("商家B", Faker.values(), stack="stack1")
                .set_global_opts(title_opts=opts.TitleOpts(
                title='这里写title',
                title_link='https://pyecharts.org/#/zh-cn/global_options',
                title_target='blank',
                subtitle='这里写副标题',
                pos_left='right',
                pos_top='top',
                title_textstyle_opts=None,
                subtitle_textstyle_opts=None))
                )
            c.render('./results/opts3.html')

    with col2:
        with open('./results/opts3.html','r') as f:
            content = f.read()
            cp.html(content,width=500,height=400,scrolling=True)
    
    st.markdown("""<h3><center>坐标轴配置项</center></h3>""",unsafe_allow_html=True)
    col1,col2 = st.columns([1,1])
    with col1:
        with st.echo():
            c = (
                    Bar(init_opts=opts.InitOpts(width='750px',height='800px'))
                    .add_xaxis(
                        [
                            "名字很长的X轴标签1",
                            "名字很长的X轴标签2",
                            "名字很长的X轴标签3",
                            "名字很长的X轴标签4",
                            "名字很长的X轴标签5",
                            "名字很长的X轴标签6",
                        ]
                    )
                    .add_yaxis("商家A", [10, 20, 30, 40, 50, 40])
                    .add_yaxis("商家B", [20, 10, 40, 30, 40, 50])
                    .set_global_opts(
                        xaxis_opts=opts.AxisOpts(type_=None,
                                        name='坐标轴名称',
                                        is_show=True,
                                        is_scale=True,
                                        is_inverse=False,
                                        name_location='end',
                                        name_gap=15,
                                        name_rotate=-15,
                                        position='bottom',
                                        axislabel_opts=opts.LabelOpts(rotate=-15)),
                        title_opts=opts.TitleOpts(title="Bar-旋转X轴标签",
                            subtitle="解决标签名字过长的问题"),
                        yaxis_opts=opts.AxisOpts(min_=0,
                                        max_=60,
                                        axisline_opts=opts.AxisLineOpts(
                                        is_show=True,
                                        linestyle_opts=opts.LineStyleOpts(
                                        is_show=True,
                                        width=1,
                                        opacity=1)),
                                        axislabel_opts=opts.LabelOpts(is_show=True,
                                        position='top',
                                        color='red',
                                        font_size=15,
                                        font_style='italic',
                                        font_weight='bold',
                                        font_family='serif',
                                        rotate=15,
                                        margin=20,
                                        formatter="{value} /月")
                    )
                    )
                    
                )
            c.render('./results/opts4.html')
    with col2:
        with open('./results/opts4.html','r') as f:
            content = f.read()
            cp.html(content,width=800,height=800,scrolling=True)

    st.markdown("""<h3><center>xy轴交换</center></h3>""",unsafe_allow_html=True)
    col1,col2 = st.columns([1,1])
    with col1:
        with st.echo():
            c = (
                Bar(init_opts=opts.InitOpts(width='500px',height='300px'))
                .add_xaxis(Faker.choose())
                .add_yaxis("商家A", Faker.values())
                .add_yaxis("商家B", Faker.values())
                .reversal_axis()
                .set_series_opts(label_opts=opts.LabelOpts(position="right"))
                .set_global_opts(title_opts=opts.TitleOpts(title="Bar-翻转 XY 轴"))
            )
            c.render('./results/opts5.html')
    with col2:
        with open('./results/opts5.html','r') as f:
            content = f.read()
            cp.html(content,width=600,height=300,scrolling=True)
    
    st.markdown("""<h3><center>标记配置项</center></h3>""",unsafe_allow_html=True)
    col1,col2 = st.columns([1,1])
    with col1:
        with st.echo():
            c = (
                Bar(init_opts=opts.InitOpts(width='600px',height='450px'))
                .add_xaxis(Faker.choose())
                .add_yaxis("商家A", Faker.values())
                .add_yaxis("商家B", Faker.values())
                .set_global_opts(title_opts=opts.TitleOpts(title="Bar-MarkPoint（指定类型）"))
                .set_series_opts(
                    label_opts=opts.LabelOpts(is_show=False),
                    markpoint_opts=opts.MarkPointOpts(
                        data=[
                            opts.MarkPointItem(type_="max", name="最大值"),
                            opts.MarkPointItem(type_="min", name="最小值"),
                            opts.MarkPointItem(type_="average", name="平均值"),
                        ]
                    ),
                )
            )
            c.render('./results/opts6.html')
    with col2:
        with open('./results/opts6.html','r') as f:
            content = f.read()
            cp.html(content,width=600,height=450,scrolling=True)
    
    col1,col2 = st.columns([1,1])
    with col1:
        with st.echo():
            c = (
                Bar(init_opts=opts.InitOpts(width='600px',height='400px'))
                .add_xaxis(Faker.choose())
                .add_yaxis("商家A", Faker.values())
                .add_yaxis("商家B", Faker.values())
                .set_global_opts(title_opts=opts.TitleOpts(title="Bar-MarkLine（指定类型）"))
                .set_series_opts(
                    label_opts=opts.LabelOpts(is_show=False),
                    markline_opts=opts.MarkLineOpts(
                        data=[
                            opts.MarkLineItem(type_="min", name="最小值"),
                            opts.MarkLineItem(type_="max", name="最大值"),
                            opts.MarkLineItem(type_="average", name="平均值"),
                        ]
                    ),
                )
            )
            c.render('./results/opts7.html')
    with col2:
        with open('./results/opts7.html','r') as f:
            content = f.read()
            cp.html(content,width=800,height=500,scrolling=True)
    
    col1,col2 = st.columns([1,1])
    with col1:
        with st.echo():
            c = (
                Bar(init_opts=opts.InitOpts(width='600px',height='400px'))
                .add_xaxis(Faker.choose())
                .add_yaxis("商家A", Faker.values())
                .add_yaxis("商家B", Faker.values())
                .set_global_opts(title_opts=opts.TitleOpts(title="Bar-MarkLine（自定义）"))
                .set_series_opts(
                    label_opts=opts.LabelOpts(is_show=False),
                    markline_opts=opts.MarkLineOpts(
                        data=[opts.MarkLineItem(y=60, name="yAxis=60")]
                    ),
                )
            )
            c.render('./results/opts8.html')
    with col2:
        with open('./results/opts8.html','r') as f:
            content = f.read()
            cp.html(content,width=600,height=400,scrolling=True)
    

    st.markdown("""<h3><center>数据缩放</center></h3>""",unsafe_allow_html=True)
    col1,col2 = st.columns([1,1])
    with col1:
        with st.echo():
            c = (
                Bar(init_opts=opts.InitOpts(width='600px',height='400px'))
                .add_xaxis(Faker.days_attrs)
                .add_yaxis("商家A", Faker.days_values)
                .set_global_opts(
                    title_opts=opts.TitleOpts(title="Bar-DataZoom（slider-水平）"),
                    datazoom_opts=opts.DataZoomOpts(),
                )
            )
            c.render('./results/opts9.html')
    with col2:
        with open('./results/opts9.html','r') as f:
            content = f.read()
            cp.html(content,width=600,height=400,scrolling=True)

    col1,col2 = st.columns([1,1])
    with col1:
        with st.echo():
            c = (
                Bar(init_opts=opts.InitOpts(width='600px',height='400px'))
                .add_xaxis(Faker.days_attrs)
                .add_yaxis("商家A", Faker.days_values, color=Faker.rand_color())
                .set_global_opts(
                    title_opts=opts.TitleOpts(title="Bar-DataZoom（slider-垂直）"),
                    datazoom_opts=opts.DataZoomOpts(orient="vertical"),
                )
            )
            c.render('./results/opts10.html')
    with col2:
        with open('./results/opts10.html','r') as f:
            content = f.read()
            cp.html(content,width=600,height=400,scrolling=True)
    
    col1,col2 = st.columns([1,1])
    with col1:
        with st.echo():
            c = (
                Bar(init_opts=opts.InitOpts(width='600px',height='400px'))
                .add_xaxis(Faker.days_attrs)
                .add_yaxis("商家A", Faker.days_values, color=Faker.rand_color())
                .set_global_opts(
                    title_opts=opts.TitleOpts(title="Bar-DataZoom（inside）"),
                    datazoom_opts=opts.DataZoomOpts(orient="vertical",type_="inside"),
                )
            )
            c.render('./results/opts11.html')
    with col2:
        with open('./results/opts11.html','r') as f:
            content = f.read()
            cp.html(content,width=600,height=400,scrolling=True)
    
    st.markdown("""<h3><center>堆叠数据</center></h3>""",unsafe_allow_html=True)
    col1,col2 = st.columns([1,1])
    with col1:
        with st.echo():
            c = (
                Bar(init_opts=opts.InitOpts(width='600px',height='400px'))
                .add_xaxis(Faker.choose())
                .add_yaxis("商家A", Faker.values(), stack="stack1")
                .add_yaxis("商家B", Faker.values(), stack="stack1")
                .add_yaxis("商家C", Faker.values())
                .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
                .set_global_opts(title_opts=opts.TitleOpts(title="Bar-堆叠数据（部分）"))
            )
            c.render('./results/opts12.html')
    with col2:
        with open('./results/opts12.html','r') as f:
            content = f.read()
            cp.html(content,width=600,height=400,scrolling=True)
    
    st.markdown("""<h3><center>图表重叠</center></h3>""",unsafe_allow_html=True)
    col1,col2 = st.columns([1,1])
    with col1:
        with st.echo():
            x_data = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]
            bar = (
                Bar(init_opts=opts.InitOpts(width="700px", height="600px"))
                .add_xaxis(xaxis_data=x_data)
                .add_yaxis(
                    series_name="蒸发量",
                    y_axis=[
                        2.0,
                        4.9,
                        7.0,
                        23.2,
                        25.6,
                        76.7,
                        135.6,
                        162.2,
                        32.6,
                        20.0,
                        6.4,
                        3.3,
                    ],
                    label_opts=opts.LabelOpts(is_show=False),
                )
                .add_yaxis(
                    series_name="降水量",
                    y_axis=[
                        2.6,
                        5.9,
                        9.0,
                        26.4,
                        28.7,
                        70.7,
                        175.6,
                        182.2,
                        48.7,
                        18.8,
                        6.0,
                        2.3,
                    ],
                    label_opts=opts.LabelOpts(is_show=False),
                )
                .extend_axis(
                    yaxis=opts.AxisOpts(
                        name="温度",
                        type_="value",
                        min_=0,
                        max_=25,
                        interval=5,
                        axislabel_opts=opts.LabelOpts(formatter="{value} °C"),
                    )
                )
                .set_global_opts(
                    tooltip_opts=opts.TooltipOpts(
                        is_show=True, trigger="axis", axis_pointer_type="cross"
                    ),
                    xaxis_opts=opts.AxisOpts(
                        type_="category",
                        axispointer_opts=opts.AxisPointerOpts(is_show=True, type_="shadow"),
                    ),
                    yaxis_opts=opts.AxisOpts(
                        name="水量",
                        type_="value",
                        min_=0,
                        max_=250,
                        interval=50,
                        axislabel_opts=opts.LabelOpts(formatter="{value} ml"),
                        axistick_opts=opts.AxisTickOpts(is_show=True),
                        splitline_opts=opts.SplitLineOpts(is_show=True),
                    ),
                )
            )

            line = (
                Line()
                .add_xaxis(xaxis_data=x_data)
                .add_yaxis(
                    series_name="平均温度",
                    yaxis_index=1,
                    y_axis=[2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2],
                    label_opts=opts.LabelOpts(is_show=False),
                )
            )

            bar.overlap(line).render('./results/opts13.html')
    with col2:
        with open('./results/opts13.html','r') as f:
            content = f.read()
            cp.html(content,width=800,height=800,scrolling=True)
    
    
        
            
    