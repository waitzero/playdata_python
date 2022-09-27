a=10#전역변수
def f1(x):#파라미터도 지역변수
    b=20#지역변수
    print('a:', a, 'b', b, 'x',x)
# def f2():#에러남 b와x는 f1()의 지역변수로 다른함수에서 사용불가
    # print('a:', a, 'b', b, 'x', x)

def f3():
    a=100#a 지역변수
    print('f3()에서 a:',a)
def f5():
    global a#a:전역변수
    a = 200
    print('fr5()에서a:', a)
def f4():
    print('f4()에서a:', a)
