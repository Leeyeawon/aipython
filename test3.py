def print_cat():
    cat = [ 
        " /\\_/\\ ", 
        "(  o.o  )  ~냥!",
        " >  ^  < "
    ]
    for n in range(5):
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
    for n in range(5):
        for line in dog:
            print(line)

def print_rabbit():
    rabbit = [
        "(\\(\\  ",
        "( -.-)",  
        "o(_(\")\")"
    ]
    for n in range(5):
        for line in rabbit:
            print(line)

for n in range(5):
    print("그림 출력 프로그램")
    print("==================")
    print("1. 고양이")
    print("2. 강아지")
    print("3. 토끼")
    print("==================")
    print("번호를 입력하세요")
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
    elif n == 0:
        print("프로그램을 종료합니다.")
        break

    else:
        print("잘못된 입력")

#for n in range(5):
    #print(i)
    #print (n)



# 동물 그림 출력 프로그램이 총 5번 반복실행될 수 있게 만드시오

#위 프로그램을 완성한 사람은 프로그램이 계속 반복되게 하고
#만약에 0을 입력하면 종료 되는 프로그램을 만드시오

while True:
    print("그림 출력 프로그램")
    print("==================")
    print("1. 고양이")
    print("2. 강아지")
    print("3. 토끼")
    print("0. 종료")
    print("==================")
    n = int(input("번호를 입력하세요: "))

    if n == 1:
        print("고양이 그림")
        print_cat()
    elif n == 2:
        print("강아지 그림")
        print_dog()
    elif n == 3:
        print("토끼 그림")
        print_rabbit()
    elif n == 0:
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 입력")
