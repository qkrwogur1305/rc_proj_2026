name = input("상품명을 입력하세요: ")
str(name)


price = input("상품가격을 입력하세요: ")
if type(price) != int:
    print("가격은 정수형이어야합니다.")
    price = input("상품가격을 입력하세요: ")


discount = input("할인율을 입력하세요: ")
if type(discount) != int:
    print("할인율은 정수형이어야합니다.")
    discount = input("할인율을 입력하세요: ")
