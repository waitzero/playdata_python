class Parent:
    def __init__(self, x=0):
        self.x = x

    def parent_method(self):
        print('x:', self.x)

#Parent를 상속받는 child
class Child(Parent):
    def __init__(self, x=0, y=0):
        super().__init__(x)
        print('child 생성자')
        self.y = y

    def child_method(self):
        print('x:', self.x)
        print('y:', self.y)
class Member:
    def __init__(self, name=''):
        print('member생성자')
        self.name = name

    def print_name(self):
        print('name:', self.name)

class Test(Parent, Member):
    def __init__(self, x=0, name=''):
        Parent.__init__(self, x=x)
        Member.__init__(self, name=name)
        print('Test 생성자')

if __name__=='__main__':
    p = Parent(1)
    p.parent_method()

    c=Child(2, 3)
    c.parent_method()
    c.child_method()

    t = Test(x=4, name='aaa')
    t.print_info()
    t.parent_method()
    t.print_name()