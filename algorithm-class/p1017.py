# 중간고사 : 10월 24일 9교시
# 장소 : 7-613
# 범위 : 부록 1부터 그리디까지
# 요약은 9교시에 해드림
# 윈도우 안에 유리 한 장(조각) : pane

# TODO : 클래스 생성
# FIXME : 고쳐야 되...

class Greedy:
    
    # private : 자기만
    # protected : 상속된 자신만
    # public : 아무나..
    
    def __init__(self) :
        self.data = "클래스 생성 연습"
        
    def readData(self):
        self.data1 = list(map(int, input("Input Data : ").split()))
        print(self.data1)
    
    def remainFn(self):
        # n = int(input("거스름돈 : ").split()[0])
        self.n = 1260
        coinTypes = [500, 100, 50, 10]
        self.count = 0
        
        for coin in coinTypes:
            self.count += self.n // coin
            self.n %= coin
            
        print(self.count)
        
    def plusBigNumber(self):
        n, m, k = 5, 7, 3
        data = [2, 4, 5, 6, 4]
        data.sort()
        length = len(data)
        first = data[length -1]
        second = data[length -2]
        print(first, second)
        
        result = 0
        count = (m // k+1) * k
        count = (m % (k+1)) + count
        result = count * first
        result = (m-count) * second
        print(result)

# 큰수
# 1이 될떄까지 숙제

if __name__ == "__main__":
    print("10월 17일 탐욕 알고리즘")
    classInstance = Greedy() 
    # classInstance.readData()
    # classInstance.remainFn()
    classInstance.plusBigNumber()