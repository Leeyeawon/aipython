#함수 만들기
#함수 호출 
name = input("이름을 입력: ")
hello_name(name)

#연산을 하는 함수
def cal(r1, r2, op): 
    r = 0
    if op == "+":
        r = r1 + r2
    elif op =="-":
        r = r1 - r2
    else:
        print("잘못된 입력")
    return r

r = cal(2, 1, "+")
print(f"두 수를 더한 값{r}")
r = cal(2, 1, "-")
print(f"두 수를 뺀값{r}")