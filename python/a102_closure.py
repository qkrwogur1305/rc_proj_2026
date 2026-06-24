#함수 안에서 만든 내부 함수가 

def make_counter():
    count=0

    def counter():
        nonlocal count
        count+=1
        return count
    return counter



def main():
    c=make_counter()
    print(type(c)) # main에 c객체가 남아있다.
    print(c())
    print(c())
    ab=make_counter() # main에 ab객체가 남아있다.
    print(c())
    print(ab())
    print(ab())

if __name__ == "__main__":
    main()