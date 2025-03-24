
# 사용자에게 숫자를 입력받습니다.
num = int(input("출력할 구구단 단 수를 입력하세요: "))

# 구구단 출력
if 2 <= num <= 9:
    for i in range(1, 10):
        print(f"{num} × {i} = {num * i}")
else:
    print("2~9 사이의 숫자를 입력하세요.")
