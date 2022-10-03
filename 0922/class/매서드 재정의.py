class Point2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


    def print_points(self):
        print('(',self.x,',',self.y,')')

class Point3(Point2):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y)
        self.z = z

    def print_points(self):
        super().print_points()
        print('z:', self.z)




if __name__=='__main__':
    p = Point3(1,2,3)
    p.print_points()


