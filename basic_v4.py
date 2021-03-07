# 함수정의
def student(student_name):
    print(student_name)
student('edward')
# 매개 변수가 여러개인 함수
def students(st1,st2,st3):
    print(st1,st2,st3)
students('ed','thom','AD')
# 함수에 함수 전달하기
def english(h):
    help()
def help():
    print('도와줘')
english(help)

# 함수에서 데이터 반환받기
def st():
    name = 'AD'
    return name
st = st()
print(st)

# 함수에서 데이터 여러개 반환받기
def multi():
    return 'a','b'
a, b= multi()
result = multi()
print(result)

# 클래스
class B_school():
    def __init__(self):
        print('b대학교 초기화')
        self.school_name = 'b학교'

class A_school():
    def __init__(self):
        print('초기화 생성자')
        self.student1_name = None

        b = self.math()
        print('수학과 학생 %s' % b)

        b_school = B_school()
        print(b_school.school_name)
    def math(self):
        self.student1_name ='영수'
        name = self.student1_name

        return name
A_school()

# 클래스의 상속
class Parent():
    def __init__(self):
        print('부모')
        self.money = 50000000
    def home(self):
        return '부모의 집'
class ChildA(Parent):
    def __init__(self):
        print('자식A')

        print('부모의 돈을 물려받을 수 없습니다.')
        print('%s을 물려받았습니다.' %self.home())
class ChildB(Parent):
    def __init__(self):
        super().__init__()
        print('자식B')

        print('부모의 돈%s' %self.money)
        print('%s을 물려받았습니다.' %self.home())
ChildB()
ChildA()

# 연습 문제
'''
Kiwom 클래스와 Condition클래스가 있다.
class Kiwom()과 class Condition()

Kiwom클래스에는 __init__ 부분에 다음과 같은 딕셔너리가 있다.
{'네이버':6000, '애플':15000,'다음':3000,'넷플릭스':5000,'구글':100000,'삼성':3000,
'LG':1000, '키움':500,'호랑':8000, '셀트리온':8500, '코난':6050, '컬링':1000,'하이원':3200}

Condition 클래스에는 판매기준(def sell_filtering()) 함수가 있고, self_filtering() 함수에는 5000원 이하의 종목만
필터링 하도록 구성돼있다. Kiwoom 클래스에 있는 딕셔너리를 Condition클래스의 Filtering 함수에 보내서 5,000원이하의 종목은 어떤것들이 있는지 출력하라.
'''
class Condition():
    def sell_filtering(self, my_dict):
        for key, val in my_dict.items():
            if 5000 >= my_dict[key]:
                print('{},{}'.format(key, val))
class Kiwom():
    def __init__(self):
        self.my_dict = {'네이버':6000, '애플':15000,'다음':3000,'넷플릭스':5000,'구글':100000,'삼성':3000,
'LG':1000, '키움':500,'호랑':8000, '셀트리온':8500, '코난':6050, '컬링':1000,'하이원':3200}

        condition = Condition()
        condition.sell_filtering(self.my_dict)

Kiwom()

'''
외국인 투자자들이 빠져나가고 있다. 그래서 외국인 보유량이 많은 넥플릭스, 애플, 구글의 보유량을 반으로 줄이려고 한다.
보유량을 줄여주는 sell_filtering() 함수로 만들고, return을 사용해서 결과값을 반환받은 다음 출력하라.
'''
class Condition():
    def sell_filtering(self, my_dict):
        for key in my_dict.keys():
            if key == '넷플릭스':
                my_dict[key].update({'보유량':int(my_dict[key]['보유량']/2)})
            if key == '애플':
                my_dict[key].update({'보유량': int(my_dict[key]['보유량'] / 2)})
            elif key =='구글':
                my_dict[key].update({'보유량': int(my_dict[key]['보유량'] / 2)})
        return my_dict

class Kiwom():
    def __init__(self):
        self.my_dict = {'네이버': {'현재가':6000, '보유량':100}, '애플':{'현재가':15000, '보유량':200},'다음':{'현재가':3000, '보유량':50},
                        '넷플릭스':{'현재가':5000, '보유량':200},'구글':{'현재가':100000, '보유량':30},'삼성':{'현재가':3000, '보유량':70}}

        condition = Condition()
        result = condition.sell_filtering(self.my_dict)
        print(result)
Kiwom()