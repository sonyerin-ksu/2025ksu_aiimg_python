from rich.console import Console
# 텍스트 꾸미기
from rich.text import Text
# 이모티콘 적용
from rich.emoji import Emoji
# 판넬
from rich.panel import Panel
# 로딩 애니메이션
from rich.progress import track
import time


for step in track(range(10), description="준비 중..."):
    time.sleep(0.3)

console = Console()


# 아스키 코드 그림 출력하기
def print_cat():
    cat = [
        " /\\_/\\  ",
        "( o.o ) ",
        " > ^ <  "
    ]
    
    styled_cat = Text()
    for  line in cat:
        styled_cat.append(line + "\n", style="sky_blue1")

    console.print(styled_cat)


def print_bear():
    bear = [
        "ʕ•ᴥ•ʔ"
        ]

    styled_bear = Text()
    for  line in bear:
        styled_bear.append(line + "\n", style="yellow")

    console.print(styled_bear)

def print_rabbit():
    rabbit = [
        '(\\(\\' ,
        '( -.-)',
        'o_(")(")'
    ]
    
    # 텍스트 스타일 적용
    styled_rabbit = Text()
    for line in rabbit:
        styled_rabbit.append(line + "\n", style="bold #ff69b4")

    console.print(styled_rabbit)

    # for line in rabbit:
        # print(line)

def print_sheep():
    sheep = [
        """
        .　,〜⌒⌒､⌒ヽ
        (⊂,~〜､⊃）） ) )
        ((ξ･ﻌ ･๑Ҙ)　)　）
        (　~　ノ(　ﾉ ﾉ
        　ヽ〜 〜 ノノ
        　　UU￣UU"""
        ]

    styled_sheep = Text()
    for  line in sheep:
        styled_sheep.append(line + "\n", style="#B464eb")

    console.print(styled_sheep)

# 이 함수를 수정하여 두 개의 프로그램이 될 수 있게 만드시오.

def play_game(n):
    print("그림 출력 프로그램")
    print("=====================")
    console.print(Emoji.replace("[bold sky_blue1]1. 고양이:cat:[/bold sky_blue1]"))
    console.print(Emoji.replace("[bold yellow]2. 곰돌이:bear:[/bold yellow]"))
    console.print(Emoji.replace("[bold #ff69b4]3. 토끼:rabbit:[/bold #ff69b4]"))
    console.print(Emoji.replace("[bold #B464eb]4. 양:sheep:[/bold #B464eb]"))
    print("=====================")
    # n = int(input("선택: "))

    # if n == 0:
        # print("프로그램을 종료합니다.")
        # exit()

    # 만약에 1을 입력하면 1번에 해당하는 캐릭터 출력
    if n == 1:
        console.print(Emoji.replace("[bold sky_blue1]고양이:cat:[/bold sky_blue1]"))
        print_cat()
    # 2를 입력하면 2번 캐릭터 출력
    elif n == 2:
        console.print(Emoji.replace("[bold yellow]곰돌이:bear:[/bold yellow]"))
        print_bear()
    # 3을 입력하면 3번 캐릭터 출력
    elif n == 3:
        console.print(Emoji.replace("[bold #ff69b4]토끼:rabbit:[/bold #ff69b4]"))
        print_rabbit()
    # 4를 입력하면 4번 캐릭터 출력
    elif n == 4:
        console.print(Emoji.replace("[bold #B464eb]양:sheep:[/bold #B464eb]"))
        print_sheep()
    # 잘못 입력하면 잘못 입력했다고 출력
    else:
        console.print("[italic #D3D3D3]*해당 숫자에 대한 동물이 없습니다[/italic #D3D3D3]")

# 동물 그림 출력 프로그램이 총 5번 반복 실행될 수 있게 만드시오.
# print("5번 출력 프로그램 시작")
# for i in range(5):
   # play_game()

# print("5번 출력 프로그램 종료")

# 위 프로그램을 완성한한 사람은 프로그램이 계속(무한) 반복하게 하고
# 만약에 0을 입력하면 종료되는 프로그램을 만드시오.
console.print(Panel("0을 입력하면 종료 프로그램 시작"))
while True: # 무한반복(계속 참)
    # 만약에 0이면 break
    try:
        n_str = input("선택(1-4), 종료(0): ")
        n = int(n_str) # 여기서 ValueError 발생 가능
    except ValueError:
        console.print("[underline red]잘못된 입력입니다. 숫자를 입력해주세요.[/underline red]")
        continue # 다시 입력 받기 위해 반복문 처음으로 돌아감

    if n == 0:
        break
    play_game(n) # 문자를 받으면 "잘못 입력" 처리
   

console.print(Panel(Emoji.replace("0을 입력하면 종료 프로그램 종료:wave:")))

