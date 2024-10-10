
# 9월 26일

# 문자열 연습
def strFn():
    print("test"*3)
    print([0]*5)
    print(["test"])
    print(list("test"))
    
    # 문자열은 리스트 처리한다.
    str1 = "iloveyou"
    print(str1[2:5])
    
    # str1 
    print(id(str1))
    
# 딕셔너리 연습 (json : java script object notation)
def dictEx():
    dict1 = {"사과" : "Apple", "바나나" : "Banana", "코코넛" : "Coconut"}
    print(dict1)
    
    for i in dict1:
        print(i)
    
    print(dict1.keys())
    print(dict1.values())
    print(dict1.items())
    
    # 중요 !!
    for i in dict1.values():
        print(i)
    
    for i in dict1.items():
        print(i)
    
    for i in dict1.keys():
        print(i,":", dict1[i])
    
    # 딕셔너리는 값을 변경할 수 있다.
    dict1["사과"] = "미안"
    print(dict1)
    
    # mutable과 immutable의 기본적인 개념
    # immutable : 메모리 안에 담겨 있는 값이 언제나 변하지 않는 객체
    # mutable : 메모리 안에 담겨 있는 값이 변할수 있는 객체
    a = 3
    print(a, id(a))
    a = 5
    print(a, id(a))
    b = a
    print(id(a), id(b))
    b = 100
    print(id(a), id(b))
    
    # 리스트 주소는 바뀌지 않고, 리스트 값은 바뀐다.
    l1 = [1,2,3]
    print(l1, id(l1))
    l1[2] = 100
    print(l1, id(l1))
    
    
    # 파이썬에서 문자열 = 리스트가 아니다.
        # list, dict 등은 변경 가능(mutable)하며,
        # int, float, string, tuple 등은 변경 불가능(immutable)하다.

    # 문자열 찾아 바꾸기
    str1 = 'test'
    #str2 = list(str1)
    #str2[0] = 'a'
    #str1 = ''.join(str2)
    #print(str1)
    
    # str1[0] = 'a' # Error
    #str3 = str1.replace("t", "a", 1) # t를 하나만 대체
    #print(str3)
    
    str3 = str1.replace("t", "a", 2) # t를 두개 대체
    print(str1, str3)
    
def ifEx():
    a = 100
    
    if a > 10:
        print('크다')
    else:
        print('작다')

def listRemove():
    a = list(range(1,6))
    for _ in range(3):
        a.append(5)
    print(a)
    
    # !!!! important
    removeSet = {3, 5}
    result = [i for i in a if i not in removeSet]
    print(result)

    # Python에서 부등식 사용 여부 확인
    a = 150
    if 0 < a < 20 :
        print("Success")
    else:
        print("Failure")

# 임의의 숫자까지 홀수 짝수의 합
def EvenOddSum(TestString): # TestString : Parameter (매개변수)
    # InputData = int((input("값 입력 >> "))
    
    # --Debug--
    InputData = 10
    
    EvenSum = sum(range(0, InputData+1, 2))
    OddSum = sum(range(1, InputData+1, 2))
    print(OddSum, EvenSum)
    
    EvenSum = 0; OddSum = 0
    for i in range(InputData+1):
        if i % 2 == 0:
            EvenSum += i
        else :
            OddSum += i
    print(OddSum, EvenSum)

    # DataList = list(range(InputData))
    
    DataList = [1,1,1,1,2,2,2,2]
    # [1,2,4,6,1,2,5,7,9]
    # 홀수합 : 23 , 짝수합 : 14
    # 리스트 함축으로 홀수짝수 합을 구하자.
    
        # 내가 짠 코드
    OddSum = 0
    EvenSum = 0
    for i in DataList:
        if i % 2 == 0:
            EvenSum += i
        else : 
            OddSum += i
    print("1 : ", OddSum, EvenSum)
    
        # 교수님이 짠 코드, C언어 스타일
    OddSum = 0
    EvenSum = 0
    for i in range(len(DataList)): 
        if DataList[i] % 2 == 0:
            EvenSum += DataList[i]
        else : 
            OddSum += DataList[i]
    print("2 : ", OddSum, EvenSum)
        # list comprehension
    EvenSum = sum([i for i in DataList if i % 2 == 0])
    OddSum = sum([i for i in DataList if i % 2 == 1])
    print("3 : ", OddSum, EvenSum)
    
def testFn(aa, bb, *args, **kwargs): # keyword argument : **kwargs
    print("test")
    print(aa, bb)
    print(args, type(args))
    #print(kwargs, type(kwargs)) # 주석 처리하면 앞 args만 받는다.

    # Python 접근 제어자
        #  pubilc
        # _ : protected
        # __ : privated
    
    # 입출력
        # map() , list() , split()
        # p445 참고 - 입력을 위한 전형적이 소스코드
        # 공백을 기준으로 구분하여 적은 수의 데이터 입력
        

import sys

def datareadFn():
    #data = sys.stdin.readline().rstrip() # readline : 한줄씩, readlines : 여러줄
    #print(data)
    
    #data1 = list(sys.stdin.readline().rstrip().split())
    #print(data1)
    
    # read(), readlines(), open ~ close(), with open()
    # data1 = list(map(int, sys.stdin.readlines().rstrip().split()))
    # print(data1)
    
    # --Debug--
    result = eval("3 + 4") # "3 + 4a" 는 불가능
    print(result)
    
    # p451 - eval() 함수 : 수학 수식이 문자열 형식으로 들어오면 해당 수식을 계산한 결과를 반환
    
if __name__ == "__main__":
    print('9월 26일')
    
    strFn()
    dictEx()
    ifEx()
    listRemove()
    EvenOddSum("test") # 념겨주는 값 : argument(실인자, 실인수)
    testFn(1, 2, 3, 4, 5, a=1, b=2, c=3) # args와 kwargs의 순서는 정해져 있다.
    datareadFn()