# 특정 개수의 정수를 n줄 입력받아 리스트 저장
import sys
input = sys.stdin.readline

n = int(input()) # 받을 문자의 개수 : n
data = [] 

for _ in range(n): 
	line = input().strip() # 한 줄을 입력받아 줄 바꿈 문자 제거
	data.append(line)

print(data)