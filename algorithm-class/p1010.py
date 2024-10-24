# 10월 10일
# itertools : 파이썬에서 반복되는 데이터를 처리하는 기능을 포함하고 있는 라이브러리
# heapq : 다익스트라 최단 경로 알고리즘을 포함해 다양한 알고리즘에서 우선 순위 큐 기능을 구현할때 사용
# bisect : 이진 탐색을 쉽게 구현할 수 있도록 제공되는 라이브러리
# math : 자주 사용되는 수학적인 기능을 포함하고 있는 라이브러리
# 투포인터 : 리스트에 순차적으로 접근해야 할 때 2개의 점의 위치를 기록하면서 처리하는 알고리즘을 의미

import itertools
# from itertools import permutations, combinations 지정
from itertools import *
import numpy as np
import heapq
import bisect
# from bisect import *


def reviewfn():
    # inmutable 예시
    a = 1
    print(id(a))
    a = 3
    print(id(a))
    # a 변수 두개의 id가 다르다. 
    
    b = a
    print(id(b))
    b = 7
    print(id(b))
    # b=a를 했을때는 id가 같다. b변수의 값을 다시 바꾸면 id가 바뀐다.
    
    l1 = [1, 2, 3]
    print(id(l1))
    l1.append(4)
    print(id(l1)) # 리스트는 id가 바뀌지 않는다.
    
    t1 = (11, 2, 3) # tuple은 append가 되지 않는다.
    print(id(t1))
    t1 = (3, 4, 5)
    print(id(t1)) # 위 두개의 id는 달라진다.
    
def iterFn():
    data1 = ['A', 'B', 'C']
    # com1 = list(combinations(data1, 3)) # 조합
    # per1 = list(permutations(data1, 3)) # 순열 (모든 순열 구하기)
    # print(com1, '\n' ,per1)
    
    com1 = list(combinations(data1, 2)) # 2개로 진행
    per1 = list(permutations(data1, 2)) 
    print(com1, '\n' ,per1)
    
    pro1 = list(list(product(data1, repeat=2)))
    print(pro1)
    
    # a = range(1, 10, 0.1) # 일반적인 실수 증가는 불가하다.
    # print(a)
    
    a = np.arange(1, 2, 0.1) # numpy 모듈 사용
    print(a)

# def heapsort():
#     h = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
#     result = []
#     
#     for val in h:
#         heapq.heappush(h, val)
#     for _ in range(len(h)):
#         result.append(heapq.heappop(h))
#     print(result)

def bisearchFn():
    
    a = [1, 2, 4, 4, 4, 4, 4, 8] # 정렬된 배열을 사용해야한다.
    x = 4
    leftx = bisect.bisect_left(a, x)
    rightx = bisect.bisect_right(a, x)
    # print(bisect_left(a, x)) # 2
    # print(bisect_right(a, x)) # 7
    
    # 원소 개수 확인
    print(rightx - leftx)
    
# from math import *
import math # 코딩 테스트 측면에서는 모든 import하는 것보다 좋을 수 있다.

def mathFn():
    print(math.sin(90)) # 삼각함수 각도는 라디안 (호도법) 처리한다.
    print(math.sin(90*math.pi/180)) 
    print(math.e)
    print(5.2 % 3.1) # C언어에서는 계산되지 않는다.
    print(5.2 % 3.1, 5/3, 5//3)
    print(math.sqrt(4))
    # gcd(a, b) - a와 b의 최대공약수를 반환
    
    data1 = np.arange(15).reshape(3, 5)
    print(data1)
    data2 = data1.T
    print(data2)
    
def is_prime_number():
    x = 4
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            print('소수가 아님')
    print('소수')

# 2부터 1000까지의 모든 소수를 찾는 함수
def eraFn(): 
    n = 1000
    array = [True for i in range(n+1)] # 리스트의 모든 요소를 True로 초기화
    
    # 에라토스테네스의 체 알고리즘
    for i in range(2, int(math.sqrt(n))+ 1):
        if array[i] == True: # 첫번째 값 찾음
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1
    for i in range(2, n+1):
        if array[i]:
            print(i, end=',')
    
import random
def listPlus():            
    l1 = list() ; l2 = []
    for _ in range(3):
        l1.append(random.randint(1, 9))
    for _ in range(5):
        l2.append(random.randint(1, 9))
    
    print(l1, l2)
    
    l3 = ['a', 'b', 'c']
    str1 = "".join(l3)
    print(str1)
    
    #p488 암호 만들기 시험문제 (조합 알고리즘 문제유형)
def passwordFn():
    vowels = ('a', 'e', 'i', 'o', 'u')
    l, c = map(int, input().split(' '))
    
    # 가능한 암호를 사전식으로 출력해야 하므로 입력 이후에 정렬 수행
    array = input().split(' ')
    array.sort()
    
    # 길이가 l인 모든 암호 조합을 확인
    for password in combinations(array, l):
        #패스워드에 포함된 각 문자를 확인하며 모음의 개수를 세기
        count = 0
        for i in password:
            if i in vowels:
                count += 1
        # 최소 1개의 모음과 최소 2개의 자음이 있는 경우 출력
        if count >= 1 and count <= l - 2:
            print(''.join(password))

import requests
def scrollFn():
    target = 'https://google.com'
    res = requests.get(url=target)
    print(res.status_code)
    # bs, selenium, etc...
    
    # 100 : 정보제공 (information)
    # 200 : 정상 (success)
    # 300 : 리다이렉션 (redirection)
    # 400 : 클라이언트 에러 (client error)
    # 500 : 서버 에러 (server error)
    
    
if __name__ == "__main__":
    print("10월 10일")
    
    reviewfn()
    iterFn()
    # heapsort()
    bisearchFn()
    mathFn()
    is_prime_number()
    eraFn()
    #twopointFn()
    listPlus()
    passwordFn()
    scrollFn()