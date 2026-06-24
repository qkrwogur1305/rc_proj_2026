def print_hello(a : int):
    for i in range(a):
        print("안녕하세요!", i)
    return "excution OK!"

def main():
    re=print_hello(3)  #positional argument follows keyword argument
    print(re)


if __name__ == "__main__":
    main()
