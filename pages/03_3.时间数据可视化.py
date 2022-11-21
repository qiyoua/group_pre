import pandas as pd
import numpy as np
#导入pyecharts
from pyecharts.charts import *
import pyecharts.options as opts
from pyecharts.commons.utils import JsCode
from datetime import datetime
import streamlit as st
import streamlit.components.v1 as cp
from streamlit_option_menu import option_menu

st.set_page_config(layout='wide')

# tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8,tab9 = st.tabs(['1.一个简单的折线图','2.在折线图里进行标记','3.指数年度收益率柱状图','4.指数月度收益率柱状图','5.一个简单的k线图',
# '6.添加时间轴的k线图','7.时间与点','8.上证综指vs创业板','9.一个复杂的k线图'])

with st.sidebar:
    menu = ['3.1.一个简单的折线图','3.2.在折线图里进行标记','3.3.指数年度收益率柱状图','3.4.指数月度收益率柱状图','3.5.一个简单的k线图',
    '3.6.添加时间轴的k线图','3.7.时间与点','3.8.上证综指vs创业板','3.9.一个复杂的k线图']
    opt = option_menu(menu_title='3.时间数据可视化',options=menu,styles='sky')

sh = pd.read_csv(r'./results/sh.csv',index_col=0)
sh.index = sh.index.astype('datetime64[ns]')

index_price = pd.read_csv(r'./results/index_price.csv',index_col=0)
index_price.index = index_price.index.astype('datetime64[ns]')

df = pd.read_csv(r'./results/df.csv',index_col=0)
df.index = df.index.astype('datetime64[ns]')
index_ret=index_price/index_price.shift(1)-1
ss=index_ret.to_period('Y')
sss=(ss.groupby(ss.index).apply(lambda x: ((1+x).cumprod()-1).iloc[-1])*100).round(2)

if opt == menu[0]:
    with st.echo():
        import pandas as pd
        import numpy as np
        #导入pyecharts
        from pyecharts.charts import *
        import pyecharts.options as opts
        from pyecharts.commons.utils import JsCode
        from datetime import datetime
        sh = pd.read_csv(r'./results/sh.csv',index_col=0)
        sh.index = sh.index.astype('datetime64[ns]')

        index_price = pd.read_csv(r'./results/index_price.csv',index_col=0)
        index_price.index = index_price.index.astype('datetime64[ns]')

        df = pd.read_csv(r'./results/df.csv',index_col=0)
        df.index = df.index.astype('datetime64[ns]')
        g=(Line()
        .add_xaxis(sh.index.strftime('%Y%m%d').tolist())
        .add_yaxis('',sh.close))
        g.render(r'./results/ts1.html')
    with open(r'./results/ts1.html') as f:
        cp.html(f.read(),width=1000,height=500)

if opt == menu[1]:
    with st.echo():
        #不同点位设置不同颜色
        des=sh.close.describe()
        v1,v2,v3=np.ceil(des['25%']),np.ceil(des['50%']),np.ceil(des['75%'])
        pieces=[{"min": v3, "color": "red"},
                {"min": v2, "max": v3, "color": "blue"},
                {"min": v1, "max": v2, "color": "black"},
                {"max": v1, "color": "green"},]
        #链式调用作用域()
        g = (
            Line({'width':'100%','height':'480px'})#设置画布大小，px像素
            .add_xaxis(xaxis_data=sh.index.strftime('%Y%m%d').tolist())#x数据
            .add_yaxis(
                series_name="",#序列名称
                y_axis=sh.close.values.tolist(),#添加y数据
                is_smooth=True, #平滑曲线
                is_symbol_show=False,#不显示折线的小圆圈
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(width=2),#线宽
                markpoint_opts=opts.MarkPointOpts(data=[#添加标记符
                    opts.MarkPointItem(type_='max', name='最大值'),
                    opts.MarkPointItem(type_='min', name='最小值'),],symbol_size=[100,30]),
                markline_opts=opts.MarkLineOpts(#添加均值辅助性
                        data=[opts.MarkLineItem(type_="average")], ))
            .set_global_opts(#全局参数设置
                title_opts=opts.TitleOpts(title='上证指数走势', subtitle='2000年-2022年',pos_left='center'),
                tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
                visualmap_opts=opts.VisualMapOpts(#视觉映射配置
                    orient = "horizontal",split_number = 4,
                    pos_left='center',is_piecewise=True,
                    pieces=pieces,),)
            .set_series_opts(
                markarea_opts=opts.MarkAreaOpts(#标记区域配置项
                    data=[
                        opts.MarkAreaItem(name="牛市", x=("20050606", "20071016")),
                        opts.MarkAreaItem(name="牛市", x=("20140312", "20150612")),],)))
        #使用jupyter notebook显示图形
        #g.render_notebook()
        g.render(r'./results/ts2.html')
    with open(r'./results/ts2.html') as f:
        cp.html(f.read(),width=1000,height=500)

if opt == menu[2]:
    with st.echo():
        #index_price.head()
        #指数年度收益率柱状图
        index_ret=index_price/index_price.shift(1)-1
        ss=index_ret.to_period('Y')
        sss=(ss.groupby(ss.index).apply(lambda x: ((1+x).cumprod()-1).iloc[-1])*100).round(2)

        g=(Bar()
        .add_xaxis(sss.index.strftime('%Y').tolist())
        .add_yaxis("", sss['上证综指'].tolist()))
        #g.render_notebook()
        g.render(r'./results/ts3.html')
    with open(r'./results/ts3.html') as f:
        cp.html(f.read(),width=1000,height=500)

if opt == menu[3]:
    with st.echo():    
        g = (Bar()
            .add_xaxis(sss.index.strftime('%Y').tolist())
            .add_yaxis("上证综指", sss['上证综指'].tolist(),gap="0%")
            .add_yaxis("创业板", sss['创业板'].tolist(),gap="0%")
            #添加全局配置项
            .set_global_opts(title_opts=opts.TitleOpts(title="指数月收益率"),
                        datazoom_opts=opts.DataZoomOpts(),#区域缩放配置项
                        yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(formatter="{value}%")))
            .set_series_opts(#添加序列配置项
                label_opts=opts.LabelOpts(is_show=True,formatter='{c}%')))
        g.width = "100%" #设置画布比例
        #g.render_notebook()
        g.render(r'./results/ts4.html')
    with open(r'./results/ts4.html') as f:
        cp.html(f.read(),width=1000,height=500)

if opt == menu[4]:
    with st.echo():    
        g = (Kline()
        .add_xaxis(df['2022':].index.strftime('%Y%m%d').tolist()) 
        #y轴数据，默认open、close、low、high，转为list格式
        .add_yaxis("",y_axis=df[['open', 'close', 'low', 'high']]['2022':].values.tolist())
    )
        g.render(r'./results/ts5.html')
    with open(r'./results/ts5.html') as f:
        cp.html(f.read(),width=1000,height=500)

if opt == menu[5]:
    with st.echo():    
        def draw_kline(data):
            g = (Kline()
                .add_xaxis(data.index.strftime('%Y%m%d').tolist()) 
                #y轴数据，默认open、close、high、low，转为list格式
                .add_yaxis(series_name="",
                    y_axis=data[['open', 'close', 'low', 'high']].values.tolist(),
                    itemstyle_opts=opts.ItemStyleOpts(
                        color="red",#阳线红色
                        color0="green",#阴线绿色
                        border_color="red",
                        border_color0="green",),
                    markpoint_opts=opts.MarkPointOpts(data=[#添加标记符
                        opts.MarkPointItem(type_='max', name='最大值'),
                        opts.MarkPointItem(type_='min', name='最小值'),]),
                    #添加辅助性，如某期间内最大max最小值min均值average
                    markline_opts=opts.MarkLineOpts(
                        data=[opts.MarkLineItem(type_="average",
                                                value_dim="close")], ),)
                .set_global_opts(
                    datazoom_opts=[opts.DataZoomOpts()],#滑动模块选择
                    title_opts=opts.TitleOpts(title="股票K线图",pos_left='center'),))
            return g
        draw_kline(df).render(r'./results/ts6.html')
    with open(r'./results/ts6.html') as f:
        cp.html(f.read(),width=1000,height=500)

if opt == menu[6]:
    with st.echo():    
        #创业板和上证综指历年收益率数据
        #sss.head()
        g = (
            Scatter()
            .add_xaxis([str(d) for d in sss.index.year])
            .add_yaxis("上证综指(%)",sss['上证综指'].tolist())
            .add_yaxis("创业板(%)", sss['创业板'].tolist())
            .set_global_opts(
                title_opts=opts.TitleOpts(title="指数历年收益率"),
                visualmap_opts=opts.VisualMapOpts(type_="size", is_show=False),
                xaxis_opts=opts.AxisOpts(type_="category",
                    axisline_opts=opts.AxisLineOpts(is_on_zero=False),
                    ),
                yaxis_opts=opts.AxisOpts(is_show=False,))
        )
        g.width = "100%"
        g.render(r'./results/ts7.html')
    with open(r'./results/ts7.html') as f:
        cp.html(f.read(),width=1000,height=500)

if opt == menu[7]:
    with st.echo():    
        g = (
            Scatter()
            .add_xaxis(sss['上证综指'].tolist())
            .add_yaxis("", sss['创业板'].tolist(),
            symbol_size=20,
            label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
                title_opts=opts.TitleOpts('上证综指 VS 创业板'),
                tooltip_opts=opts.TooltipOpts(is_show=False),
                xaxis_opts=opts.AxisOpts(name='上证综指',
                    type_="value", 
                    splitline_opts=opts.SplitLineOpts(is_show=True),                     
                    axislabel_opts=opts.LabelOpts(formatter='{value}%')),
                yaxis_opts=opts.AxisOpts(name='创业板',
                    type_="value",
                    splitline_opts=opts.SplitLineOpts(is_show=True),                     
                    axislabel_opts=opts.LabelOpts(formatter='{value}%'),)))
        g.width = "100%"
        g.render(r'./results/ts8.html')
    with open(r'./results/ts8.html') as f:
        cp.html(f.read(),width=1000,height=500)

if opt == menu[8]:
    with st.echo():    
        import pandas as pd
        import numpy as np
        # import talib as ta
        # import tushare as ts
        #导入pyecharts
        from pyecharts.charts import *
        from pyecharts import options as opts
        from pyecharts.commons.utils import JsCode

        def plot_kline_volume_signal(data):
            kline = (
                Kline(init_opts=opts.InitOpts(width="1800px",height="1000px"))
                .add_xaxis(xaxis_data=list(data.index))
                .add_yaxis(
                    series_name="klines",
                    y_axis=data[["open","close","low","high"]].values.tolist(),
                    itemstyle_opts=opts.ItemStyleOpts(color="#ec0000", color0="#00da3c"),
                )
                .set_global_opts(legend_opts=opts.LegendOpts(is_show=True, pos_bottom=10, pos_left="center"),
                    datazoom_opts=[
                        opts.DataZoomOpts(
                            is_show=False,
                            type_="inside",
                            xaxis_index=[0,1],
                            range_start=98,
                            range_end=100,
                        ),
                        opts.DataZoomOpts(
                            is_show=True,
                            xaxis_index=[0,1],
                            type_="slider",
                            pos_top="85%",
                            range_start=98,
                            range_end=100,
                        ),
                    ],
                    yaxis_opts=opts.AxisOpts(
                        is_scale=True,
                        splitarea_opts=opts.SplitAreaOpts(
                            is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
                        ),
                    ),
                    tooltip_opts=opts.TooltipOpts(
                        trigger="axis",
                        axis_pointer_type="cross",
                        background_color="rgba(245, 245, 245, 0.8)",
                        border_width=1,
                        border_color="#ccc",
                        textstyle_opts=opts.TextStyleOpts(color="#000"),
                    ),
                    visualmap_opts=opts.VisualMapOpts(
                        is_show=False,
                        dimension=2,
                        series_index=5,
                        is_piecewise=True,
                        pieces=[
                            {"value": 1, "color": "#00da3c"},
                            {"value": -1, "color": "#ec0000"},
                        ],
                    ),
                    axispointer_opts=opts.AxisPointerOpts(
                        is_show=True,
                        link=[{"xAxisIndex": "all"}],
                        label=opts.LabelOpts(background_color="#777"),
                    ),
                    brush_opts=opts.BrushOpts(
                        x_axis_index="all",
                        brush_link="all",
                        out_of_brush={"colorAlpha": 0.1},
                        brush_type="lineX",
                    ),
                )
            )

            bar = (
                Bar()
                .add_xaxis(xaxis_data=list(data.index))
                .add_yaxis(
                    series_name="volume",
                    y_axis=data["volume"].tolist(),
                    xaxis_index=1,
                    yaxis_index=1,
                    label_opts=opts.LabelOpts(is_show=False),
                    itemstyle_opts=opts.ItemStyleOpts(
                        color=JsCode(
                            """
                        function(params) {
                            var colorList;
                            if (barData[params.dataIndex][1] > barData[params.dataIndex][0]) {
                                colorList = '#ef232a';
                            } else {
                                colorList = '#14b143';
                            }
                            return colorList;
                        }
                        """
                        )
                    ),
                )
                .set_global_opts(
                    xaxis_opts=opts.AxisOpts(
                        type_="category",
                        grid_index=1,
                        axislabel_opts=opts.LabelOpts(is_show=False),
                    ),
                    legend_opts=opts.LegendOpts(is_show=False),
                )
            )
            
            line=(Line()
                .add_xaxis(xaxis_data=list(data.index))
                .add_yaxis(
                    series_name="ma5",
                    y_axis=data["ma5"].tolist(),
                    xaxis_index=1,
                    yaxis_index=1,
                    label_opts=opts.LabelOpts(is_show=False),
            ).add_yaxis(
                    series_name="ma10",
                    y_axis=data["ma10"].tolist(),
                    xaxis_index=1,
                    yaxis_index=1,
                    label_opts=opts.LabelOpts(is_show=False),
            ).add_yaxis(
                    series_name="ma20",
                    y_axis=data["ma20"].tolist(),
                    xaxis_index=1,
                    yaxis_index=1,
                    label_opts=opts.LabelOpts(is_show=False),
            )
            )
            

            grid_chart = Grid(
                init_opts=opts.InitOpts(
                    width="1800px",
                    height="1000px",
                    animation_opts=opts.AnimationOpts(animation=False),
                )
            )

            grid_chart.add_js_funcs("var barData={}".format(data[["open","close"]].values.tolist()))
            overlap_kline_line = kline.overlap(line)
            grid_chart.add(
                overlap_kline_line,
                #kline,
                grid_opts=opts.GridOpts(pos_left="11%", pos_right="8%", height="40%"),
            )
            grid_chart.add(
                bar,
                grid_opts=opts.GridOpts(
                    pos_left="10%", pos_right="8%", pos_top="60%", height="20%"
                ),
            )
            grid_chart.render(r'./results/ts9.html')

        if __name__=="__main__":
            data = pd.read_csv(r'./results/kline.csv',index_col=0)
            data.index = data.index.astype('datetime64[ns]')
            plot_kline_volume_signal(data)
    with open(r'./results/ts9.html') as f:
        cp.html(f.read(),width=1500,height=1500)

    