#과제 테스트용

from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

def print_rabbit():
    rabbit_lines = [
        "(\\(\\",     # 귀
        "( -.-)",     # 얼굴
        'o_(")(")'    # 몸
    ]

    styled_rabbit = Text()
    for line in rabbit_lines:
        styled_rabbit.append(line + "\n", style="bold magenta")

    # 색상 수정: "pink" → "bright_magenta" 또는 "#ff69b4"
    console.print(Panel(styled_rabbit, title="귀염뽀짝 토끼 🐰", border_style="bright_magenta"))

print_rabbit()

from rich.console import Console
from rich.text import Text

console = Console()

def print_rabbit():
    rabbit_lines = [
        "(\\(\\",     # 귀
        "( -.-)",     # 얼굴
        'o_(")(")'    # 몸
    ]

    # 텍스트 스타일 적용
    styled_rabbit = Text()
    for line in rabbit_lines:
        styled_rabbit.append(line + "\n", style="bold magenta")

    # Panel 없이, 그냥 텍스트 출력
    console.print(styled_rabbit)

print_rabbit()

console.print("밝은 노란색", style="bright_yellow")

#이모지 사용

from rich.console import Console
from rich.emoji import Emoji

console = Console()

# 곰돌이와 고양이 이모지 사용
console.print(Emoji.replace("곰돌이 이모지: :bear:"))
console.print(Emoji.replace("고양이 이모지: :cat:"))
console.print(Emoji.replace(":wave:"))

from rich.console import Console

console = Console()

def print_text_with_background():
    # 텍스트 색상: white, 배경색: sky_blue1
    console.print("하늘색 배경에 흰색 텍스트!", style="white on sky_blue1")

print_text_with_background()

from rich.console import Console

console = Console()

def print_italic_gray_text():
    # 회색 텍스트에 기울임꼴 적용
    console.print("기울어진 회색 텍스트!", style="italic #D3D3D3")

print_italic_gray_text()


