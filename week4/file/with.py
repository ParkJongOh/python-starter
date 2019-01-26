# with 구문은
# with 오픈함수 as 변수명
# 변수 = 함수
# with 함수 as 변수
# with을 사용하면 close처리를 해줄필요가 없다.

with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")