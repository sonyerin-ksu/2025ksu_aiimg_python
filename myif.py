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
        "  (\\_/)",
        "  (o o)",
        "  ( > )"
    ]
    
    for line in rabbit:
        print(line)

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
    print("잘못입력")