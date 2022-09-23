# l1 =[1, 2, 3]
# #요소로 접근
# for i in l1:#li의 요소를 하나씩 꺼내서 i에 할당하여 루프에서 사용
#     print(i)
# #인덱스로 접근
# for i in range(0, len(l1)):#range로 인덱스 값 생성(0, 1, 2).
#     print(l1[i])
#
# l1[2] = 40
# print(l1[2])
#
# # l1[3] = 4#에러
# l1.append(4)#끝에 방을 추가하고 새 방에 값 할당
# print(l1)
#빈 리스트 l2를 정의하고 숫자 5개를 키보드 입력 받아 리스트에 저장하고 출력
# l2=[]
# for i in range(0, 5):
#     l2.append(int(input("num", i ,":")))
 # print(l2)
#
# l3 = [[1,2,3][4,5,6]]
# for i in l3:
#     for j in i:
#         print(j, end=', ')
#     print(
#     )

# #점수 담을 리스트
# score = []
# title=['kor', 'eng', 'math', 'total']
# for i in range(3):
#     data = [0,0,0,0]
#     for j in range(3):
#         data[j] = int(input(title[j]+':'))
#         data[3] += data[j]
#         score.append(data)
# print(score)

# l4 = ['aaa', 'bbb', 'ccc']
# for idx, data in enumerate(l4):
#     print(idx, ':', data)
# print(l4[1:3])
# print(l4[:3])
# print(l4[1:])
# print(l4[1:5:2])#1~4번방까지 2간격으로 데이터 추출

#리스트 요소 추가
# list1 =[1,2,3,4]
#추가
#list1[3] =4
# list1[3] =4
# list1.append(4)
# print(list1)

# if 'abc' in l4:
#     print(val, 'rlq')
addr = []
cnt = 1

#새 주소 등록
def add_addr():
    global cnt
    member = []
    member.append(cnt) # 번호 자동 할당
    cnt+=1
    member.append(input('name:')) #이름입력
    member.append(input('tel:')) #전화입력
    member.append(input('address:')) #주소입력
    addr.append(member)

# 전체 목록 출력
def print_all():
    for mem in addr:#요소(member)를 하나씩 추출
        print_mem(mem)

def print_mem(mem):
    for data in mem:  # member에서 번호,이름,전화,주소 하나씩 꺼냄
        print(data, end=' / ')  # 꺼낸 데이터 출력
    print()

#번호로 검색
def search_by_num(num): # 검색할 번호 파람
    for mem in addr: #addr에서 한명씩 꺼내서
        if mem[0]==num: #각 사람의 번호와 num이 같으면
            return mem #그 사람 리스트 반환(참조값)

#이름으로 검색
def search_by_name(name):
    res = [] #이름 같은 사람들 담을 리스트
    for mem in addr: #addr에서 요소(mem) 하나씩 꺼냄
        if mem[1]==name: #mem에서 이름이 같은 요소 찾으면
            res.append(mem)  #res에 담음
    return res #검색 결과가 담긴 res반환

def print_by_num():
    num = int(input('검색할 사람의 번호:'))
    mem = search_by_num(num)
    if mem==None:
        print('없는 번호')
    else:
        print_mem(mem)

def print_by_name():
    name = input('검색할 사람의 이름:')
    mems = search_by_name(name)
    if len(mems)==0:
        print('없는 이름')
    else:
        for mem in mems:
            print_mem(mem)

if __name__=='__main__':
    while True:
        m = input('1.등록 2.번호로검색 3.이름으로검색 4.수정 5.삭제 6.전체출력 7.종료')
        if m=='1':
            add_addr()
        elif m=='2':
            print_by_num()
        elif m=='3':
            print_by_name()
        elif m=='4':
            pass
        elif m=='5':
            pass
        elif m=='6':
            print_all()
        elif m=='7':
            break




