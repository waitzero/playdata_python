# def add(a,b):
#     c=a+b
#     return c
#
#
#
# result = add(1,2)
# print('result:',result)

# def gugudan(dan):
#     for i range(1,10):
#         print(dan,'*',i,'=',dan*i)
# def main():
#     for i in range(2, 10):
#         print(i, '단')
#         gugudan(i)
#         print()
# main()

def argTest1(name, tel, age)->int: #->은 반환타입 지정. :은 파라미터 타입 지정
    print('name',name)
    print('tel',tel)
    print('age', age)
    print('12년후 age', age+12)


def argTest2(age, name='aaa', tel='111'):
    print('name:', name)
    print('tel:',tel)
    print('age',age)
    print('12년 후 age:', age+12)
#디폴트 인자:팡라메터의 기본값을 설정하며 호출시 인자전달 생략가능
def test(a:str='asd', b:int=0, c:int=0)->int: #->은 반환타입 지정. :은 파라메터 타입 지정
    print(a)
    print(b+c)
    return b+c

#가변인자: 파라메터 개수가 고정이 아님
def test2(*args): # *args: 가변인자
    print(type(args))
    print(args)
    return sum(args)

if __name__=='__main__':
    res = test('aaa', 1,2)
    print(res)

    #키워드 인자
    res = test(a='bbb', b=10, c=5)
    print(res)

    res = test()
    print(res)

    res = test('qwer')
    print(res)

    res = test('qwer', 1)
    print(res)

    res = test('qwer', 1, 2)
    print(res)

    s = test2(1,2,3)
    print(s)

    s = test2(1, 2, 3, 4, 5)
    print(s)

