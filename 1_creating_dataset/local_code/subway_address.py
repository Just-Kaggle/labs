from urllib.parse import quote    
from urllib.request import urlopen
import json
import sys
import requests
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)


import sys

subway_place = pd.read_csv("data/subway_addr.csv",header=0)

print(subway_place[subway_place['addr'].isna() == True])

for name in subway_place[subway_place['addr'].isna() == True]['name']:
  break
  print(name)

  #name = '주안'
  #name = ''

  requestURL = 'http://swopenapi.seoul.go.kr/api/subway/(your_key1)/json/stationInfo/0/999/' + quote(name)
  
  site = urlopen(requestURL)
  html = site.read().decode('utf-8')
  #print(html)

  json_station_result = json.loads(html)
  #print(json_station_result)
  #print(json_station_result['stationList'][0]['adresBass'])
  #print(json_station_result['stationList'][0]['adresDetail'])

  for index in range(len(json_station_result)):
    try:
      adresBass = json_station_result['stationList'][index]['adresBass']
      adresDetail = json_station_result['stationList'][index]['adresDetail']

      adresBassSplit = adresBass.split(' ')
      dong = ''
      print(adresBassSplit[0][0:2])
      if adresBassSplit[0][0:2] != '서울':
        print('서울아님')
        subway_place.loc[subway_place['name'] == name, ['addr']] = '서울아님'
        break;
      for addr in adresBassSplit:
        if addr[-1] == '동' or addr[-1] == '가':
          dong = addr
          print("한번에" + dong)
          subway_place.loc[subway_place['name'] == name, ['addr']] = dong
          #print(subway_place[subway_place['name']  == name]['addr'])
          break
      if dong != '':
        break

      dong = adresBassSplit[-1] + adresDetail.split(' ')[0]
      if '동' in dong or '가' in dong:
        print("조합1" + dong)
        #print(subway_place[subway_place['name']  == name])
        #print(subway_place[subway_place['name']  == name]['addr'])
        subway_place.loc[subway_place['name'] == name, ['addr']] = dong
        #subway_place[subway_place['name' == name]]['addr'] = dong
        #print("조합2" + dong)
        #print(subway_place[subway_place['name']  == name]['addr'])
        break
    except:
      continue



#    break
#  break

print(subway_place)
#pd.DataFrame(subway_place,columns = ["name","addr"]).to_csv("subway_addr2.csv",mode="a")
