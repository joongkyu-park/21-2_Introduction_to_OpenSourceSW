#과제 2번_12150981

class Menu:

    def __init__(self):
        self.orderList = dict()
        self.total = 0

    def addMenu(self, f):
        fp = open(f, "r")
        while True:
            line = fp.readline()
            if not line: break

            arr = line.split(sep=", ")
            self.orderList[int(arr[0])] = [arr[1],int(arr[2]),int(arr[3])]

        fp.close()

    def printMenu(self):
        print()
        print("="*40)
        keys = list(self.orderList.keys())
        keys.sort()
        for k in keys:
            print(k,".",self.orderList[k][0],
                  " "*(10-len(self.orderList[k][0])),
                  "금액 : ",self.orderList[k][1],"원",
                  " "*(10-len(str(self.orderList[k][1]))),
                  "재고 : ", self.orderList[k][2],
                  sep="")
        print("end를 입력하시면 주문서로 돌아갑니다")
        print("=" * 40)
        print()

class Order(Menu):

    def __init__(self,):
        super().__init__()
        self.orderResult = []

    def orderMenu(self, menuNum):
        self.printMenu()
        if self.orderResult != []:
            pass
        else:
            self.orderResult = list(0 for i in range(0,len(self.orderList)+1))

        if menuNum == "end":
            quantitySum = 0
            for i in range(1, len(self.orderList)+1):
                quantitySum += self.orderResult[i]
            costSum = 0
            for i in range(1, len(self.orderList)+1):
                costSum += self.orderResult[i]*self.orderList[i][1]
                self.total += self.orderResult[i]*self.orderList[i][1]

            print("주문내역")
            print("총 주문 수량 : %d개, 총 주문 금액 : %d원" % (quantitySum, costSum))
            print()
            self.orderResult.clear()

            return 0

        else:
            while True:
                print("선택한 메뉴의 수량을 입력해주세요")
                orderQuantity = int(input("input : "))

                if self.orderList[menuNum][2] == 0:
                    print("품절되었습니다. 다른 메뉴를 선택해해주세요")

                    return 1

                elif self.orderList[menuNum][2] < orderQuantity:
                    print("수량이 부족합니다.")
                    self.printMenu()

                else:
                    self.orderResult[menuNum] = self.orderResult[menuNum] + orderQuantity
                    self.orderList[menuNum][2] = self.orderList[menuNum][2] - orderQuantity

                    return 0

class Manage(Order):

    def __init__(self):
        super().__init__()
        self.ManageResult = []

    def Management(self, menuNum):
        self.printMenu()
        if self.ManageResult != []:
            pass
        else:
            self.ManageResult = list(0 for i in range(0,len(self.orderList)+1))

        if menuNum == "end":
            quantitySum = 0
            for i in range(1, len(self.orderList)+1):
                quantitySum += self.ManageResult[i]
            costSum = 0
            for i in range(1, len(self.orderList)+1):
                costSum += self.ManageResult[i] * self.orderList[i][1]

            print("주문내역")
            print("총 주문 수량 : %d개, 총 주문 금액 : %d원" % (quantitySum, costSum))
            print()

            self.ManageResult.clear()

        else:
            print("선택한 메뉴의 수량을 입력해주세요")
            orderQuantity = int(input("input : "))

            self.ManageResult[menuNum] = self.ManageResult[menuNum] + orderQuantity
            self.orderList[menuNum][2] = self.orderList[menuNum][2] + orderQuantity


    def totSale(self):
        print("총 매출 %d원입니다"%(self.total))
        print()

m = Manage()
m.addMenu("cafe.txt")

ordernum = -1
while True:
    print("=" * 20)
    print(" "*7,"주문서"," "*7)
    print("=" * 20)
    print("1. 커피 주문하기")
    print("2. 커피 매출 확인")
    print("3. 커피 입고 하기")
    print("4. 종료하기")
    print("=" * 20)
    print()
    print("원하시는 주문 번호를 입력해주세요")
    orderNum = int(input("input : "))
    print()

    if orderNum == 1:
        print("주문할 메뉴 번호를 입력해주세요")

        while True:
            menuNum = input("input : ")

            if menuNum == 'end':
                m.orderMenu(menuNum)
                break
            elif int(menuNum) in list(m.orderList.keys()):
                if m.orderMenu(int(menuNum)) == 1:
                    print()
                    print("메뉴 번호를 다시 입력해주세요")

                else:
                    print()
                    print("추가로 주문할 메뉴 번호를 입력해주세요")
            else:
                print("존재하지 않는 메뉴입니다")

    elif orderNum == 2:
        m.totSale()

    elif orderNum == 3:
        print("입고할 메뉴 번호를 입력해주세요")
        while True:
            menuNum = input("input : ")

            if menuNum == "end":
                m.Management(menuNum)
                break
            elif int(menuNum) in list(m.orderList.keys()):
                m.Management(int(menuNum))
                print("추가로 입고할 메뉴 번호를 입력해주세요")
            else:
                print("존재하지 않는 메뉴입니다")

    elif orderNum == 4:
        break

    else:
        print("올바른 주문 번호를 입력해주세요")
