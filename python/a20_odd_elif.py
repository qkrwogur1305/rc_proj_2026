def main():
    number= int(input("정수를 입력하세요>"))

    # if number % 2 == 0:
    #     print(f"{number}는 짝수입니다.")
    # elif number % 2 == 1:
    #     print(f"{number}는 홀수입니다.")
    print("홀수" if number % 2 else "짝수", "입니다.")


if __name__ == "__main__":
    main()