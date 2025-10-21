#pip install folium===0.16.0
import folium

apikey='E5B1657B-9B6F-3A4B-91EF-98512BE931A1'

map = folium.Map(
    location=[36.5, 127],
    zoom_start=7,
)


folium.TileLayer(
    tiles=f'https://api.vworld.kr/req/wmts/1.0.0/{apikey}/Base/{{z}}/{{y}}/{{x}}.png',
    attr='공간정보 오픈플랫폼(브이월드)',
    name='브이월드 배경지도',
).add_to(map)


folium.WmsTileLayer(
    url='https://api.vworld.kr/req/wms?',
    layers='lt_c_landinfobasemap',
    request='GetMap',
    version='1.3.0',
    height=256,
    width=256,
    key=apikey,
    fmt='image/png', #브이월드는 format=image/png이지만 folium은 fmt=image/png를 이용한다.
    transparent=True, #주제도 투명도
    name='LX맵(편집지적도)',
).add_to(map)

folium.LayerControl().add_to(map) # 레이어 컨트롤기능 추가

"""
브이월드의 API들은 x y 순으로 되어있으나 leaflet(folium)은 y x 순으로 되어있으므로 순서를 바꿔 이용해야한다.
"""

address = [
    ['시흥시청', '경기도 시흥시 시청로 20'],
    ['시흥도시공사', '경기도 시흥시 시흥대로 268번길 8'],
    ['시흥어울림국민체육센터1', '경기도 시흥시 정왕대로233번길 33'],
]

import requests

apiurl = 'https://api.vworld.kr/req/address?'
for addr in address:
    params = {
        'service': 'address',
        'request': 'getcoord',
        'crs': 'epsg:4326',
        'address': addr[1],
        'format': 'json',
        'type': 'ROAD', # 지번주소일 경우 PARCEL
        'key': apikey
    }
    response = requests.get(apiurl, params=params)
    if response.status_code == 200:
        data = response.json()

        print(data['response']['result']['point']) # 브이월드는 x y 순으로 가져온다
        x = data['response']['result']['point']['x']
        y = data['response']['result']['point']['y']

        folium.Marker([y, x],
                      popup = folium.Popup(f'<b>{addr[0]}</b><br>{addr[1]}', max_width=200),
                      icon = folium.Icon(color='red', icon='bookmark') # 아이콘 색상 변경(red, blue 등) 및 아이콘 변경(home, star, flag, cloud, heart, bookmark 등)
        ).add_to(map) # folium은 y x 순으로 받는다.


map.save('map.html')

"""
파이썬 지오코딩 심화버전
"""
#pip install pandas===2.2.2
##pip install openpyxl===3.1.2

import pandas as pd

df = pd.read_excel('관심지점.xlsx')
apiurl = 'https://api.vworld.kr/req/address?'
for i in df.index:
    params = {
        'service': 'address',
        'request': 'getcoord',
        'crs': 'epsg:4326',
        'address': df['주소'][i],
        'format': 'json',
        'type': 'PARCEL',
        'key': apikey
    }
    response = requests.get(apiurl, params=params)
    if response.status_code == 200:
        data = response.json()

        x = data['response']['result']['point']['x']
        y = data['response']['result']['point']['y']

        folium.Marker([y, x],
                      popup = folium.Popup(f'<b>{df["명칭"][i]}</b><br>{df["주소"][i]}', max_width=200),
                      icon = folium.Icon(color='blue', icon='star')
        ).add_to(map)

map.save('map2.html')