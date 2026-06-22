import keyword

class A_test:
    def __repr__(self):
        return "A_test 객체이다."

def main():
    print(2345)
    print(123, "park", "jae", "hyeok")
    print(3.1432)
    a = A_test()
    print(a)

    print("this", "is", "python", "class!!", sep="_", end="")

if __name__ == "__main__":
    main()