#전역 변수
hp = 30
exp = 0
lv = 1


def 밥먹기():
    global hp #global:전역 변수 끌어다 사용
    print('피카추 밥먹음')
    hp += 5
    return

def 잠자기(): #hp 10증가
    global  hp
    global  exp
    print('피카추가 이두를 조지고있습니다')
    hp -= 8
    exp += 8
    레벨업()
    으앙주금()

def 놀기():  #hp 4 감소, exp5증가, 살뒤체크
    global hp
    global exp
    print('피카츄가 클럽에서 흔들어재끼고있습니다')
    hp -= 4
    exp += 5
    레벨업()
    으앙주금()

def 운동하기():# hp 8감소, exp 12증가, 살뒤첵
    global hp
    global exp
    print('피카추가 이두를 조지고있습니다')
    hp -= 8
    exp += 8
    레벨업()
    으앙주금()



def 레벨업():#레벨업:exp20마다 레벨 1 증가
    global exp
    global lv
    if exp >20:
        print("라이츄에 가까워짐")
        lv+=1
        exp=0

def 으앙주금():
    if hp>0:
     print("피카츄 사름")
    else:
        print("피카츄 주금")

def printInfo():
    global hp, exp, lv



if __name__=='__main__':

    flag = True
    while flag:
        menu = int(input("피카츄가 할것을 골라보세요 1.밥먹기 2 잠자기 3놀기 4운동하기 5상태확인 6 종료"))
    if menu==1:
        밥먹기()
    elif menu == 2:
        잠자기()
    elif menu == 3:
        놀기()
    elif menu == 4:
        운동하기()
    elif menu == 5:
        flag=printInfo()
    elif menu==6:
        break
