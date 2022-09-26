import json
''''
data='{"num:" 1, "name": "aaa"}'
jsonObject = json.loads(data)#string json data parsing
print(jsonObject.get("num"))#get()함수로 키값 읽음
print(jsonObject.get("name"))#딕셔너리 키 읽기


data='[{"num:" 1, "name": "aaa"},{"num:" 2, "name": "bbb"}, {"num:" 1, "name": "ccc"}]'
jsonArray= json.loads(data)#string json data parsing
for i in jsonArray:
    print(i.get("num"))
    print(i.get("nuim"))
'''
#파일오픈
file = open('data.json')
jsonData = json.load(file)#파일에서 로드한 데이터를 파싱
for key in jsonData:
    print(key,':', jsonData[key])

# obj = jsonData['metadata']
# for key in obj:
#     print(key, obj.get(key))
# arr = jsonData['frames']
# for fr in arr:
#     print('number:', fr['number'])
#     print('image', fr['image'])
#     anns = fr['annotations']
#     for a in anns:
#         print('x', a['label']['x'])
#         print('y', a['label']['y'])
#         print('category code:', a['category']['code'])