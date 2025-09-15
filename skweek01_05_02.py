

def get_data(start, end) :
  while True :
    try :
      input_str = input('입력 하쇼 : ')
      if not start <= int(input_str) <= end :
        raise ValueError('1~100 이탈')
      return int(input_str)
    except Exception as e :
      print(f'error {e}')
    else :
      return input_str


import random as rd 
start, end = 1, 100
computer = rd.randint(start, end)

counter = 0
lt = []
#게임
while True :
    humun = get_data(start, end)
    counter += 1
    if humun > computer :
        print('큼')
        lt.append(humun)
    elif humun < computer :
        print('작음')
        lt.append(humun)
    else :
        for kk in range(len(lt)) :
            print(f'{kk+1}번의 너의 정답 : {lt[kk]} , 실제 정답 : {computer}')
        print(f'{counter}번만에 정답')
        break