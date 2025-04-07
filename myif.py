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
        '(\(\\' ,
        '( -.-)',
        'o_(")(")'
    ]
    
    for line in rabbit:
        print(line)

def play_game():
    print("그림 출력 프로그램")
    print("=====================")
    print("1. 고양이")
    print("2. 곰돌이")
    print("3. 토끼")
    print("=====================")
    n = int(input("선택: "))
   
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
for i in range(5):
   play_game()

# 위 프로그램을 완성한한 사람은 프로그램이 계속(무한) 반복하게 하고
# 만약에 0을 입력하면 종료되는 프로그램을 만드시오.
while True: # 무한반복(계속 참)
   play_game()



