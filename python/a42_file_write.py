from pathlib import Path


def main():
    # print(Path(__file__).parent)
    # f=open(Path(__file__).parent.parent / "data" / "text.txt", "w") #a는 add모드로 실행할때마다 같은 내용이 더해져서 추가됨, w는 계속 실행해도 같은 결과만나옴
    # f.write("안녕하세요\n")
    # f.close() 
    url= Path(__file__).parent.parent/ "data"/ "text.txt"
    bin_url = Path(__file__).parent.parent/ "data"/ "text.txt"
    with open(url, "r", encoding="utf_8") as f:
        data=f.read()
        print(data)
        f.seek(0)
        while data := f.readline():
            print(data)
        f.seek(0)
        data = f.readlines()
        print(data)
        binary_data=b'\1\2\3'
        with open(bin_url, "wb") as f:
            f.write(binary_data)
        with open(bin_url, "rb") as f:
            data=f.read()
            print(data)



if __name__ == "__main__":
    main()