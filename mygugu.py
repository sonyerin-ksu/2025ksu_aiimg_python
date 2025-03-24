# 숫자 두 를 입력을 받아서
# +, -, *, / 를 출력하는 프로그램을 만들어 보자

# 사용자로부터 숫자 입력 받기
num1 = int(input("첫 번째 숫자를 입력하세요: "))
num2 = int(input("두 번째 숫자를 입력하세요: "))

# 나눗셈은 0으로 나누는 경우를 처리
if num2 != 0:
    division = num1 / num2
else:
    division = "0으로 나눌 수 없습니다."

# 결과 출력
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {division}")