# num = int(input("출력할 구구단 단 수를 입력하세요: "))
# int = 정수 값만 받아드림
# input은 모든 것을 문자로 처리함
s_num = input("출력할 구구단 단 수를 입력하세요: ")
print(f"(num)단:")
# print(num, "단:")
# print(num + "단:")
# print(num + "단, " + num + "단," + num + "단,")
# print(f"(num)단, (num)단, (num)단")
# num 값이 문자열이기 문에 숫자로 변경해서 연산
num = int(s_num)
result = num * 2
print(result)

# 들여쓰기를 하면 앞에 코드에 포함됨
# tap = 들여쓰기
# shift + tap = 들여쓰기 지우기