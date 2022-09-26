#list=>볂할수 있다, 요소:변할수 있다
#set=>변할수 있다. 요소:변할 수 없다.
#tuple=>변할수 없다. 요소:변할 수 있다.
#dictionary=>키와 값 저장. d['name']='aaa'


# #1.set
# #요소=>중복허용안한. 순서없음. 수정 불가능
# #생성
# set1={1,2,3,4}
# print(set1)
# print(type(set1))
# # set2={1,[2,3],4}#변경 가능한 요소는 안됨(에러남)
# #문자열
# set2={'aaa', 'bbb', 'ccc'}
# 'aaa'+'bbb'
# print(set2)
# print(type(set2))
# #문자열+정수
# set3={1,'aaa',(3,4)}
# print(set3)
# print(type(set3))
# set4=set([1,2,3,4])
# print(set4)

#2.tuple
#변경 불가, 요소자체는 변할수 있음
#고정된 집합 데이터를 저장, 요소를 추가, 삭제, 변경 안됨
#인덱스로 접근 가능
t1 = (1,2,3)
t2 = 4,5,6
t3 = tuple([6,7,8])
t4 = (5,)

print(t1)
print(type(t1))

print(t2)
print(type(t2))

print(t3)
print(type(t3))

print(t4)
print(type(t4))

for i in t1:
    print(i)

print('t1[0]:', t1[0])

#t1[0] = 10

def test():
    a = 10
    b = 20
    c = 30
    return a, b, c

res = test()
print(res)
print(type(res))

x, y, z = test()
print(x, y, z)




#dictionary
d1 = {'name':'aaa', 'age':12}
print(d1['name'])
print(d1['age'])

print(d1)
d1['tel']='111' #요소 추가. 새 키로 값 할당
print(d1)

d1['name']='bbb' #요소 값 변경
print(d1)

d1.pop('tel') #요소 삭제
print(d1)

