# x =int(input("점수를 입력하세영:"))
#
# if x>90 and x<100:
#          print("a입니다")
# elif x>80 and x<89:
#          print("b입니다")
# elif x>70 and x<79:
#          print("c입니다")
# elif x>60 and x<69:
#          print("d입니다")
# elif x>0 and x<59:
#          print("f입니다")
# else:
#     print("0-100샤이의 정수만 입력 부탁드립니다")
#

# x=1
# y=1
# while x<=100:
#     if x % 2 == 1:
#         print (x)
#     x+=1
#  while x<= 100:
#      y= i+=1
#     print(y)
# for i in range(1, 100):
#     if i % 2 == 1:
#         print(i)
# x= 0
# for i in range(1, 100):
#     x = x+i
#     print(x)
#     #range(start, end, step-1):연속된 숫자 나열을 만들음
#     a= list(range(1, 11))
#     print(a)
#     b= list(range(1, 11, 2))
#     print(b)
#
#     for i in range(1, 101, 2):
#         print(i)
#     for i in range(1, 101, 2):
#         print(i)
#
#     s=0
#     for i in range(1, 101):
#         s+=i
#     print(s)
#
#     for i in[1,2,3,4,5]:
#         print(i, end=', ')
#         print()
#
#     for i in range(1, 10):
#         print('3 *',i ,'= ', 3*i)
#
#         for i in range(2, 10):
#             for j in range(1, 10):
#                 print(i,'*',j,'=', i*j)
#     for i in range(2, 10):
#         for f in range(2, 10):
#             print(j, '*', i, '=', i*j, end='\t\t')
#             print()



# x = -1
# while x < 0 or x > 100:
#     x = int(input("점수를 입력하세영:"))
#
# if x>90 and x<100:
#          print("a입니다")
# elif x>80 and x<89:
#          print("b입니다")
# elif x>70 and x<79:
#          print("c입니다")
# elif x>60 and x<69:
#          print("d입니다")
# elif x>0 and x<59:
#          print("f입니다")
# else:
#     print("0-100샤이의 정수만 입력 부탁드립니다")


# 각 사람의 정보를 딕셔너리로 처리
# 각 사람의 정보를 딕셔너리로 처리
#addr = {1:{'name':'asd','tel':'1111','address':'asf'}, 2:{}}
addr = {} #빈 딕셔너리
cnt = 1

#새 주소 등록
def add_addr():
    global cnt
    key = ['name', 'tel', 'address']
    # 한사람 정보 담을 딕셔너리
    member = {}
    for i in key:
        member[i]=input(i+':')
    addr[cnt]=member
    cnt+=1

# 전체 목록 출력
def print_all():
    for key in addr:#key(1,2,3...) 번호
        print('num:', key)
        print_mem(addr[key])

# 한명 정보/ 딕셔너리 한개 출력
def print_mem(mem): #param: {'name':'asd','tel':'1111','address':'asf'}
    for key in mem:  # member에서 번호,이름,전화,주소 하나씩 꺼냄
        print(key, ':', mem[key])  # 꺼낸 데이터 출력
    print('=============')

#번호로 검색
def search_by_num(num): # 검색할 번호 파람
    try:
        return num, addr[num]
    except KeyError:
        print('없는 번호')

#번호로 검색하여 출력
def print_by_num():
    num = int(input('검색할 사람의 번호:'))
    res = search_by_num(num)
    if res!=None:
        print('num:', res[0])
        print_mem(res[1])

def edit_addr():
    num = int(input('수정할 사람의 번호:'))
    res = search_by_num(num) #res:(num, dict)
    if res!=None:
        res[1]['tel']=input('new tel:')    #요소의 전화번호 수정
        res[1]['address']=input('new addr:')    #요소의 주소 수정

def del_addr():
    num = int(input('삭제할 사람의 번호:'))
    res = search_by_num(num)
    if res!=None:
        addr.pop(res[0])

'''
#이름으로 검색
def search_by_name(name):
    res = [] #이름 같은 사람들 담을 리스트
    for mem in addr: #addr에서 요소(mem) 하나씩 꺼냄
        if mem[1]==name: #mem에서 이름이 같은 요소 찾으면
            res.append(mem)  #res에 담음
    return res #검색 결과가 담긴 res반환


#이름으로 검색하여 출력
def print_by_name():
    name = input('검색할 사람의 이름:')
    mems = search_by_name(name)
    if len(mems)==0:
        print('없는 이름')
    else:
        for mem in mems:
            print_mem(mem)


'''
if __name__=='__main__':
    while True:
        m = input('1.등록 2.번호로검색 3.이름으로검색 4.수정 5.삭제 6.전체출력 7.종료')
        if m=='1':
            add_addr()
        elif m=='2':
            print_by_num()
            pass
        elif m=='3':
            #print_by_name()
            pass
        elif m=='4':
            edit_addr()
        elif m=='5':
            del_addr()
        elif m=='6':
            print_all()
        elif m=='7':
            break