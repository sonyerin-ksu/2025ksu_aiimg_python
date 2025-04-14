# 아스키 코드 그림 출력하기
def print_cat():
    cat = [
        " /\\_/\\  ",
        "( o.o ) ",
        " > ^ <  "
    ]
    
    for line in cat:
        print(line)


def print_bear():
    bear = [
        "ʕ•ᴥ•ʔ"
        ]
    for  line in bear:
        print(line)

def print_rabbit():
    rabbit = [
        r'(\(\\' ,
        '( -.-)',
        'o_(")(")'
    ]
    
    for line in rabbit:
        print(line)

# 이 함수를 수정하여 두 개의 프로그램이 될 수 있게 만드시오.
def play_game(n):
    print("그림 출력 프로그램")
    print("=====================")
    print("1. 고양이")
    print("2. 곰돌이")
    print("3. 토끼")
    print("=====================")
    # n = int(input("선택: "))

    # if n == 0:
        # print("프로그램을 종료합니다.")
        # exit()

    # 만약에 1을 입력하면 1번에 해당하는 캐릭터 출력
    if n == 1:
        print("고양이")
        print_cat()
    # 2를 입력하면 2번 캐릭터 출력
    elif n == 2:
        print("곰돌이")
        print_bear()
    # 3을 입력하면 3번 캐릭터 출력
    elif n == 3:
        print("토끼")
        print_rabbit()
    # 잘못 입력하면 잘못 입력했다고 출력
    else:
        print("해당 숫자에 대한 동물이 없습니다")

# 동물 그림 출력 프로그램이 총 5번 반복 실행될 수 있게 만드시오.
# print("5번 출력 프로그램 시작")
# for i in range(5):
   # play_game()

# print("5번 출력 프로그램 종료")

# 위 프로그램을 완성한한 사람은 프로그램이 계속(무한) 반복하게 하고
# 만약에 0을 입력하면 종료되는 프로그램을 만드시오.
print("0을 입력하면 종료 프로그램 시작")
while True: # 무한반복(계속 참)
    # 만약에 0이면 break
    try:
        n_str = input("선택(1-3), 종료(0): ")
        n = int(n_str) # 여기서 ValueError 발생 가능
    except ValueError:
        print("잘못된 입력입니다. 숫자를 입력해주세요.")
        continue # 다시 입력 받기 위해 반복문 처음으로 돌아감

    if n == 0:
        break
    play_game(n) # 문자를 받으면 "잘못 입력" 처리
   

print("0을 입력하면 종료 프로그램 종료")

