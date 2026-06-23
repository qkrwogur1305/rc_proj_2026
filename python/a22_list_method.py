class Mylist:
    def __init__(self):
        self.myVariable = "park" #인스턴스 변수
        self.myVariable2 = "jae" #인스턴스 변수
        self.myList=list()

    def append(self, ele):
        self.myList.append(ele) 

def main():
    list_a =[1, 2, 3]
    list_b =[4, 5, 6]

    print(list_a + list_b)
    print(list_a)
    list_a.extend(list_b)
    print(list_a)

    list_b.append(7)
    list_b.append(8)
    print(list_b)
    list_b.insert(1, 4.5)
    print(list_b)
    mylist_a = Mylist()
    mylist_a.append(1)
    print(myList_a.myVariable, )


if __name__ == "__main__":
    main()