def sayHello():
    print('hello')
def main():
    funcObj = sayHello
    funcObj()
    sayHello()
main()

def error1():
    print('1번에러 방생')
def error2():
    print('2번에러 방생')
def error3():
    print('3번에러 방생')
def error4():
    print('4번에러 방생')
def main():
    ec=2
    if ec==1:
         error1()
    elif ec == 2:
        error2()
    elif ec == 3:
        error3()
    elif ec == 4:
        error4()
def main2():
    ec=2
    f=[error1, error2, error3, error4]
    f[ec-1]()
main2()
def onEvent(f):
    print("핸들러가 등록되었습니다.")
    f()
    print()
def myHandler1():
    print("1번 핸들러입니다.")
def myHandler2():
    print("2번 핸들러입니다.")
def myHandler3():
    print("3번 핸들러입니다.")
def main():
    onEvent(myHandler1())
    onEvent(myHandler2())
    onEvent(myHandler3())
main()
