# 숫자 up&down game
import random
# game을 위한 random 숫자 생성
rn = random.randrange(1,101,1)
num = -1

t_cnt = 0 #시도 횟수
print("1~100 숫자 up&down 게임을 시작합니다!")
print("-------------------------------------")
while(rn != num):
    
    num=int(input("1부터 100사이의 숫자를 입력하세요."))
    if( num> rn):
        print("Down")
    elif(num < rn):
        print("Up")
    
    t_cnt+=1
print("----------------------------------------")
print(t_cnt,"번 만에 정답!")