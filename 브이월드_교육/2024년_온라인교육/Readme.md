# 브이월드 2024년 온라인 교육

🙌 브이월드 온라인 교육을 ~~~

## 목차
1. [파일 다운로드](#파일-다운로드)
2. [🙋‍♀️ 2차시 교육](#🙋‍♀️‍-2차시 교육)

## 파일 다운로드
[📥 교육자료 다운로드](https://drive.usercontent.google.com/download?id=1Nu9fvBzGn4CKGFlAxc3yOyfABYf5HFDU&export=download&authuser=2)


## 🙋‍♀️ 2차시 교육
- folium 불러오기
```python
import folium

apikey='E5B1657B-9B6F-3A4B-91EF-98512BE931A1'
# 인증키는 언제든 삭제될 수 있으므로 인증키 발급 후 사용

map = folium.Map(
    location=[36.5, 127],
    zoom_start=7,
)
```
- 브이월드 배경지도 불러오기
```python
folium.TileLayer(
    tiles=f'https://api.vworld.kr/req/wmts/1.0.0/{apikey}/Base/{{z}}/{{y}}/{{x}}.png',
    attr='공간정보 오픈플랫폼(브이월드)',
    name='브이월드 배경지도',
).add_to(map)
```
![image](./images/브이월드%20배경지도%20불러오기.png)


- WMS(LX맵) 불러오기
```python
folium.WmsTileLayer(
    url='https://api.vworld.kr/req/wms?',
    layers='lt_c_landinfobasemap',
    request='GetMap',
    version='1.3.0',
    height=256,
    width=256,
    key=apikey,
    fmt='image/png',
    transparent=True,
    name='LX맵(편집지적도)',
).add_to(map)
```
- 레이어 컨트롤 기능 추가하기
```python
folium.LayerControl().add_to(map)
```
![image](./images/WMS(LX맵)%20불러오기.png)


[📥 3D모델 다운로드](https://drive.usercontent.google.com/download?id=1Nu9fvBzGn4CKGFlAxc3yOyfABYf5HFDU&export=download&authuser=2)