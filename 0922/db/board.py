import pymysql
addr = {} #빈 딕셔너리
cnt = 1
class Board:
        def __init__(self, num=0, writer='', w_date='', title='', content=''):
            self.num = num
            self.writer = writer
            self.w_date = w_date
            self.title = title
            self.content = content

        def __str__(self):
            return 'num:'+str(self.num)+' / writer:'+self.writer+' / w_date:'+self.w_date+' / title:'+self.title+' / content:'+self.content
class BoardDao:
    def conn(self):
        return pymysql.connect(host='localhost', user='root', password='1234', db='python', charset='utf8')

    #글작성
    def insert(self, b:Board):
        #db연결
        conn = self.conn()
        #사용할 커서 객체 생성
        cursor = conn.sursor()
        #실행할 sql문을 정의
        sql = 'insert into board value(%s, %s, %s, %s, %s)'
        #sql문 %s에 매칭 값 튜플에 저장
        d =(b.num, b.writer, b.w_date, b.title, b.content)
        #sql문 실행
        cursor.execute(sql, d)
        #쓰기 작업 커밋
        conn.commit()
        #db를 끊어라
        conn.close()
        
    #글 번호로 검색하여 Board 객체 반환
    def select(self, num:int)->Board:
        conn = self.conn()
        cursor = conn.cursor()
        sql= 'select * from board where num=%s'
        cursor.execute(sql, num)
        row = cursor.fetchone()  # 커서에서 한줄만 추출
        conn.close()
        if row:
            return Board(row[0], row[1], row[2], row[3])
    #글 작성자로 검색
    def select_by_writer(self, writer:str)->list:
        conn = self.conn()
        cursor = conn.cursor()
        sql = 'select * from board where writer=%s'
        cursor.execute(sql, writer)
        row = cursor.fetchone()
        if row:
            return Board(row[0], row[1], row[2], row[3])
    #글 타이틀로 검색하여 리스트 반환(like 패턴 검색)
    def select_by_title(self, title:str)->list:
        conn = self.conn()
        cursor = conn.cursor()
        sql = 'select * from board where title=%s'
        cursor.execute(sql, title)
        row = cursor.fetchone()
        if row:
            return Board(row[0], row[1], row[2], row[3])
    #글 수정, 글 번호로 찾아서 title, content는 입력 받은 값으로 수정, w date는 현재(now())날짜로 수정
    def update(self, b:Board):
        conn = self.conn()
        cursor = conn.cursor()
        sql = 'update board set title=%s, content=%s w-date=%s, where num=%s'
        d = (b.title, b.content, b.w_date.now())
        cursor.execute(sql, d)
        conn.commit()
        conn.close()
    #글 삭제
    def delete(self, num:int):
        conn = self.conn()
        cursor = conn.cursor()
        sql = 'delete from board where num=%s'
        cursor.execute(sql, num)
        conn.commit()
        conn.close()

class BoardService:

    def __init__(self):
        self.dao = BoardDao()
    def add(self):
        global cnt
        key=['','','','','',]

    def id_check(self, id: str) -> bool:
        b: Board = self.dao.select(id)
        return b == None  # 중복안되면 True, 아니면 False반환
    # 글작성
    def insert(self, b: Board):
        print("글작성")
        content = input('content')
        title = input('title')


    def search_by_num(num):  # 검색할 번호 파람
        try:
            return num, addr[num]
        except KeyError:
            print('없는 번호')

    # 글 번호로 검색하여 Board 객체 반환
    def get_one(self, num: int) -> Board:
        num = int(input('검색할 글'))
        res = self.search(num)
        if res!=None:
            print('num', res[0])
        else:
            print("값이 없는데용")

    # 글 작성자로 검색
    def get_by_writer(self, writer: str) -> list:
        writer = input("검색할 작성자")
        res = self.get_by_writer(writer)
        if res!=None:
            print('writer', res[0])
        else:
            print("값이 없다")
    # 글 타이틀로 검색하여 리스트 반환(like 패턴 검색)
    def get_by_title(self, title: str) -> list:
        pass

    # 글 수정, 글 번호로 찾아서 title, content는 입력 받은 값으로 수정, w date는 현재(now())날짜로 수정
    def edit(self, b: Board):
        pass

    # 글 삭제
    def delete(self, num: int):
        pass