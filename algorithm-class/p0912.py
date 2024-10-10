# 9월 12일 파이썬 기본 문법

# error 종류
# 1. 구문 에러(syntax Error)
#   - 컴퓨터 언어 문법에 어긋날 때
# 2. 논리 에러(logical Error)
#   - 알고리즘상에 문제가 발생했을 때
#       for i in range(100): / 1~99까지 100이 되는 순간 빠져나온다.
# 3. 의미 에러(semantic Error)
#   - 인간이 사용하는 문법과 컴퓨터 문법이 상이할 때

#import math
#from math import pi

#math.sin()

# 예제 1. 두 수를 입력 받아서 더하기 프로그램
def plusFn():
    # a = int(input("값 입력 >> "))
    # b = int(input("값 입력 >> "))
     
    # print(f"a의 타입 {type(a)}")
    # print(f"b의 타입 {type(b)}")
     
    #  -- 중요 --
    # a , b = map(int, input("값 입력 >> ").split())
    # iList = list(map(int,input("값 입력 >> ").split()))
    # a = iList[0] ; b = iList[1]
    # print(iList)
    

    # -- Debug --
    a = 3 ; b = 5
        
    c = a + b
    print(f"{a} + {b} = {c}")
    
    # 고등학생 : a + bi
    # 대학생 : i : 전류, a + jb
    # python : a+bj (숫자인지 문자인지 구분이 안가기 때문에 뒤에 j를 붙임)
    #d = 3 + 4j
    #print(f"{d}, 실수부 : {d.real}, 허수부 : {d.imag}")
    #print(f"d.real 타입 : {type(d.real)}")
    
# 입력데이터까지 더하기
def plusHandred():
    # inputData = int(input("값 입력 >> "))
    
    # -- Debug --
    inputData = 100
    
    Total = 0
    for i in range(inputData+1): # range(inputData) == range(1, inputData+1)
        # print(f"{i}")
        Total += i 
    
    print(f"결과 : {Total}")
    
    # -- 중요 --
    Total2 = sum(list(range(inputData+1))) # list comprehension
    print(f"결과 : {Total2}")
    
# 입력 받은 숫자까지 홀수와 짝수의 합을 출력하는 함수
def plusEvenOdd():
    # inputData = int(input("값 입력 >> "))
    
    # -- Debug --
    inputData = 100
    
    # 내가 푼 풀이
    even_value = 0
    odd_value = 0
    for i in range(inputData+1):
        if i % 2 == 0:
            even_value += i
        else:
            odd_value += i
        
    print(f"홀수의 합 결과 : {odd_value}")
    print(f"짝수의 합 결과 : {even_value}")
    
    # 방법 1
    evenSum = 0 ; oddSum = 0
    for i in range(0, inputData+1, 2):
        evenSum += i
    for i in range(1, inputData+1, 2):
        oddSum += i
        
    print(f"방법 1 - 홀수 합 : {oddSum}, 짝수합 : {evenSum}")
    
    # 방법 2
    evenSum = 0 ; oddSum = 0
    for i in range(inputData+1):
        if i % 2 == 0:
            evenSum += i
        else:
            oddSum += i
    
    print(f"방법 2 - 홀수 합 : {oddSum}, 짝수합 : {evenSum}")
    
    # 방법 3 -- 중요 --
    evenSum = sum(list(range(0, inputData+1, 2)))
    oddSum = sum(list(range(1, inputData+1, 2)))
    print(f"방법 3 - 홀수 합 : {oddSum}, 짝수합 : {evenSum}")
    
if __name__ == '__main__':
    plusFn()
    
    plusHandred()
    
    plusEvenOdd()