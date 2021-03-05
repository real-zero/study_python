# tuple () 를 사용
a_list = ('키움', '카카오', '대신')
for val in a_list:
    print(val)

# list [] 를 사용
b_list = ['키움', '카카오', '대신']
for val in b_list:
    print(val)

b_list.append('대신증권')
print(b_list)

# 인덱스 번호를 이용
print((b_list[1]))

c_list = ['키움', '카카오', '대신']
print(c_list)

c_list[2] = '다음'
print(c_list)

del c_list[1]
print(c_list)

for idx, val in enumerate(c_list):
    print('인덱스:%s, 값: %s' %(idx, val))



# dictionary {} 사용
a_dict = {'키움증권':1300,'카카오증권':1500,'네이버증권':1000}
print(a_dict.get('키움증권'))
print(a_dict['키움증권'])

for key in a_dict.keys():
    print(a_dict.get(key))
# key와 value 동시에 접근
for key,val in a_dict.items():
    print('%s, %s' % (key,val))
# 딕셔너리에 데이터 추가하기
a_dict['다음증권']=2000
print(a_dict)

a_dict.update({'애플':4000})
print(a_dict)
#여러 데이터 한번에 추가하기
a_dict.update({'애플':4000,'삼성':5000,'LG':1700})
print(a_dict)

# 딕셔너리에 있는 데이터의 총합 구하기
stock_list = {'키움증권':5000,'카카오증권':3000,'네이버증권':2000}
total = 0
for val in stock_list.keys():
    total += stock_list[val]
    #total = total + stock_list[val]
    print(val ,stock_list[val])
    print(total)

# 나의 에수금으로 주식을 원하는 만큼 매수하고, 남은 금액을 확인하기
'''
{'키움증권':5000,'카카오증권':3000,'네이버증권':2000}과 예수금 111000원이있다. 
예수금을 가지고 증권사에서 원하는 만큼사라, 그리고 남은 금액을 출력하라
'''
charge = 111000
for val in stock_list.keys():
    if val == '키움증권':
        charge -= charge - stock_list[val]*3
    elif val == '카카오증권':
        charge -= charge - stock_list[val] * 3
    elif val == '네이버증권':
        charge -= charge - stock_list[val] * 3
print(charge)
# 종목이 특정 가격이 됐을 때 다른 종목 추가하기
'''
{'키움증권':5000,'카카오증권':3000,'네이버증권':2000}에서 키움증권 가격이 매일 1000원씩 올랐다.
키움증권이 10000원이 됐을때 종목하나를 더 주시하기로 했다.
키움증권이 10000원이 됐을때 딕셔너리에 이베스트증권의 현재가 5000원을 출력하고 딕셔너리를 출력해라
'''
i = True
while i :
    stock_list['키움증권'] += 1000

    if stock_list['키움증권'] == 10000:
        stock_list.update({'이베스트증권': 5000})
        break
print(stock_list)



