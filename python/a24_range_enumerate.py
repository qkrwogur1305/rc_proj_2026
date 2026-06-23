def main():
    print(range(10))  # 0~9까지 들어있음
    print(range(0, 10, 1))   #0~9까지 1씩 증가
    a= range(10)
    print(list(a))
    print(list(range(5, 10, 1)))
    a=[]
    for i in range(100):
        a.append(i+1)
    print(a)

    a=[i+1 for i in range(100)]
    print(a)

    list_b=["a", "b", "c", "d", "e", "f", "g"]
    a=0
    for a, ele in enumerate(list_b):
        print(ele+"원소",a)


    list_c=["에이", "비", "씨", "디", "이", "에프", "지"]
    for i in range(7):
        print(list_b[i], list_c[i])
        
    for b, c in zip(list_b, list_c):  #pythonic, pydantic
        print(b, c)

    




if __name__ == "__main__":
    main()