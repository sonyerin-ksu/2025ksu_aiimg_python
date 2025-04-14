# 텍스트에 색, 스타일 넣기
from rich import print

print("[bold magenta]안녕하세요[/bold magenta] [underline green]Rich[/underline green]입니다!")

# 로깅에 사용
from rich.logging import RichHandler
import logging

logging.basicConfig(
    level=logging.DEBUG,
    handlers=[RichHandler()],
)
logger = logging.getLogger("rich")

logger.info("이건 정보 로그입니다.")

# 표 만들기
from rich.table import Table
from rich.console import Console

console = Console()

table = Table(title="학생 성적표")

table.add_column("이름", style="cyan", no_wrap=True)
table.add_column("수학", justify="right", style="green")
table.add_column("영어", justify="right", style="magenta")

table.add_row("홍길동", "95", "88")
table.add_row("김철수", "78", "92")

console.print(table)

# 코드 하이라이팅
from rich.console import Console
from rich.syntax import Syntax

code = """
def hello():
    print("Hello, World!")
"""

syntax = Syntax(code, "python", theme="monokai", line_numbers=True)
Console().print(syntax)

# 스피너(로딩 애니메이션)
from rich.console import Console
from rich.progress import track
import time

for step in track(range(10), description="처리 중..."):
    time.sleep(0.3)

#이모지 사용
from rich.console import Console
from rich.emoji import Emoji

console = Console()

# 곰돌이와 고양이 이모지 사용
console.print(Emoji.replace("곰돌이 이모지: :bear:"))
console.print(Emoji.replace("고양이 이모지: :cat:"))

