import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from urllib.parse import quote    
from urllib.request import urlopen
#from urllib.request import urlopen
import urllib.request
import sys
import requests

bus_coordinate = pd.read_csv("data/seoul_bus_coordinate_copy.csv", encoding='euc_kr',dtype=str)
print(bus_coordinate.head())

coordinate = ''
index = 0
csv_data = []
for i in range(len(bus_coordinate)):
  print(bus_coordinate.loc[i,'X좌표'])
  print(str(bus_coordinate.loc[i,'X좌표']) + ',' + str(bus_coordinate.loc[i,'Y좌표']))
  coordinate = str(bus_coordinate.loc[i,'X좌표']) + '%2C' + str(bus_coordinate.loc[i,'Y좌표'])
  #print(bus_coordinate[0,'X좌표'] + ',' + bus_coordinate[0,'X좌표'])
  #if index == 1: break
  #print(str(i['X좌표']) + ',' + str(i['Y좌표']))
  #index += 1

  terminal_num = str(bus_coordinate.loc[i,'정류소번호'])
  if len(terminal_num) == 4:
      terminal_num = '0' + terminal_num

  '''
  requestURL = 'http://swopenapi.seoul.go.kr/api/subway/(your_key1)/xml/stationInfo/0/999/' + quote(name)
  site = urlopen(requestURL)
  html = site.read().decode('utf-8')
  '''

#{'Connection': 'keep-alive', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'User-Agent': 'python-requests/2.13.0'}

#!curl --location --request GET 'http://api.vworld.kr/req/address?service=address&request=getAddress&key=(your_key2)&point=126.9877498816,37.569765125100005&type=PARCEL'

  print(coordinate)
  requestURL = 'http://api.vworld.kr/req/address?service=address&request=getAddress&version=2.0&format=xml&crs=epsg:4326&type=PARCEL&zipcode=false&simple=false&key=24439DF9-DA66-3236-AF47-76D0F520E805&point=' + coordinate
#126.9877498816,37.569765125100005
#print(requestURL)

  site = urlopen(requestURL)
  html = site.read().decode('utf-8')
  print(html)
  try:
    dong_list = html.split("<level4L><![CDATA[")
    dong = dong_list[1].split("]]></level4L>")[0]
  except:
    dong = 'null'
  print(dong)
  arr = [terminal_num, dong]
  print(arr)
  csv_data = []
  csv_data.append(arr)
  pd.DataFrame(csv_data,columns = ["id","dong"]).to_csv("terminal_coordinate.csv",mode="a")
