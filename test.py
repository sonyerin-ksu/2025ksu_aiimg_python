#number = int(input("구구단을 출력할 단수를 입력하세요: "))
s_number = input("구구단을 출력할 단수를 입력하세요: ")
print(f"{s_number}단:")
#print(number, "단:")
#print(number + "단:")
#print(number + "단," + number + "단, " + number + "단")
#print(f"{number}단,{number}단,{number}단")
#s_number 값이 문자열이기 때문에 숫자로 변경해서 연산
number = int(s_number)
result = number * 2
print(result)