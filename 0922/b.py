import json

#파일 오픈
file = open("BoxOfficeList.json", encoding='UTF8')
jsonData = json.load(file)#파일에서 로드한 데이터를 파싱
for key in jsonData:
    print(key,':', jsonData[key])
arr = jsonData['dailyBoxOfficeList']
for rk  in arr:
    print("rank:", rk['rank'])
    print("moviename:", rk['movieNm'])
    print("openDt:", rk['openDt'])
    print("salesAmt:", rk['salesAmt'])
    print("showCnt:", rk['showCnt'])



