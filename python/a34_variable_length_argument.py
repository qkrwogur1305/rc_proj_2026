import random

def sum_all(a, b, c, *value): #positional 다음에 가변인자를 넣어야됨
    sum=0
    for i in value:
        sum+=i
        avr=sum/len(value)
        return sum, avr
    


def main():
    list_a=[random.randint(1, 100) for i in range(100)]
    s, a =sum_all(*list_a)
    print(f"합계는 {s}, 평균은 {a}입니다.")
    s, a =sum_all(100, 200, 300, 400, 2345)
    print(f"합계는 {s}, 평균은 {a}입니다.")


if __name__ == "__main__":
    main()