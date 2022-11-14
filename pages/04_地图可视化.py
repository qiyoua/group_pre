import streamlit as st
import numpy as np
import pandas as pd
import streamlit.components.v1 as cp
from pyecharts.datasets import register_url
from pyecharts.globals import BMapType, ChartType
from pyecharts.charts import BMap
from pyecharts.globals import GeoType


tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8,tab9 = st.tabs(['1.1.点图:POI数据介绍','1.2.点图POI数据获取','1.3.点图:POI数据可视化','1.4.点图:核酸点的可视化','1.5.点图:空气质量点',
'2.1.线图:在地图上连线','2.2.线图:绘制路线图','3.1.面图:简单的热力图','3.2.香港人口密度可视化'])


with tab1:
    st.markdown("""<h5><center>什么是POI数据?</center></h5>""",unsafe_allow_html=True)
    col1,col2 = st.columns([1.5,1])
    with col1:
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
        cp.iframe('https://map.baidu.com/@12951162,4831749,13z',height=650,scrolling=True)



        
    
    with col2:
        # st.markdown(r'<br></br>',unsafe_allow_html=True)
        st.markdown("""<h6><center>一个简单的POI数据集</center></h6>""",unsafe_allow_html=True)
        st.dataframe(pd.read_excel('./results/covid_test.xlsx'))
        st.markdown("""<h6><center>一个复杂的POI数据集</center></h6>""",unsafe_allow_html=True)
        st.image('./results/复杂的poi.png')
        

with tab2:
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
    
    
with tab3:
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
            cp.html(content,height=600)
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
            cp.html(content,height=600,width=800)
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


with tab4:
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


with tab5:
    with open('./results/air.html','r') as f:
            content = f.read()
            cp.html(content,height=800)


with tab6:
    with open('./results/line1.html','r') as f:
            content = f.read()
            cp.html(content,height=800)


with tab7:
    with open('./results/line2.html','r') as f:
            content = f.read()
            cp.html(content,height=800)

with tab8:
    with open('./results/heatmap.html','r') as f:
            content = f.read()
            cp.html(content,height=800)

with tab9:
    with open('./results/hongkong.html','r') as f:
            content = f.read()
            cp.html(content,height=800)

