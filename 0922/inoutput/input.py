'''
r:읽기.파일없다 에러
read()읽기 작업
w:쓰기. 파일이 없으면 생성해서 오픈
내용을 싹 지우고 오픈
q:이어쓰기
'''

# f=open('../함수/재귀함수.py', 'r', encoding='utf-8')
# content = f.read()#전체내용읽기
# print(content)
# f.close()
# print("===========")
#
# f=open('c.txt', 'w', encoding='utf-8')
# while True:
#     msg = input('내용입력(멈추려면 /strop입력)')#한줄씩 읽기
#     if msg== '/stop':
#         break
#     f.write(msg+'\n')
# f.close()
'''
f=open('c.txt', 'w', encoding='utf-8')
f.write('여기부터는 추가된 내용\n')
f.write('난 마카오 난 조마에요\n')
'''

f = open('c.txt','rb')
s = f.read(4)
print(s)
print('현재위치:', f.tell())#tell():현재 커서 위치
f.seek(5, 1)
print('현재위치:', f.tell())
ch = f.read(1)
print('ch:', ch)

