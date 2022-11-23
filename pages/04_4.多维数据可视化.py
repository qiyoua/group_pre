import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import streamlit.components.v1 as cp
import numpy as np


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
         """
     )
# set_bg_hack_url()

with st.sidebar:
    menu = ['2.1.数据介绍','2.2.图的布局','2.3.3d柱状图与热图',
    '2.4.店铺特征矩阵的构建','2.5. 散点图','2.6.平行坐标系']
    opt = option_menu('多维数据可视化',options=menu)

a = pd.read_csv("./results/shoes.csv")
t1=a[a.nick=="意尔康皮鞋旗舰店"].groupby("info.款式").size()
t2=a[a.nick=="米兰多格商场"].groupby("info.款式").size()
p0=pd.concat([t1,t2],axis=1,sort=False).fillna(0)

if opt == menu[0]:
    """- 多维数据的可视化的概念"""
    """所谓多维，就是数据不仅仅有x,y两列，而是有多列数据特征需要展示。这里主要分为两类展示方法，一类是用多张图展示多个数据，一类是一张图上展示多列数据。"""
    """- shoes数据集"""
    st.dataframe(a.head(1))
    """- 以店铺的商品数量排序"""
    st.code(a.groupby("nick").size().sort_values(ascending=False))
    """- 查看数据集的特征"""
    st.code(a.columns)
    
if opt == menu[1]:
    """- 图形的并列"""
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
    
    """- 图形选项卡"""
    with st.echo():
        from pyecharts.faker import Faker
        import pyecharts.options as opts
        from pyecharts.charts import Bar, Tab, Pie, Line
        from pyecharts.components import Table


        def bar_datazoom_slider() -> Bar:
            c = (
                Bar()
                .add_xaxis(Faker.days_attrs)
                .add_yaxis("商家A", Faker.days_values)
                .add_yaxis("商家B", Faker.days_values)
                .set_global_opts(
                    title_opts=opts.TitleOpts(title="Bar-DataZoom（slider-水平）"),
                    datazoom_opts=[opts.DataZoomOpts()],
                )
            )
            return c


        def line_markpoint() -> Line:
            c = (
                Line()
                .add_xaxis(Faker.choose())
                .add_yaxis(
                    "商家A",
                    Faker.values(),
                    markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="min")]),
                )
                .add_yaxis(
                    "商家B",
                    Faker.values(),
                    markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]),
                )
                .set_global_opts(title_opts=opts.TitleOpts(title="Line-MarkPoint"))
            )
            return c


        def pie_rosetype() -> Pie:
            v = Faker.choose()
            c = (
                Pie()
                .add(
                    "",
                    [list(z) for z in zip(v, Faker.values())],
                    radius=["30%", "75%"],
                    center=["25%", "50%"],
                    rosetype="radius",
                    label_opts=opts.LabelOpts(is_show=False),
                )
                .add(
                    "",
                    [list(z) for z in zip(v, Faker.values())],
                    radius=["30%", "75%"],
                    center=["75%", "50%"],
                    rosetype="area",
                )
                .set_global_opts(title_opts=opts.TitleOpts(title="Pie-玫瑰图示例"))
            )
            return c


        def table_base() -> Table:
            table = Table()

            headers = ["City name", "Area", "Population", "Annual Rainfall"]
            rows = [
                ["Brisbane", 5905, 1857594, 1146.4],
                ["Adelaide", 1295, 1158259, 600.5],
                ["Darwin", 112, 120900, 1714.7],
                ["Hobart", 1357, 205556, 619.5],
                ["Sydney", 2058, 4336374, 1214.8],
                ["Melbourne", 1566, 3806092, 646.9],
                ["Perth", 5386, 1554769, 869.4],
            ]
            table.add(headers, rows).set_global_opts(
                title_opts=opts.ComponentTitleOpts(title="Table")
            )
            return table

        tab = Tab()
        tab.add(bar_datazoom_slider(), "bar-example")
        tab.add(line_markpoint(), "line-example")
        tab.add(pie_rosetype(), "pie-example")
        tab.add(table_base(), "table-example")
        tab.render('./results/hl2.html')
    with open('./results/hl2.html','r') as f:
        cp.html(f.read(),height=600,width=1000)

    """- 时间轮播图"""
    with st.echo():
        from pyecharts.faker import Faker
        import pyecharts.options as opts
        from pyecharts.charts import Bar, Page, Pie, Timeline


        def timeline_bar() -> Timeline:
            x = Faker.choose()
            tl = Timeline()
            for i in range(2015, 2020):
                bar = (
                    Bar()
                    .add_xaxis(x)
                    .add_yaxis("商家A", Faker.values())
                    .add_yaxis("商家B", Faker.values())
                    .set_global_opts(title_opts=opts.TitleOpts("某商店{}年营业额".format(i)))
                )
                tl.add(bar, "{}年".format(i))
            return tl
        timeline_bar().render('./results/hl3.html')
    with open('./results/hl3.html','r') as f:
        cp.html(f.read(),height=600,width=1000)

if opt == menu[2]:
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

if opt == menu[3]:
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

if opt == menu[4]:
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

if opt == menu[5]:
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
