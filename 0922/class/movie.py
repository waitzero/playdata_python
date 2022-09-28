import json
#영화명, 순위, 일매출액, 누적관객수, 개봉일


file = open("../BoxOfficeList.json")
jsonData = json.load(file)
arr= jsonData['dailyBoxOfficeList']
class Movie:

    #생성자
    def __init__(self, rnum="", rrank="", audiCnt="", salesAmt="", moviceCd=""):
        self.rnum = rnum
        self.rrank = rrank
        self.audiCnt = audiCnt
        self.salesAmt = salesAmt
        self.moviceCd = moviceCd
    def __str__(self) -> str:
            return 'num:'+str(self.rnum)+' /n rank:'+str(self.rrank)+' /n audiCnt:' + str(self.audiCnt)+' /n salesAmt:' + str(self.salesAmt)+'/n movieCd:' + str(self.moviceCd)
class Dao:
        def __init__(self):
            file = open("../BoxOfficeList.json")
            jsonData = json.load(file)
            self.data = jsonData['dailyBoxOfficeList']

        def select(self, rnum:int):
            for m in self.data:
                if m.rnum == rnum:
                 return m
class Service:
    def __init__(self, dao:Dao):
        self.dao = dao
    def get_by_num(self):
        rnum = int(input("검색할 번호:"))
        m:Member = self.dao.select(rnum)
        if m == None:
            print('없는번호')
