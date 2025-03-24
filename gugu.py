# 사용자로부터 입력을 받는 함수
def print_multiplication_table():
    #사용자로부터 단수를 입력받습니다.
    number = int(input("구구단을 출력할 단수를 입력하세요: "))
    
    # 입력받은 단수에 대한 구구단을 출력합니다.
    print(f"{number}단:")
    for i in range(1, 10):
        result = number * i
        print(f"{number} x {i} = {result}")

#프로그램 실행
print_multiplication_table()