import streamlit as st
import streamlit.components.v1 as cp
from pyecharts import options as opts
from pyecharts.charts import Bar,Line
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType
from pyecharts.globals import RenderType
from pyecharts.faker import Faker
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
             background: url("https://www.beihaiting.com/uploads/allimg/150528/10723-15052QF335K6.jpg");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
set_bg_hack_url()
with st.sidebar:
    st.markdown(
    """
<style>
.stSidebar .sidebar-content {
    background-image: linear-gradient(#2e7bcf,#2e7bcf);
    color: white;
}
</style>
""",
    unsafe_allow_html=True,
)
    menu = ['1.1pyecharts介绍','1.2pyecharts绘图逻辑说明','1.3pyecharts图表的配置项']
    opt = option_menu(menu_title='1.pyecharts简介',options=menu)


# tab1,tab2,tab3 = st.tabs(['1.pyecharts介绍','2.pyecharts绘图逻辑说明','3.pyecharts图表的配置项'])

if opt == menu[0]:
    """
    ### 📣 概况

    在对数据的掌握及分析变得愈加重要的当今时代，数据可视化作为提高用户对数据的理解程度，创新架构，增进体验的重要一环，一向富有表现力的Python语言应当可以发挥更大作用，优秀的pyechart第三方库即在这样的背景下诞生
    为了更好理解pyechart的功能，首先为大家介绍Echarts：

    [Echarts](https://github.com/ecomfe/echarts)是一个由百度开源的商业级数据图表，它是一个纯JavaScript的图表库，可以流畅的运行在PC和移动设备上，兼容当前绝大部分浏览器,提供直观、生动、可交互、可高度个性化定制的数据可视化图表。它可以为用户提供直观生动，可交互，可高度个性化定制的数据可视化图表，赋予了用户对数据进行挖掘整合的能力。
    ECharts提供了常规的折线图、柱状图、散点图、饼图、K线图，用于统计的盒形图，用于地理数据可视化的地图、热力图、线图，用于关系数据可视化的关系图、treemap、旭日图，多维数据可视化的平行坐标，还有用于BI的漏斗图、仪表盘，并且支持图与图之间的混搭。

    那么，echarts能做什么呢？

    首先，echarts的图表类型之丰富，绝不亚于市面上常见的付费软件，以至于不少BI系统都是基于echarts搭建。于分析师而言，日常使用最多的折线图、条形图、散点图、饼图等，自然不在话下，同时，还有丰富的扩展项，如南丁格尔玫瑰图：
    """
    with open('./results/rose.html','r') as f:
        cp.html(f.read(),height=400)

    """
    综上，Echarts拥有开源、高度定制的优点，并且凭借着良好的交互性，精巧的图表设计，得到了众多开发者的认可。但是美中不足的是，ECharts的使用需要有一定的前端开发基础，只是这一点就让很多人望而却步了，对于分析师而言，大部分工作并不会涉及到前端开发，为了使用某个图表学习前端框架和JS语言的成本可能太高了。但不幸中的万幸，有大神为我们开发了一套基于ECharts的开源框架——pyecharts，Python 是一门富有表达力的语言，很适合用于数据处理。当数据分析遇上数据可视化时，pyecharts诞生了。该框架使用python语言编写，函数式传参、简单快捷。在大数据和机器学习概念日益火爆的今天，python已经成为了很多分析师的必备技能，在这一buff加成之下，要学会使用ECharts简直是易如反掌。

    [pyecharts](https://github.com/pyecharts/pyecharts)库是一个用于生成 Echarts 图表的类库。实际上就是 Echarts 与 Python 的对接。使用 pyecharts 可以生成独立的网页，也可以在 flask ， Django 中集成使用。

    

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


if opt == menu[1]:
    st.markdown('<h4><center>从简单的图表开始</center></h4>',unsafe_allow_html=True)
    """
    pyecharts的绘图逻辑分为以下几步。

    ① 选择图表类型；

    ② 声明图形类并添加数据；

    ③ 选择全局变量；

    ④ 显示及保存图表；

    - 第一步

    第一步是选择图表类型，基于自己的数据特点，我们看看自己想要绘制哪种图形，需要什么图形就导入什么图形，下面简单列举了几个导入方法。"""
    st.code("""
from pyecharts.charts import Scatter  # 导入散点图
from pyecharts.charts import Line     # 导入折线图
from pyecharts.charts import Pie      # 导入饼图
from pyecharts.charts import Geo      # 导入地图
    """)
    _,col,_ = st.columns([1,2,1])
    with col:
        st.image('./results/charts.png')
    """- 第二步

    第二步是声明图形类并添加数据，什么是图形类呢？其实每一个图形库都是被pyecharts作者封装成为了一个类，这就是所谓的面向对象，我们在使用这个类的时候，需要实例化这个类(观察下面代码)。声明类之后，相当于初始化了一个画布，我们之后的绘图就是在这个画布上进行。接下来要做的就是添加数据，pyecharts中添加数据共有2种方式，一种是普通方式添加数据，一种是链式调用(观察下面代码)来添加数据。
    """
    "下面绘制的是：正弦曲线的散点图"
    with st.echo():
        # 1.选择图表类型：我们使用的是散点图，就直接从charts模块中导入Scatter这个图形。
        from pyecharts.charts import Scatter
        import numpy as np
        
        x = np.linspace(0,2 * np.pi,100)
        y = np.sin(x)
        
        (
        # 注意：使用什么图形，就要实例化该图形的类；
        # 2.我们绘制的是Scatter散点图，就需要实例化散点图类，直接Scatter() 即可；
        Scatter() 
        # 实例化类后，接着就是添加数据，下面这种方式就是使用“链式调用”的方式绘图；
        # 注意：散点图有X、Y轴，因此需要分别给X轴、Y轴添加数据；
        # 3.我们先给X轴添加数据；
        .add_xaxis(xaxis_data=x)
        # 4.我们再给Y轴添加数据；
        .add_yaxis(series_name="这是图例",y_axis=y)
        ).render('./results/scatter.html')
    with open('./results/scatter.html','r') as f:
        cp.html(f.read(),height=500)
    """- 第三步"""
    """第三步就是设置全局变量，用通俗的话说就是：调节各种各样的参数，把图形变得更好看。常用的有标题配置项、图例配置项、工具配置项、视觉映射配置项、提示框配置项、区域缩放配置项。"""
    """- 第四步"""
    """第四步是显示及保存图表，我们这里介绍两种最常用的保存方式，如下所示。"""
    st.code("""
.render("C:\\Users\\黄伟\\Desktop\\CSDN上传图像\\a.html")
# 如果不指定路径，就是直接保存在当前工作环境目录下；
# 如果指定了路径，就是保存到指定的目录下；
# 注意：最终都是以html格式展示，发给其他任何人都可以直接打开看的；
 
.render_notebook()
# 如果我们使用的是jupyter notebook，直接使用这行代码，可以直接显示图片""")


if opt == menu[2]:
    
    st.code("""
    from pyecharts import options as opts
from pyecharts.charts import Bar,Line
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType
from pyecharts.globals import RenderType
from pyecharts.faker import Faker 
    """)
    st.markdown("""<h3><center>初始化配置项</center></h3>""",unsafe_allow_html=True)
    with st.echo():
        c = Bar(init_opts=opts.InitOpts(
            width='1000px',
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
    with open('./results/opts1.html','r') as f:
        content = f.read()
        cp.html(content,width=1000,height=400,scrolling=True)

    st.markdown("""<h3><center>动画配置项</center></h3>""",unsafe_allow_html=True)
    with st.echo():
        c = (
            Bar(init_opts=opts.InitOpts(width='1000px',height='300px'
            ,animation_opts=opts.AnimationOpts(
                animation=False)))
            .add_xaxis(Faker.choose())
            .add_yaxis("商家A", Faker.values(), stack="stack1")
            .add_yaxis("商家B", Faker.values(), stack="stack1")
            .set_global_opts()
            )
        c.render('./results/opts2.html')
    with open('./results/opts2.html','r') as f:
        content = f.read()
        cp.html(content,width=1000,height=300,scrolling=True)
    
    st.markdown("""<h3><center>标题配置项</center></h3>""",unsafe_allow_html=True)
    with st.echo():
        c = (
            Bar(init_opts=opts.InitOpts(width='1000px',height='400px'))
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

    with open('./results/opts3.html','r') as f:
        content = f.read()
        cp.html(content,width=1000,height=400,scrolling=True)
    
    st.markdown("""<h3><center>坐标轴配置项</center></h3>""",unsafe_allow_html=True)
    with st.echo():
        c = (
                Bar(init_opts=opts.InitOpts(width='1000px',height='800px'))
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
    with open('./results/opts4.html','r') as f:
        content = f.read()
        cp.html(content,width=1000,height=800,scrolling=True)

    st.markdown("""<h3><center>xy轴交换</center></h3>""",unsafe_allow_html=True)
    with st.echo():
        c = (
            Bar(init_opts=opts.InitOpts(width='1000px',height='400px'))
            .add_xaxis(Faker.choose())
            .add_yaxis("商家A", Faker.values())
            .add_yaxis("商家B", Faker.values())
            .reversal_axis()
            .set_series_opts(label_opts=opts.LabelOpts(position="right"))
            .set_global_opts(title_opts=opts.TitleOpts(title="Bar-翻转 XY 轴"))
        )
        c.render('./results/opts5.html')
    with open('./results/opts5.html','r') as f:
        content = f.read()
        cp.html(content,width=1000,height=400,scrolling=True)
    
    st.markdown("""<h3><center>标记配置项</center></h3>""",unsafe_allow_html=True)
    with st.echo():
        c = (
            Bar(init_opts=opts.InitOpts(width='1000px',height='450px'))
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
    with open('./results/opts6.html','r') as f:
        content = f.read()
        cp.html(content,width=1000,height=450,scrolling=True)
    
    with st.echo():
        c = (
            Bar(init_opts=opts.InitOpts(width='1000px',height='400px'))
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
    with open('./results/opts7.html','r') as f:
        content = f.read()
        cp.html(content,width=1000,height=500,scrolling=True)
    
    with st.echo():
        c = (
            Bar(init_opts=opts.InitOpts(width='1000px',height='400px'))
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
    with open('./results/opts8.html','r') as f:
        content = f.read()
        cp.html(content,width=1000,height=400,scrolling=True)
    

    st.markdown("""<h3><center>数据缩放</center></h3>""",unsafe_allow_html=True)
    with st.echo():
        c = (
            Bar(init_opts=opts.InitOpts(width='1000px',height='400px'))
            .add_xaxis(Faker.days_attrs)
            .add_yaxis("商家A", Faker.days_values)
            .set_global_opts(
                title_opts=opts.TitleOpts(title="Bar-DataZoom（slider-水平）"),
                datazoom_opts=opts.DataZoomOpts(),
            )
        )
        c.render('./results/opts9.html')
    with open('./results/opts9.html','r') as f:
        content = f.read()
        cp.html(content,width=1000,height=400,scrolling=True)


    with st.echo():
        c = (
            Bar(init_opts=opts.InitOpts(width='1000px',height='400px'))
            .add_xaxis(Faker.days_attrs)
            .add_yaxis("商家A", Faker.days_values, color=Faker.rand_color())
            .set_global_opts(
                title_opts=opts.TitleOpts(title="Bar-DataZoom（slider-垂直）"),
                datazoom_opts=opts.DataZoomOpts(orient="vertical"),
            )
        )
        c.render('./results/opts10.html')

    with open('./results/opts10.html','r') as f:
        content = f.read()
        cp.html(content,width=1000,height=400,scrolling=True)
    

    with st.echo():
        c = (
            Bar(init_opts=opts.InitOpts(width='1000px',height='400px'))
            .add_xaxis(Faker.days_attrs)
            .add_yaxis("商家A", Faker.days_values, color=Faker.rand_color())
            .set_global_opts(
                title_opts=opts.TitleOpts(title="Bar-DataZoom（inside）"),
                datazoom_opts=opts.DataZoomOpts(orient="vertical",type_="inside"),
            )
        )
        c.render('./results/opts11.html')
    with open('./results/opts11.html','r') as f:
        content = f.read()
        cp.html(content,width=1000,height=400,scrolling=True)
    
    st.markdown("""<h3><center>堆叠数据</center></h3>""",unsafe_allow_html=True)

    with st.echo():
        c = (
            Bar(init_opts=opts.InitOpts(width='1000px',height='400px'))
            .add_xaxis(Faker.choose())
            .add_yaxis("商家A", Faker.values(), stack="stack1")
            .add_yaxis("商家B", Faker.values(), stack="stack1")
            .add_yaxis("商家C", Faker.values())
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(title_opts=opts.TitleOpts(title="Bar-堆叠数据（部分）"))
        )
        c.render('./results/opts12.html')

    with open('./results/opts12.html','r') as f:
        content = f.read()
        cp.html(content,width=1000,height=400,scrolling=True)
    
    st.markdown("""<h3><center>图表重叠</center></h3>""",unsafe_allow_html=True)
    with st.echo():
        x_data = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]
        bar = (
            Bar(init_opts=opts.InitOpts(width="1000px", height="600px"))
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
    with open('./results/opts13.html','r') as f:
        content = f.read()
        cp.html(content,width=1000,height=600,scrolling=True)
   
    
    
        
            
    