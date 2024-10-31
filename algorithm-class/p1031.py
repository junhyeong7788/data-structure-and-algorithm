
def inoutEx():
    inputData = int(input())
    print(inputData)
    
    total = 0
    for i in range(100):
        total += i
    print(f"합계: {total}")
    
    
    total = 100*(100+1)/2
    print(f"합계: {total}")
    
import sys
def lrupFn():
    n = int(input())
    

    # Debug
    #print(n)
    plans = input().split()
    #print(type(str1), str1)
    
    # lenofplans = len(plans)
    #print(lenofstr1, str1)

    x, y = 1, 1
    move_types = ['L', 'R', 'U', 'D']
    dx = [0, 0, -1, 1] # 위아래
    dy = [-1, 1, 0, 0] # 좌우
    
    # 이동 계획을 하나씩 확인
    for plan in plans:
        for i in range(len(move_types)):
            if plan == move_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]
        # 공간을 벗어나는 경우 무시
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        # 이동수행
        x, y = nx, ny
        
    print(f"좌표 (x, y) : {x, y}")
    
def timecount():
    h = int(input())
    
    count = 0
    for i in range(h+1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i) + str(j) + str(k):
                    count += 1
                    
    print(count)

def threesixnine():
    n = int(input())
    print(f" {n} 까지 369 게임 출력 ")
        
    threesixnine = ['3', '6', '9']

    #for i in range(n):
    #    data = list(str(i)) # strm repr, f-string
    #    
    #    count = 0
    #    for j in threesixnine:
    #        if j in data:
    #            count += data.count(j)
    #    if count == 0:
    #        print(i)
    #    else:
    #        for j in range(count):
    #            print("짝", end="")
    #        print("")
    #        
    #        def threesixnine():

    for i in range(1, n + 1):
        count = sum(1 for digit in str(i) if digit in '369')
        
        if count == 0:
            print(i)
        else:
            print("짝" * count)
    print('--------------------------')
    
def knightmoveFn():
    # 현재 나이트의 위치 입력 받기
    inputdata = input()
    #print(inputdata[0], inputdata[1], type(inputdata))
    row = int(inputdata[1])
    # a~h 까지의 값을 숫자로 바꿔야...
    # a -> 1, b -> 2, c -> 3, ..., h -> 8
    col = int(ord(inputdata[0])) - int(ord('a')) + 1
    print(col)
    
    # 나이트가 이동할 수 있는 8가지 방향 정의
    steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
    
    # 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
    result = 0
    for step in steps:
        # 이동하고자하는 위치 확인
        next_row = row + step[0]
        next_col = col + step[1]
        # 해당 위치로 이동이 가능하다면 카운트 증가
        if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
            result += 1
    print(result)

def moveMap():
    # 데이터 읽고 초기화 하고,,
    n, m = map(int, input().split())
    
    # 2차원 배열 초기화 중요..
    d = [[0]*m for _ in range(n)]
    x, y, direction = map(int, input().split())
    d[x][y] = 1
    
    # 맵 입력
    array = []
    for i in range(n):
        array.append(list(map(int, input().split())))
    
    # 동서남북 방향 정하고
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    
    # 시뮬레이션 시작
    count = 1
    turn_time = 0
    while True:
        
        # 왼쪽으로 회전
        direction = (direction - 1) % 4  # direction이 -1이 되면 3으로 설정
        
        nx = x + dx[direction]
        ny = y + dy[direction]
        
        if d[nx][ny] == 0 and array[nx][ny] == 0:
            d[nx][ny] = 1
            x = nx
            y = ny
            count += 1
            turn_time = 0
            continue
        else:
            turn_time += 1
        
        if turn_time == 4:
            nx = x - dx[direction]
            ny = y - dy[direction]
            
            if array[nx][ny] == 0:
                x = nx
                y = ny
            else:
                break
            turn_time = 0

    # 정답 출력        
    print(count)
        

if __name__ == "__main__":
    print('10월 31일 구현')
    
    inoutEx()
    lrupFn()
    timecount()
    threesixnine()
    knightmoveFn()
    moveMap()