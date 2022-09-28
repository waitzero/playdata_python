class Test:
    val=3
    #생정자
    #모든 메서드의 첫 파라메터는 객체 참조값(this)
    def __init__(self, name='', age=0):
        #맴버변수 정의
        #self.이름 =>참조변수
        self.name = name
        self.age = age
        self.__y = 10 #private멤버__붙으면 프라이빗
        self.Y = self.__y

    def setY(self, y):
        self.__y = y

    def getY(self):
        return self.__y

    def print(self):
        print('name:', self.name)
        print('age:', self.age)
        print('__y:', self.__y)

    #클래스 레벨 메서드(정적메서드)
    def method():
        print('정적 메서드')
        print(Test.val)


if __name__=='__main__':
    print(Test.val)#val은 정적변수이므로 객체 생성 없이 사용 가능
    Test.method()
    t1 =Test()
    t1.print()
    print('t1.name:', t1.name)
    print('t1.age', t1.age)
    print('t1.__y:', t1.__y)
    t2 = Test(name='aaa')
    t2.print()

    t3= Test(name='bbb', age=45)
    t3.print()

    data=[]
    data.append(Test('ddd', 23))
    data.append(Test('ccc', 12))