
# 9월 19일
#%%
import math
from math import inf

# vscode에서 특정 단위를 셀단위(jupyter notebook)로 실행하고자 할때, '#In[1]', '#In[]', '#%%', 'shift + enter' 를 사용하면 된다.
#%%
def datatypeFn():
    print('def datatype')
    
    iData = 3
    fData = 3.14
    cData = 3 + 4j

    print(f'iData type : {type(iData)}') # 모든 데이터 타입을 클래스 인스턴스로 처리한다.
    print(f'fData type : {type(fData)}')
    print(f'cData type : {type(cData)}')
    print("Python은 모든 데이터 타입을 개체 처리합니다.")
    
    data1 = range(5)
    print(f'{type(data1)}')
    data2 = '문자열'
    print(f"{type(data2)}")
    data3 = [1, 2, 3]
    print(f'{type(data3)}')
    data4 = (1, 2 ,3)
    print(f'{type(data4)}')
    data5 = {1, 2, 1, 2}
    print(f'{type(data5)}')
    data6 = {'a':'apple', 'b':'banana', 'c':'cherry'}
    print(f'{type(data6)}')
    data7 = True
    print(f'{type(data7)}')
#%%
def opFn():
    print(5/3) # 파이썬에서는 실수 계산해서 나온다, (C언어에서는 정수가 나온다)
    print(5//3)
    print(5%3)
    print(5%3.0)
    print(5.2%3.0)
    print(5**3) # 산술연산자
#%%   
def maxFn():
    print('\n','def maxFn')
    
    a = 3; b = 5
    if a > b :
        max = a
    else : 
        max = b
    print(f'큰 값 : {max}')
    
    # python one-line coding (삼항연산자, 리스트 함축)
    a = 5; b = 7
    max = a if a > b else b
    print(f'큰 값 : {max}')
    
#%%
def bitFn():
    print('\n','def bitFn')
    
    a = 12
    b = 7
    
    print(bin(a)); print(bin(b))
    print(f'{a&b}')
    print(f'{a|b}')
    print(f'{a^b}')
    print(f'{~a}')
    print(f'{~b}')
    
    a = 0b01010101
    b = 0o123
    print(bin(a))
    
    # 지수 표현방식 가능, 소문자 대문자 구별 안함
    print(f'{3e3}, {3.14E5}') 
    
    # 무한 숫자
    c = math.inf
    print(c)
    d = inf
    print(d)
    
    # NaN : Not a Number - 표현되지 않는 부동 소수점
    # None은 객체(데이터)가 없는것 - python에서 존재하지 않음을 의미한다.
    # NaN과 None은 다른 것이다.
    
    print(0.3 + 0.6) # 계산을 못한다. = 정확한 계산값이 안나온다.
    # 0.3 * 2 = '0.6, 1.2, 0.4, 0.8, 1.6', 1.2,  -> 0.0'1001' / ''안에 있는 값이 순환(무한루프)
    # 0.6 -> 0.'1001'
#%%
def listEx():
    print('\n','def listEx')
    
    # 빈리스트 만들기
    a = list()
    b = []
    
    a1 = [1,2,3,4,5,6,7,8,9]
    a2 = list(range(1, 10)) # 실수 : numpy.arange()
    a3 = [i for i in range(1, 10)]
    print(a1, a2, a3)
    
    a4 = [0] * 10
    a5 = [0 for _ in range(10)]
    print(a4, a5)
    
    a6 = [1,2,3,4]
    # 슬라이스, 제일 마지막 인덱스 바로 앞까지 [1,2,3] / 슬라이싱
    a7 = a6[:-1] 
    # 역순으로 출력 [4,3,2,1] / 역순
    a8 = a6[::-1] 
    print(a7, a8)
    
#%%
def listCom():
    print('\n','def listCom')
    
    a1 = [i for i in range(10)]
    print(a1)
    
    a2 = [i**2 for i in range(10)]
    print(a2)
    
    
    event_a = ['아반떼', '투싼', '넥쏘']
    event_b = ['흰색', '실버', '검정']
    a3 = [[x,y] for x in event_a for y in event_b]
    print(a3)
    a4 = [len(i) for i in event_a]
    print(a4)
    a5 = [i[0] for i in event_a]
    print(a5)
    
    a6 = [i for i in range(10) if i%2 != 0]
    print(a6)
    a7 = [i if i % 2 != 0 else '짝수' for i in range(10)]
    print(a7)

#%%
# 2차원 리스트 초기화(매우 중요!!) / error 확인
def twolist():
    print('\n','def twolist')
    
    r = 3; c = 4
    
    # *** Error
    l1 = [[0]*c] * r
    print(l1)
    
    l1[2][2] = 5 # l1의 [0][2]와 [1][2]에는 5가 들어가면 안되는데 들어간다.
    print(l1)
    
    l2 = [[0]*c for _ in range(r)]
    print(l2)
    l2[2][2] = 5
    print(l2)
    l2[1][2] = 7
    print(l2)
    
    l3_1 = [0,0,0,0] * 3 # 1차원 배열
    print(l3_1)
    l3_2 = [[0,0,0,0]] * 3
    print(l3_2)
    l3_2[2][2] = 5
    print(l3_2)
    
    l4 = [[0,0,0,0], [0,0,0,0], [0,0,0,0]]
    print(l4)
    l4[2][2] = 5
    print(l4)
    
    n = 3; m = 4
    l5 = [[0] * m for _ in range(n)]
    print(l5)
    l5[2][2] = 7
    print(l5)
    
#%%
def softlist():
    print('\n','def softlist')
    
    l1 = [1, 5, 9, 2, 7]
    l2 = l1.sort() # 리스트의 멤버 함수, l1자체를 정렬해라. 반환값은 없다.
    print(l2) # l2에서는 값이 들어가지 않고, None
    
    l1 = [1, 5, 9, 2, 7]
    l3 = sorted(l1) # 내장 함수, l1을 정렬해서 그 정렬된 리스트를 반환해라
    print(l3)
    
    # copy() 얕은 복사 vs deepcopy() 깊은 복사 / # sort() vs sorted()
    # list는 메모리 참조를 한다.
    a = [1,2,3]
    b = a
    b[2] = 100  # deep copy 라면 a = [1 1000 3], b = [1 2, 100]
    a[1] = 1000 # swallow copy a = b = [1, 100, 100]
    print(a, b)
    
    del a, b # 지정된 변수값 클리어 = del
    a = 3
    b = a
    a = 1000
    print(a, b)
    
    # !!!
    a = [1,2,3,4,5,5,5]
    remove_set = {3,5}
    result = [i for i in a if i not in remove_set]
    print(f'result : {result}')
    
    result.remove(1)
    print(result)
    
    # 항상 지우기 전에는 있는지 없는지 체크해라.
    # 없는 값 지우면 에러 발생.. 
    # [파이썬 리스트 특정 요소 제거](https://www.freecodecamp.org/korean/news/paisseon-list-remove-paisseon-baeyeoleseo-hangmogeul-jegeohaneun-bangbeob/)
    remove_value = 100
    if remove_value in result:
        result.remove(remove_value)
    else:
        pass
    print(result)
    
    try:
        result.remove(remove_value)
    except Exception as e :
        print(f'에러 메시지 : {e}')
    
#%%
if __name__ == "__main__":
    print("9월 19일")

    datatypeFn()
    opFn()
    maxFn()
    bitFn()
    listEx()
    listCom()
    twolist()
    softlist()

# %%
