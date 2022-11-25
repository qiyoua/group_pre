import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import streamlit.components.v1 as cp
import numpy as np
import base64


st.set_page_config(layout='wide')
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

with st.sidebar:
    menu = ['2.1.数据介绍','2.2.单图中多列数据合并','2.3散点图和折线图并列','2.4柱状图并列','2.5 3d柱状图与热图',
    '2.6 店铺特征矩阵的构建','2.7散点图','2.8平行坐标系']
    opt = option_menu('多维数据可视化',options=menu)

a = pd.read_csv("./results/shoes.csv")
t1=a[a.nick=="意尔康皮鞋旗舰店"].groupby("info.款式").size()
t2=a[a.nick=="米兰多格商场"].groupby("info.款式").size()
p0=pd.concat([t1,t2],axis=1,sort=False).fillna(0)

if opt == menu[0]:
    """# 多维数据的可视化"""
    """
1.概念
* 所谓多维，就是数据不仅仅有x,y两列，而是有多列数据特征需要展示。这里主要分为两类展示方法，一类是用多张图展示多个数据，一类是一张图上展示多列数据。

2.数据来源
* 所用的数据为2017年从淘宝爬取的男鞋销售情况

3.数据包含的属性

* 鞋子上市年份季节  
* 上市时间
* 低帮鞋品名
* 鞋子功能
* 吊牌价
* 品牌 
* 图案
* 上市年份季节 
* 上市时间
* ...
* 颜色分类
* 风格
* price

4.代码、代码结果和代码分析如下
"""

    """- shoes数据集"""
    st.dataframe(a.head(1))
    """- 以店铺的商品数量排序"""
    st.code(a.groupby("nick").size().sort_values(ascending=False))
    """- 查看数据集的特征"""
    st.code(a.columns)
    """
    * 计算上面排名前二的两个商家各个款式的对应的商品数量，并且组成矩阵，使得第一列是"意尔康皮鞋旗舰店"对应的商品数量，第二列是"米兰多格商场"对应的商品数量（注意为什么要组成数据框，这是为了可以让索引对齐）
    """
    with st.echo():
        t1=a[a.nick=="意尔康皮鞋旗舰店"].groupby("info.款式").size()
        t2=a[a.nick=="米兰多格商场"].groupby("info.款式").size()
        p0=pd.concat([t1,t2],axis=1,sort=False).fillna(0)
    st.dataframe(p0.T)
    
    
if opt == menu[1]:
    """
    pyecharts 包制作的图表里有工具栏，左上角有一些图片功能，包括：保存图片、还原、数据视图、区域缩放、切换为折现图、切换成柱状图、切换为堆叠、矩形选择、圈选、横向选择、纵向选择、保持选择、清除选择，交互性较强
    """
    with st.echo():
        from pyecharts.globals import ThemeType
        from pyecharts.faker import Faker
        from pyecharts import options as opts
        from pyecharts.charts import Bar

        bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.PURPLE_PASSION))
        bar.add_xaxis(p0[0].index.tolist())
        bar.add_yaxis("意尔康皮鞋旗舰店", p0[0].tolist())
        bar.add_yaxis("米兰多格商场", p0[1].tolist())
        bar.set_global_opts(title_opts=opts.TitleOpts(title="两个商场的销售情况",subtitle="意尔康皮鞋旗舰店、米兰多格商场"),toolbox_opts=opts.ToolboxOpts())
        bar.render('./results/bar1.html')  #切换成柱状图
    with open('./results/bar1.html','r') as f:
        cp.html(f.read(),height=800,width=1000)

if opt == menu[2]:
    """- 图形的并列"""
    """pyecharts 包可以组合多个图表，让多图在一个界面显示，比如说图的并列（柱 状图并列）（散点图和折线图也可以并列）、图形选项卡，时间线轮播图"""
    with st.echo():
        from pyecharts.faker import Faker
        import pyecharts.options as opts
        from pyecharts.charts import Bar, Grid, Line,Scatter


        def grid_horizontal() -> Grid:
            scatter = (
                Scatter()
                .add_xaxis(p0[0].index.tolist())
                .add_yaxis("意尔康皮鞋旗舰店",list(p0[0].values))
                .add_yaxis("米兰多格商场", list(p0[1].values))
                .set_global_opts(
                    title_opts=opts.TitleOpts(title="Grid-Scatter"),
                    legend_opts=opts.LegendOpts(pos_left="20%"),
                )
            )
            line = (
                Line()
                .add_xaxis(p0[0].index.tolist())
                .add_yaxis("意尔康皮鞋旗舰店",  list(p0[0].values))     
                .add_yaxis("米兰多格商场",list(p0[1].values))
                .set_global_opts(
                    title_opts=opts.TitleOpts(title="Grid-Line", pos_right="5%"),
                    legend_opts=opts.LegendOpts(pos_right="20%"),
                )
            )

            grid = (
                Grid()
                .add(scatter, grid_opts=opts.GridOpts(pos_left="55%"))
                .add(line, grid_opts=opts.GridOpts(pos_right="55%"))
            )
            return grid
        grid_horizontal().render('./results/hl1.html')
    with open('./results/hl1.html','r') as f:
        cp.html(f.read(),height=500,width=1000)

if opt == menu[3]: 
    """- 柱状图并列"""
    with st.echo():
        from pyecharts.charts import Bar, Grid, Line,Scatter
        from pyecharts.globals import ThemeType
        import pyecharts.options as opts

        f1=Bar()
        f1.add_xaxis(p0.index.tolist())
        f1.add_yaxis("意尔康皮鞋旗舰店", p0[0].tolist())
        f1.set_global_opts(title_opts=opts.TitleOpts(title="两个商场的销售情况", subtitle="意尔康皮鞋旗舰店、米兰多格商场"),
                        legend_opts=opts.LegendOpts(pos_left="20%"))


        f2=Bar()
        f2.add_xaxis(p0.index.tolist())
        f2.add_yaxis("米兰多格商场", p0[1].tolist())
        f2.set_global_opts(title_opts=opts.TitleOpts(title="两个商场的销售情况", subtitle="意尔康皮鞋旗舰店、米兰多格商场"),
                        legend_opts=opts.LegendOpts(pos_right="20%"))

        g1=Grid(init_opts=opts.InitOpts(theme=ThemeType.PURPLE_PASSION))
        g1.add(f1, grid_opts=opts.GridOpts(pos_left="55%"))
        g1.add(f2, grid_opts=opts.GridOpts(pos_right="55%"))

        g1.render('./results/bar2.html')
    with open('./results/bar2.html','r') as f:
        cp.html(f.read(),height=500,width=1000)
    """- 图形选项卡"""
    with st.echo():
        from pyecharts.faker import Faker
        import pyecharts.options as opts
        from pyecharts.charts import Bar, Tab, Pie, Line, Timeline
        from pyecharts.components import Table


        def bar_datazoom_slider() -> Bar:
            c = (
                Bar()
                .add_xaxis(p0.index.tolist())
                .add_yaxis("意尔康皮鞋旗舰店", list(p0[0].values))
                .add_yaxis("米兰多格商场", list(p0[1].values))
                .set_global_opts(
                    title_opts=opts.TitleOpts(title="柱状图"),
                    datazoom_opts=[opts.DataZoomOpts()],
                )
            )
            return c


        def line_markpoint() -> Line:
            c = (
                Line()
                .add_xaxis(p0.index.tolist())
                .add_yaxis(
                    "意尔康皮鞋旗舰店",
                    list(p0[0].values),
                    markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="min")]),
                )
                .add_yaxis(
                    "米兰多格商场",
                    list(p0[1].values),
                    markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]),
                )
                .set_global_opts(title_opts=opts.TitleOpts(title="折线图"))
            )
            return c


        def pie_rosetype() -> Pie:
            v = p0.index.tolist()
            c = (
                Pie()
                .add(
                    "",
                    [list(z) for z in zip(v,  list(p0[0].values))],
                    radius=["30%", "75%"],
                    center=["25%", "50%"],
                    rosetype="radius",
                    label_opts=opts.LabelOpts(is_show=False),
                )
                .add(
                    "",
                    [list(z) for z in zip(v,  list(p0[0].values))],
                    radius=["30%", "75%"],
                    center=["75%", "50%"],
                    rosetype="area",
                )
                .set_global_opts(title_opts=opts.TitleOpts(title=""))
            )
            return c


        def table_base() -> Table:
            table = Table()

            headers = ["款式","意尔康皮鞋旗舰店", "米兰多格商场"]
            rows = [
                ["乐福鞋", 3.0, 1.0],        
                ["伐木鞋", 1.0, 0.0],
                ["休闲皮鞋", 87.0,108.0],
                ["休闲高帮皮鞋", 8.0,0.0],
                ["商务休闲鞋", 38.0,9.0],
                ["布洛克鞋", 3.0, 0.0],
                ["德比鞋（正装皮鞋）", 91.0, 11.0],
                ["懒人鞋",4.0,0.0],
                ["户外休闲鞋",7.0,0.0],
                ["板鞋",18.0,18.0],
                ["沙滩鞋",7.0,0.0],
                ["豆豆鞋",8.0,8.0],
                ["运动休闲鞋",9.0,0.0],
                ["镂空皮鞋",3.0,1.0],
                ["高帮板鞋",2.0,0.0],
                ["工装鞋",0.0,2.0]    
            ]
            table.add(headers, rows).set_global_opts(
                title_opts=opts.ComponentTitleOpts(title="Table")
            )

            return table




        tab = Tab()
        tab.add(bar_datazoom_slider(), "bar")
        tab.add(line_markpoint(), "line")
        tab.add(pie_rosetype(), "pie")
        tab.add(table_base(), "table")
        tab.render('./results/hl2.html')
    with open('./results/hl2.html','r') as f:
        cp.html(f.read(),height=600,width=1000)

    """- 时间轮播图"""
    with st.echo():
        f1=Bar()
        f1.add_xaxis(p0.index.tolist())
        f1.add_yaxis("意尔康皮鞋旗舰店", p0[0].tolist())
        f1.set_global_opts(title_opts=opts.TitleOpts(title="两个商场的销售情况", subtitle="意尔康皮鞋旗舰店、米兰多格商场"))

        f2=Bar()
        f2.add_xaxis(p0.index.tolist())
        f2.add_yaxis("米兰多格商场", p0[1].tolist())
        f2.set_global_opts(title_opts=opts.TitleOpts(title="两个商场的销售情况", subtitle="意尔康皮鞋旗舰店、米兰多格商场"))

        t1=Timeline()
        t1.add(f1,"777")
        t1.add(f2,"888")
        t1.render('./results/hl3.html')
    with open('./results/hl3.html','r') as f:
        cp.html(f.read(),height=600,width=1000)
    """
    从以上图中可以看到商品数量排名前二的两个商家中，休闲皮鞋都是卖得最好一个款式，意尔康皮鞋期间店里卖得最好的是德比鞋，另外板鞋在两家店铺中的销售情况相同。
    """
if opt == menu[4]: 
    """
    * 对于多维数据，3d图是非常形象的表现方法，x,y轴通常表示两个条件限定，z轴（柱的高度）通常表示在这样限定下的数量
    
    * 注意 pyecharts3d 柱状图的数据格式，x,y 分别对应有哪些类别，通常是一个列表，而data 是一个三元列表，前两个为确定哪两个类别，通过序号指代，最后一个为数量使用的数据是：“鞋面材质”,“风格”这两个特征下商品的数量
    """
    """- 3D柱状图"""
    with st.echo():
        import pyecharts.options as opts
        from pyecharts.charts import Bar3D 

        
        p1=a.groupby(["info.鞋面材质","info.风格"]).size().sort_values(ascending=False)
        x=[]
        y=[]
        data=[]
        n=0
        for i in p1.items():
            if i[0][0] not in x:
                x.append(i[0][0])
            if i[0][1] not in y:
                y.append(i[0][1])
            data.append([x.index(i[0][0]),y.index(i[0][1]),i[1]])
        f3=Bar3D()
        f3.add("",data,
            xaxis3d_opts=opts.Axis3DOpts(x, type_="category"),
            yaxis3d_opts=opts.Axis3DOpts(y, type_="category"),
            zaxis3d_opts=opts.Axis3DOpts(type_="value")
            ).set_global_opts(
                visualmap_opts=opts.VisualMapOpts(max_=20),
                title_opts=opts.TitleOpts(title="Bar3D-基本示例"),
                )
        f3.render('./results/hl4.html')
    with open('./results/hl4.html','r') as f:
        cp.html(f.read(),height=600,width=1000)
    """- 热图"""
    with st.echo():
        import random
        from pyecharts.faker import  Faker
        import pyecharts.options as opts
        from pyecharts.charts import HeatMap

        f4=HeatMap()
        f4.add_xaxis(x)
        f4.add_yaxis("series0", y, data)
        f4.set_global_opts(
            title_opts=opts.TitleOpts(title="鞋面材质-风格"),
            visualmap_opts=opts.VisualMapOpts(),
        )
        f4.render('./results/hl5.html')
    with open('./results/hl5.html','r') as f:
        cp.html(f.read(),height=600,width=1000)
    """
    从 3D柱状图和热图中可以发现，材质为头层牛皮的鞋子比较受欢迎， 风格里，商务、休闲、青春潮流、简约和英伦的比较受欢迎，最受欢迎的鞋子款式为尚无风格的头层牛皮鞋，最不受欢迎的鞋子为民族风格，棉布材质等
    """

if opt == menu[5]:
    st.code(
        """
z_xse: 这个店铺的销售额
z_num: 这个店铺的商品数量
p_sales: 平均的销售量
p_dbj: 每笔单价（平均每笔的单价）=销售额和/销售量的
p_price: 这个店铺的平均价格
        """
    )
    st.code("""
#把商品销量提取出来，并把对应列表的类型转化为数
a.sales=a.sales.str.split("人",expand=True)[0]
a.sales = a.sales.astype(np.int64)#转换列的类型为整数
a.price = a.price.astype(np.float)
#求出各个商品的销售额并把它并入到原始数据框中去
z1=a.sales*a.price
z1.name="xse"
a1=pd.concat([a,z1],axis=1)#给序列命名之后添加入数据框就会直接以序列名作为列标
#先做成字典，把各个特征放入字典中
te_zheng={"nick":[],"z_xse":[],"z_num":[],"p_sales":[],"p_bdj":[],"p_price":[]}
for i in a1.groupby("nick"):
    te_zheng["nick"].append(i[0])
    te_zheng["z_xse"].append(i[1].xse.sum()) #某个店铺的销售额
    te_zheng["z_num"].append(len(i[1]))  #这个店铺的商品数量
    te_zheng["p_sales"].append(round(i[1].sales.mean(),1))
    if i[1].sales.sum()==0:#存在除零的情况，所以做判断
        te_zheng["p_bdj"].append(0)
    else:
        te_zheng["p_bdj"].append(round(i[1].xse.sum()/i[1].sales.sum(),1)) #算笔单价，销售额和/销售量的和
    te_zheng["p_price"].append(round(i[1].price.mean(),1))
# 把字典转化为数据框，并基于销售额排序
df_te_zheng=pd.DataFrame(te_zheng)
df_te_zheng.sort_values(by="z_xse",ascending=False,inplace=True)""")

#把商品销量提取出来，并把对应列表的类型转化为数
a.sales=a.sales.str.split("人",expand=True)[0]
a.sales = a.sales.astype(np.int64)#转换列的类型为整数
a.price = a.price.astype(np.float)
#求出各个商品的销售额并把它并入到原始数据框中去
z1=a.sales*a.price
z1.name="xse"
a1=pd.concat([a,z1],axis=1)#给序列命名之后添加入数据框就会直接以序列名作为列标
#先做成字典，把各个特征放入字典中
te_zheng={"nick":[],"z_xse":[],"z_num":[],"p_sales":[],"p_bdj":[],"p_price":[]}
for i in a1.groupby("nick"):
    te_zheng["nick"].append(i[0])
    te_zheng["z_xse"].append(i[1].xse.sum()) #某个店铺的销售额
    te_zheng["z_num"].append(len(i[1]))  #这个店铺的商品数量
    te_zheng["p_sales"].append(round(i[1].sales.mean(),1))
    if i[1].sales.sum()==0:#存在除零的情况，所以做判断
        te_zheng["p_bdj"].append(0)
    else:
        te_zheng["p_bdj"].append(round(i[1].xse.sum()/i[1].sales.sum(),1)) #算笔单价，销售额和/销售量的和
    te_zheng["p_price"].append(round(i[1].price.mean(),1))
# 把字典转化为数据框，并基于销售额排序
df_te_zheng=pd.DataFrame(te_zheng)
df_te_zheng.sort_values(by="z_xse",ascending=False,inplace=True)

if opt == menu[6]:
    with st.echo():
        from pyecharts.charts import Scatter
        import pyecharts.options as opts
        from pyecharts.globals import ThemeType

        f1=Scatter(init_opts=opts.InitOpts(theme=ThemeType.PURPLE_PASSION))
        f1.add_xaxis(df_te_zheng[0:20].z_xse.tolist())
        f1.add_yaxis("商家A",df_te_zheng[0:20].p_bdj.tolist()) #转化为列表
        f1.set_global_opts(xaxis_opts=opts.AxisOpts(type_='value'))#注意pyechart的x轴通常默认为类别轴，需要重新设定为数值轴
        f1.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        f1.render('./results/hl5.html')
    with open('./results/hl5.html','r') as f:
        cp.html(f.read(),height=600,width=1000)

if opt == menu[7]:
    with st.echo():
        from pyecharts.charts import Parallel
        import pyecharts.options as opts


        z1=df_te_zheng.head(5)
        data1=[]
        for i in z1.iterrows():
            data1.append(i[1].tolist()[1:])
        f2=Parallel().add_schema(
            [
                {"dim": 0, "name": "z_xse"},
                {"dim": 1, "name": "z_num"},
                {"dim": 2, "name": "p_sales"},
                {"dim": 3, "name": "p_bdj"},
                {"dim": 4, "name": "p_price"},
            ]
        )
        f2.add("parallel", data1)
        f2.set_global_opts(title_opts=opts.TitleOpts(title="Parallel"))
        f2.render('./results/hl6.html')
        #头部两店铺差异化竞争
        #垄断店铺之外的商家生存之道
    with open('./results/hl6.html','r') as f:
        cp.html(f.read(),height=600,width=1000)
    """
    * 我们可以在平行坐标图中看到销售额排名前二的两家店铺的销售情况，特征依次是店铺的销售额、店铺的商品数量、店铺的男鞋平均销售量、每笔的单价以及鞋子的平均价格。

* 在平行坐标图中可以看到销售额排名第一和第二的店铺它们的商品数量不一样，销售额第一的店铺商品数量有300多，销售额第二的店铺商品数量有150多,但销售额第二的店铺笔单价比较高，排名第二的店铺它买的商品价格都偏高，而且它卖的平均价格也偏高，达到了接近700的均价，而排名第一的店铺笔单价和销售的均价都不是最高的。说明排名第一的店铺和排名第二的店铺它们在运营策略上都有差异，排名第二的店铺主打的是高价格的男鞋，主导的是高端市场，而排名第一的店铺把价格往主流方向上靠拢。

* 排名第四、第五的店铺，它们商品都比较少，甚至是个位数，但是它们的平均销量都比较高，即虽然商品通货量少，每一样商品都卖得比较高，前提是这几个商品价格都较低，说明排名第四、第五的店铺都是靠价格取胜的，通过低价总量的方式来生存的。

* 通过平行坐标图能很好的展现头部这几个店家竞争时它们的销售策略是不同的，通过不同销售方式来生存的。
    """
