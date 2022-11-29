import streamlit as st
import numpy as np
import pandas as pd
import streamlit.components.v1 as cp
from pyecharts.datasets import register_url
from pyecharts.globals import BMapType, ChartType
from pyecharts.charts import BMap
from pyecharts.globals import GeoType
from streamlit_option_menu import option_menu
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
# tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8,tab9 = st.tabs(['1.1.点图:POI数据介绍','1.2.点图POI数据获取','1.3.点图:POI数据可视化','1.4.点图:核酸点的可视化','1.5.点图:空气质量点',
# '2.1.线图:在地图上连线','2.2.线图:绘制路线图','3.1.面图:简单的热力图','3.2.香港人口密度可视化'])

with st.sidebar:
    menu = ['2.1.点图:POI数据介绍','2.2.点图POI数据获取','2.3.点图:POI数据可视化','2.4.点图:核酸点的可视化','2.5.点图:空气质量点',
'2.6.线图:在地图上连线','2.7.线图:绘制路线图','2.8.面图:简单的热力图','2.9.面图:香港人口密度']
    opt = option_menu(menu_title='2.空间数据可视化',options=menu,styles='sky')

if opt == menu[0]:
    st.markdown("""<h5><center>什么是POI数据?</center></h5>""",unsafe_allow_html=True)
    st.info(
        """
- 概念

POI（一般作为Point of Interest的缩写，也有Point of Information的说法），通常称作兴趣点，泛指互联网电子地图中的点类数据. 是地图上任何非地理意义的有意义的点, 如商店，酒吧，加油站，医院，车站等。像城市，河流，山峰这些具有地理意义的点就不属于POI.

- 来源

传统的地图测绘人员采用精密的测绘仪器去获取一个信息点的经纬度，然后再标记下来。像村委会村级行政区，还有部分政府机关单位，医院学校等国家单位的坐标点都是由gps测量得到的，每年的地理国情普查，土地调查等国家测绘项目都会进行更新。

现在地图上的POI一般是商家用手机gps和在线地图在地图平台上申请商户标注和认领，如店铺，旅店，商店超市等点。

- POI的属性

一条POI数据基本包含名称、地址、坐标、类别四个属性.当然也能包括更多属性,比如图片,城市等等.

复杂的POI数据是常常以json格式保存.`Python`用如下方式来加载json数据集.
"""
        )
    st.code("""
import json
with open('covid_test.json','r') as f:
    content = f.read()
json.loads(content)
        """)
    col1,col2 = st.columns([1,1])
    with col1:
        # st.markdown(r'<br></br>',unsafe_allow_html=True)
        st.markdown("""<h6><center>一个简单的POI数据集</center></h6>""",unsafe_allow_html=True)
        st.dataframe(pd.read_excel('./results/covid_test.xlsx'))
    with col2:
        st.markdown("""<h6><center>一个复杂的POI数据集</center></h6>""",unsafe_allow_html=True)
        with st.container():
            st.image('./results/复杂的poi.png',width=400)
    cp.iframe('https://map.baidu.com/@12951162,4831749,13z',height=650,scrolling=True)  
        
if opt == menu[1]:
    st.markdown("""<h5><center>如何获取POI数据</center></h5>""",unsafe_allow_html=True)
    col1,col2 = st.columns([1,1])
    with col1:
        st.info(
        """- 在各大平台的开放api里面爬取\n"""
        """比如:高德地图\n"""
        """[参考网址](https://lbs.amap.com/api/webservice/guide/api/search)""")
        st.code(
"""
# 高德地图爬取poi示例

# 获取poi
import requests

url = 'https://restapi.amap.com/v3/place/text?keywords=核酸&city=北京&offset=20&page=1&key=aa405328cd32f50fe58eb99d0d4c139b&extensions=all'
resp = requests.get(url)
poi = resp.json()

# 将数据保存到本地
poi_json = json.dumps(resp.json(),ensure_ascii=False)
with open('covid_test.json','w') as f:
    f.write(poi_json)
"""
        )
    with col2:
        st.info("""- 规划云提供免费爬取软件(仅Windows可用)"""
        """\n"""
        """[参考网址](http://guihuayun.com/poi/)""")
        st.image('./results/规划云.png')
       
if opt == menu[2]:
    try:
        register_url("https://echarts-maps.github.io/echarts-china-counties-js/")
    except Exception:
        import ssl
     
        ssl._create_default_https_context = ssl._create_unverified_context
        register_url("https://echarts-maps.github.io/echarts-china-counties-js/")
    st.markdown("""<h5><center>如何展示POI数据</h5></center>""",unsafe_allow_html=True)
    st.info(
        """
利用`pyecharts`包

- 安装方式

`pip install pyecharts`

- 安装地图

全球国家地图: echarts-countries-pypkg (1.9MB): 世界地图和 213 个国家，包括中国地图

`pip install echarts-countries-pypkg` 

中国省级地图: echarts-china-provinces-pypkg (730KB)：23 个省，5 个自治区

`pip install echarts-china-provinces-pypkg` 

中国市级地图: echarts-china-cities-pypkg (3.8MB)：370 个中国城市

`pip install echarts-china-cities-pypkg`

中国县区级地图: echarts-china-counties-pypkg (4.1MB)：2882 个中国县·区

`pip install echarts-china-counties-pypkg`

中国区域地图: echarts-china-misc-pypkg (148KB)：11 个中国区域地图，比如华南、华北。

`pip install echarts-china-misc-pypkg`

英国地图:echarts-united-kingdom-pypkg

`pip install echarts-united-kingdom-pypkg`
"""
        )

    st.markdown("""<h5><center>获取背景地图</center></h5>""",unsafe_allow_html=True)
    col1,col2 = st.columns([1,1])
    with col1:
        """- **方法一创建Map实例**"""
        with open('./results/map地图.html','r') as f:
            content = f.read()
            cp.html(content,height=600,width=400)
        with st.expander('代码'):
            st.code("""
            map_district = '海口'

c = (
    Map(init_opts=opts.InitOpts(height='600px',width='400px'))
    .add("标题", [list(z) for z in zip(Faker.country, Faker.values())], maptype=map_district)
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Map-%s地图" % map_district),
        visualmap_opts=opts.VisualMapOpts(max_=100),
    )
    .render('./results/map地图.html')
    
)""")

    with col2:
        """- **方法二创建Geo实例**"""
        with open('./results/geo地图.html','r') as f:
            content = f.read()
            cp.html(content,height=600)
        with st.expander('代码'):
            st.code("""
            from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.datasets import register_url

geo_district = '海淀区'
geo = (
    Geo(init_opts=opts.InitOpts(height='600px',width='400px'))
    .add_schema(maptype=geo_district)
    .set_global_opts(title_opts=opts.TitleOpts(title=geo_district))
    .render('./results/geo地图.html')
)""")
    """- **方法三 调用百度地图**"""
    col1,col2 = st.columns([2,1])
    with col1:
        with open('./results/bmap地图.html','r') as f:
            content = f.read()
            cp.html(content,height=600,width=700)
    with col2:
        st.code("""
                from pyecharts.charts import BMap
    bmap = (
        BMap()
        .add_schema(baidu_ak="3T3pZO6GVZGnMBBNA1BW2Ot1ShB2U8fU",
                        center=(121.45088,  31.25145) ,
                        zoom=1)
        .render('./results/bmap地图.html')    
    )
                """)

if opt == menu[3]:
    st.info(
"""前面我们获取了北京的部分核酸点的POI信息,现在我们将它们在地图上展示出来\n\n"""

"""我们可以在行政区域图上绘制,也可以在百度地图上绘制,接下来看看绘制的结果吧!"""
    )
    st.markdown("""<h5><center>处理数据</center></h5>""",unsafe_allow_html=True)
    col1,col2 = st.columns([1.5,1])
    with col1:
        st.code("""
    import numpy as np
import pandas as pd
from pyecharts.globals import BMapType, ChartType
from pyecharts.globals import GeoType
from pyecharts.charts import BMap
df = pd.read_excel('./results/covid_test.xlsx')
name = list(df.name.values)
loc = list(zip(df.lng,df.lat))
res = {}
for key,item in zip(name,loc):
    res[key] = list(item)
for idx,key in enumerate(res.keys()):
    res[key].append(df['address'].values[idx])
""")
        st.code("""   
import json
b = json.dumps(res,ensure_ascii=False)
f2 = open('test.json', 'w')
f2.write(b)
f2.close()
poi = [[key,value[-1]] for key,value in zip(res.keys(),res.values())]
    """)
    with col2:
        df = pd.read_excel('./results/covid_test.xlsx')
        name = list(df.name.values)
        loc = list(zip(df.lng,df.lat))
        res = {}
        for key,item in zip(name,loc):
            res[key] = list(item)
        for idx,key in enumerate(res.keys()):
            res[key].append(df['address'].values[idx])
            
        import json
        b = json.dumps(res,ensure_ascii=False)
        f2 = open('./results/test.json', 'w')
        f2.write(b)
        f2.close()
        poi = [[key,value[-1]] for key,value in zip(res.keys(),res.values())]
        
        poi[:5]

    st.markdown("""<h5><center>绘图</center></h5>""",unsafe_allow_html=True)
    col3,col4 = st.columns([1,1])
    with col3:
        """- 在轮廓图上标记"""
        with open('./results/covid1.html','r') as f:
            content = f.read()
            cp.html(content,height=800)
    with col4:
        """- 在百度地图上标记"""
        with open('./results/covid2.html','r') as f:
            content = f.read()
            cp.html(content,height=800)

if opt == menu[4]:
    with open('./results/air.html','r') as f:
            content = f.read()
            cp.html(content,height=800,width=1200)

if opt == menu[5]:
    st.code(
        """from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType

c = (
    Geo()
    .add_schema(
        maptype="china",
        itemstyle_opts=opts.ItemStyleOpts(color="#323c48", border_color="#111"),
    )
    .add(
        "",
        [("广州", 55), ("北京", 66), ("杭州", 77), ("重庆", 88)],
        type_=ChartType.EFFECT_SCATTER,
        color="white",
    )
    .add(
        "geo",
        [("广州", "上海"), ("广州", "北京"), ("广州", "杭州"), ("广州", "重庆")],
        type_=ChartType.LINES,
        effect_opts=opts.EffectOpts(
            symbol=SymbolType.ARROW, symbol_size=6, color="blue"
        ),
        linestyle_opts=opts.LineStyleOpts(curve=0.2),
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title="Geo-Lines-background"))
    .render('./results/line1.html')
    
)"""
    )
    with open('./results/line1.html','r') as f:
            content = f.read()
            cp.html(content,height=800,width=1200)

if opt == menu[6]:
    st.code(
        """
        import requests
from pyecharts.charts import BMap
from pyecharts import options as opts
from pyecharts.globals import BMapType, ChartType



# # 获取官方的数据


url = "https://echarts.apache.org/examples/data/asset/data/hangzhou-tracks.json"
data = requests.get(url).json()


map_data = [[y["coord"] for y in x] for x in data]

c = (
    BMap(init_opts=opts.InitOpts(width="1600px", height="800px"))
    .add_schema(
        baidu_ak="3T3pZO6GVZGnMBBNA1BW2Ot1ShB2U8fU",
        center=[120.13066322374, 30.240018034923],
        zoom=13,
        is_roam=True,
        map_style={
            "styleJson": [
                {
                    "featureType": "water",
                    "elementType": "all",
                    "stylers": {"color": "#d1d1d1"},
                },
                {
                    "featureType": "land",
                    "elementType": "all",
                    "stylers": {"color": "#f3f3f3"},
                },
                {
                    "featureType": "railway",
                    "elementType": "all",
                    "stylers": {"visibility": "off"},
                },
                {
                    "featureType": "highway",
                    "elementType": "all",
                    "stylers": {"color": "#fdfdfd"},
                },
                {
                    "featureType": "highway",
                    "elementType": "labels",
                    "stylers": {"visibility": "off"},
                },
                {
                    "featureType": "arterial",
                    "elementType": "geometry",
                    "stylers": {"color": "#fefefe"},
                },
                {
                    "featureType": "arterial",
                    "elementType": "geometry.fill",
                    "stylers": {"color": "#fefefe"},
                },
                {
                    "featureType": "poi",
                    "elementType": "all",
                    "stylers": {"visibility": "off"},
                },
                {
                    "featureType": "green",
                    "elementType": "all",
                    "stylers": {"visibility": "off"},
                },
                {
                    "featureType": "subway",
                    "elementType": "all",
                    "stylers": {"visibility": "off"},
                },
                {
                    "featureType": "manmade",
                    "elementType": "all",
                    "stylers": {"color": "#d1d1d1"},
                },
                {
                    "featureType": "local",
                    "elementType": "all",
                    "stylers": {"color": "#d1d1d1"},
                },
                {
                    "featureType": "arterial",
                    "elementType": "labels",
                    "stylers": {"visibility": "off"},
                },
                {
                    "featureType": "boundary",
                    "elementType": "all",
                    "stylers": {"color": "#fefefe"},
                },
                {
                    "featureType": "building",
                    "elementType": "all",
                    "stylers": {"color": "#d1d1d1"},
                },
                {
                    "featureType": "label",
                    "elementType": "labels.text.fill",
                    "stylers": {"color": "#999999"},
                },
            ]
        },
    )
    .add(
        series_name="",
        type_=ChartType.LINES,
        data_pair=map_data,
        is_polyline=True,
        is_large=True,
        linestyle_opts=opts.LineStyleOpts(color="purple", opacity=0.6, width=1),
        effect_opts=opts.EffectOpts(trail_length=0.5),
    )
    .add_control_panel(
        copyright_control_opts=opts.BMapCopyrightTypeOpts(position=3),
        maptype_control_opts=opts.BMapTypeControlOpts(
            type_=BMapType.MAPTYPE_CONTROL_DROPDOWN
        ),
        scale_control_opts=opts.BMapScaleControlOpts(),
        overview_map_opts=opts.BMapOverviewMapControlOpts(is_open=True),
        navigation_control_opts=opts.BMapNavigationControlOpts(),
        geo_location_control_opts=opts.BMapGeoLocationControlOpts(),
    )
    .render('./results/line2.html')
    
)
        """
    )
    with open('./results/line2.html','r') as f:
            content = f.read()
            cp.html(content,height=1000,width=1200)

if opt == menu[7]:
    st.code(
        """
        from pyecharts import options as opts
from pyecharts.charts import BMap
from pyecharts.faker import Faker

c = (
    BMap()
    .add_schema(baidu_ak="3T3pZO6GVZGnMBBNA1BW2Ot1ShB2U8fU", center=[120.13066322374, 30.240018034923])
    .add(
        "bmap",
        [list(z) for z in zip(Faker.provinces, Faker.values())],
        type_="heatmap",
        label_opts=opts.LabelOpts(formatter="{b}"),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="BMap-热力图"), visualmap_opts=opts.VisualMapOpts()
    )
)
c.render('./results/heatmap.html')
        """
    )
    with open('./results/heatmap.html','r') as f:
            content = f.read()
            cp.html(content,height=1000,width=1200)

if opt == menu[8]:
    st.code(
        """
        import ssl

import pyecharts.options as opts
from pyecharts.charts import Map
from pyecharts.datasets import register_url


# Gallery 使用 pyecharts 1.1.0 和 echarts-china-cities-js
# 参考地址: https://echarts.apache.org/examples/editor.html?c=map-HK

ssl._create_default_https_context = ssl._create_unverified_context
# 与 pyecharts 注册，当画香港地图的时候，用 echarts-china-cities-js
register_url("https://echarts-maps.github.io/echarts-china-cities-js")

WIKI_LINK = (
    "http://zh.wikipedia.org/wiki/"
    "%E9%A6%99%E6%B8%AF%E8%A1%8C%E6%94%BF%E5%8D%80%E5%8A%83#cite_note-12"
)
MAP_DATA = [
    ["中西区", 20057.34],
    ["湾仔", 15477.48],
    ["东区", 31686.1],
    ["南区", 6992.6],
    ["油尖旺", 44045.49],
    ["深水埗", 40689.64],
    ["九龙城", 37659.78],
    ["黄大仙", 45180.97],
    ["观塘", 55204.26],
    ["葵青", 21900.9],
    ["荃湾", 4918.26],
    ["屯门", 5881.84],
    ["元朗", 4178.01],
    ["北区", 2227.92],
    ["大埔", 2180.98],
    ["沙田", 9172.94],
    ["西贡", 3368],
    ["离岛", 806.98],
]


NAME_MAP_DATA = {
    # "key": "value"
    # "name on the hong kong map": "name in the MAP DATA",
    "中西区": "中西区",
    "东区": "东区",
    "离岛区": "离岛",
    "九龙城区": "九龙城",
    "葵青区": "葵青",
    "观塘区": "观塘",
    "北区": "北区",
    "西贡区": "西贡",
    "沙田区": "沙田",
    "深水埗区": "深水埗",
    "南区": "南区",
    "大埔区": "大埔",
    "荃湾区": "荃湾",
    "屯门区": "屯门",
    "湾仔区": "湾仔",
    "黄大仙区": "黄大仙",
    "油尖旺区": "油尖旺",
    "元朗区": "元朗",
}

c = (
    Map(init_opts=opts.InitOpts(width="1400px", height="800px"))
    .add(
        series_name="香港18区人口密度",
        maptype="香港",
        data_pair=MAP_DATA,
        name_map=NAME_MAP_DATA,
        is_map_symbol_show=False,
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="香港18区人口密度 （2011）",
            subtitle="人口密度数据来自Wikipedia",
            subtitle_link=WIKI_LINK,
        ),
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{b}<br/>{c} (p / km2)"
        ),
        visualmap_opts=opts.VisualMapOpts(
            min_=800,
            max_=50000,
            range_text=["High", "Low"],
            is_calculable=True,
            range_color=["lightskyblue", "yellow", "orangered"],
        ),
    )  
)
c.render('./results/hongkong.html')
        """)
    with open('./results/hongkong.html','r') as f:
            content = f.read()
            cp.html(content,height=800)

