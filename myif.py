# 아스키 코드출력 하기
def print_cat():
    cat = [ 
        " /\\_/\\ ", 
        "(  o.o  )  ~냥!",
        " >  ^  < "
    ]
    for line in cat:
        print(line)

def print_dog():
    dog = [ 
        "/ \\__",
        "(    @\\____",
        "/         O",
        "/   (_____/",
        "/_____/   U"
    ]
    for line in dog:
        print(line)

def print_rabbit():  # 함수명 수정
    rabbit = [  # 변수명 수정
        "(\\(\\  ",
        "( -.-)",  
        "o(_(\")\")"
    ]
    for line in rabbit:
        print(line)

print("그림 출력 프로그램")
print("==================")
print("1. 고양이")
print("2. 강아지")
print("3. 토끼")
print("==================")
n = int(input("선택: "))

if n == 1:
    print("고양이 그림")
    print_cat()
elif n == 2:
    print("강아지 그림")
    print_dog()
elif n == 3:
    print("토끼 그림")
    print_rabbit()
else:
    print("잘못된 입력")
