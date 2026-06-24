def rec_fac(n):
    #추천하지않음 -> for문으로 돌려도 되는걸 굳이 재귀함수 안해도 된다
    if n == 1:
        return 1
    else:
        return n * rec_fac(n-1)
    
def for_fac(n):
    output = 1
    for i in range(n):
        output *= i+1
    return output


cnt=0
def fibonacci(n):
    global cnt
    cnt += 1
    if n ==1:
        return 1
    elif n ==2:
        return 1
    else:
        return fibonacci(n-1)+ fibonacci(n-2)
    
def main():
    print(rec_fac(100))
    print(for_fac(100))
    print(fibonacci(40))
    print(f"피보나치 함수가 실행된 횟수: {cnt}")

if __name__ == "__main__":
    main()