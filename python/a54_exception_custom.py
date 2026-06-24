import math

class MinusError(Exception):
    def __init__(self):
        # 부모 클래스(Exception)의 생성자에 메시지를 바로 전달합니다.
        super().__init__("음수는 허용되지않습니다.")

def main():
    user_input = input("양의 정수 입력: ")
    try:
        number_input = int(user_input)
        if number_input < 0:
            raise MinusError  # 여기서 에러가 정상적으로 발생합니다.
    except MinusError as e:
        print(e)  # 이제 "음수는 허용되지않습니다."가 정상 출력됩니다!
    except ValueError as e:
        print(e)
    else:
        print(f"원의 반지름: {number_input}")
        print(f"원의 둘레: {number_input * 2 * math.pi}")
        print(f"원의 넓이: {math.pi * number_input**2}")
    finally:
        print("--프로그램이 종료되었습니다.--")

if __name__ == "__main__":
    main()