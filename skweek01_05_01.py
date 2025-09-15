num1, num2 = map(int, input('공백 기준 두개 숫자 입력').split())

calc_lists = [num1+num2, num1-num2, num1*num2, num1/num2]

print('1. 더하기', end = '\t')
print('2. 빼기', end = '\t')
print('3. 곱하기', end = '\t')
print('4. 나누기')

chice = int(input('결과:'))
print(f'결과 :  {calc_lists[chice-1]}')