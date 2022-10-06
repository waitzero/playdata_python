import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
dao없이 vo, service, menu로 구성
service에서 엑셀 파일 로드

기능
1. 영화 이름으로 검색
2. 1~10위 영화 제목 출력
3. 예매 점유율로(1~5위) 파이 그래프 출력
4. 개봉일로 검색(연도-월)
'''

class Movie:
    def __init__(self, rank=0, mvName='',opendt='', salesAmt=0, audiCnt=0):
        self.rank = rank
        self.mvName = mvName
        self.opendt = opendt
        self.salesAmt = salesAmt
        self.audiCnt = audiCnt

    def __str__(self):
        return '순위:'+str(self.rank)+'\n'+ '영화명:'+self.mvName+'\n'+ '개봉일:' + self.opendt + '\n' + '일매출:'+str(self.salesAmt)+'\n' +'누적관객수:' + str(self.audiCnt) + '\n-----------------\n'

class service:
    df = pd.read_excel('영화순위.xlsx', engine='openpyxl')


    def search(point, df):
            return df[df['영화명']==point]

    def printrank(self, df):
        return df[0:9]


    def pi(self, df):
        ex = (0, 0, 0, 0, 0)  # 각 부채꼴 떨어뜨릴 거리. 0인 요소는 붙어서 출력됨
        df[df['영화명']['2:6 ']]
        result = df[df['예매점유율']['2:6']]
        plt.pie(result, labels="영화 예매점유율", autopct='%.1f%%', counterclock=False,
                startangle=90, explode=ex)
        plt.show()
#         return
#     def searchday(self, df):
#         return df[df[]]
#
#
# class vo:
#
#
#
#
#
#
# class menu:
#
#
#
