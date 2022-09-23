# x =int(input("점수를 입력하세영:"))
#
# if x>90 and x<100:
#          print("a입니다")
# elif x>80 and x<89:
#          print("b입니다")
# elif x>70 and x<79:
#          print("c입니다")
# elif x>60 and x<69:
#          print("d입니다")
# elif x>0 and x<59:
#          print("f입니다")
# else:
#     print("0-100샤이의 정수만 입력 부탁드립니다")
#

# x=1
# y=1
# while x<=100:
#     if x % 2 == 1:
#         print (x)
#     x+=1
#  while x<= 100:
#      y= i+=1
#     print(y)
# for i in range(1, 100):
#     if i % 2 == 1:
#         print(i)
# x= 0
# for i in range(1, 100):
#     x = x+i
#     print(x)
#     #range(start, end, step-1):연속된 숫자 나열을 만들음
#     a= list(range(1, 11))
#     print(a)
#     b= list(range(1, 11, 2))
#     print(b)
#
#     for i in range(1, 101, 2):
#         print(i)
#     for i in range(1, 101, 2):
#         print(i)
#
#     s=0
#     for i in range(1, 101):
#         s+=i
#     print(s)
#
#     for i in[1,2,3,4,5]:
#         print(i, end=', ')
#         print()
#
#     for i in range(1, 10):
#         print('3 *',i ,'= ', 3*i)
#
#         for i in range(2, 10):
#             for j in range(1, 10):
#                 print(i,'*',j,'=', i*j)
#     for i in range(2, 10):
#         for f in range(2, 10):
#             print(j, '*', i, '=', i*j, end='\t\t')
#             print()



x = -1
while x < 0 or x > 100:
    x = int(input("점수를 입력하세영:"))

if x>90 and x<100:
         print("a입니다")
elif x>80 and x<89:
         print("b입니다")
elif x>70 and x<79:
         print("c입니다")
elif x>60 and x<69:
         print("d입니다")
elif x>0 and x<59:
         print("f입니다")
else:
    print("0-100샤이의 정수만 입력 부탁드립니다")
