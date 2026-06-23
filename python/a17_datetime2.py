import datetime
from a01_hello import main as a01_hello

def main():
    now =datetime.datetime.now()

    if 9<now.hour<12:
        print(f"현재시간은 {now.hour}로 오전입니다.")
    elif now.hour < 9:
        print(f"현재시각은 {now.hour}로 새벽입니다.")
    else:
        print(f"현재시각은 {now.hour}로 오후입니다.")


    if now.month in (1, 2, 3, 12):
        print("현재 계절은 겨울입니다.")
    elif now.month in (4, 5):
        print("현재 계절은 봄입니다.")
    elif now.month in (6, 7, 8):
        print("현재 계절은 여름입니다.")
    else:
        print("현재 계절은 가을입니다.")
    print(now.month, type(now.month))
    #1, 2, 3, 12 겨울
    #4, 5 봄
    #6, 7, 8 여름
    #9, 10, 11 가을



if __name__ == "__main__":
    main()