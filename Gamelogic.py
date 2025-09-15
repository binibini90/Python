import random

def cust2() : 
  cust = int(input('Input your number : ')) # 사용자 가위바위보 숫자 입력받기
                                        # 에러잡기
  if cust > 3 and cust < 1: 
    print('Error Number')
  return cust


def com2() :
  com = random.randint(1,3) # 컴퓨터 램덤한 값 숫자 받기
  return com


def winable(com, cust, wincount) :
  if com == 1 and cust == 2 :               # 승패 따지기
    print('You win!!')
    wincount += 1
  elif com == 1 and cust == 3 :
    print('You lose!!')
  elif com == 2 and cust == 1 :
    print('You lose!!')
  elif com == 2 and cust == 3 :
    print('You win!!')
    wincount += 1
  elif com == 3 and cust == 1 :
    print('You win!!')
    wincount += 1
  elif com == 3 and cust == 2 :
    print('You lose!!')
  else : 
    print('Draw!!')
  return wincount




def playgame() : 

  print('This is rock VS scissors VS paper Game')
  print('Scissors is 1, Rock is 2, Paper is 3')

  rsc = ['Scissors','Rock','Paper']             # 리스트로 가위바위보 생성

  count = 0                                     # 횟수  
  wincount = 0                                  # 이긴 횟수


  for kk in range(100) :                       # 반복문으로 계속 시작(일단 100회로 제한)
    print()
    print(f'Round {count+1}') 

    cust = cust2()
    print(f'You select {rsc[cust-1]}')        # 사용자 가위바위보 보여주기
    
    com = com2()                # 컴퓨터 램덤한 값 숫자 받기
    print(f'Computer select {rsc[com-1]}')    # 컴퓨터 가위바위보 보여주기

    wincount = winable(com, cust, wincount)

    count += 1                             # 횟수 증가
    print()
    if count % 3 == 0 :                    # 3번마다 멈출지 질문
      stop = input('Do you want stop?(y/n) : ')
      if stop == 'y' or kk == 99 :                     # y이거 횟수 종료시 스탑
        print()
        print(f'Your winningrate (without Draw): {int(wincount/count * 100)}%')      #승률 따지기
        break                             # 반복문 탈출 
    else :
      continue
  