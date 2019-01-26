#모듈을 불러올때는 import라는 명령어를 사용해서 불러온다
#모듈명을 입력할때는 .py 확장자는 제외한다
#함수명을 입력할때 모듈명을 입력하고싶지않아
#입력하고싶지 않으면 from 모듈명 import 함수명
#다른사람이 만든 모듈을 쓰고싶으면 pip를 사용 할 수 있다
#pip는 python install package의 약자로 프로젝트목록은 https://pypi.org/project/pip/ 에서 확인 할 수 있다
#설치 할 때는 pip install 모듈명
#지울때는 pip uninstall 모듈명

from calc import add

result = add(1,3)
print(result)