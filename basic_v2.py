# if 문
stock_price = 3000

if stock_price > 3000:
    print('통과')
elif stock_price >= 3000:
    print('통과2')
elif stock_price <= 3000:
    print('통과3')
else :
    print('조건에 해당 없음')

# 2개의 조건 비교 or / and
if stock_price < 3000 or stock_price >= 3000:
    print('둘 중 적합하면 출력')

if stock_price > 2000 and stock_price < 2500:
    print('2000-2500 사이')
elif stock_price >= 2500 and stock_price <=3000:
    print('2500-3000 사이')

# for 반복문
for i in range(5, 100):
    print(i)

    if i == 50:
        break

for i in range(0,10):
    for k in range(0,5):
        print('for 문 안에 for문 %s' %k)

# while문
stock_buy = True
count = 0
while stock_buy:
    count = count + 1

    if count == 10:
        break
        #stock_buy = False

    print(count)

'''
3일후의 주가 비교하기

카카오증권의 현재가는 1000원이며 3일동안 500원 씩 연달아 올랐다.
키움증권이 현재가는 500원이며 3일동안 1000원씩 연달아 올랐다.
3일 후의 현재가는 누가 더 높은가

 출력 문구) 키움이 더 높다.
 '''
kakao = 1000
kiwom = 500

for i in range(0,3):
    kakao += 500
    kiwom += 1000

    print(kakao, kiwom)

if kakao > kiwom :
    print('카카오가 더 높다.')
else :
    print('키움이 더 높다.')

'''
구구단 출력하기
'''
for i in range(1,10):
    print('{i}단'.format(i=i))
    for j in range(1,10):

        print('{} * {} = {}' .format(i,j,i*j))
