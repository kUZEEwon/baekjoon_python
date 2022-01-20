# python while 문
'''
구조
while <조건문>:
    <수행할 문장1>
    <수행할 문장2>
    <수행할 문장3>
    ...
'''

'''
treeHit = 0
while treeHit <10:
    treeHit= treeHit+1
    print("나무를 %d번 찍었습니다" % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")
'''

'''
def 함수명(매개변수):
    <수행할 문장1>
    <수행할 문장2>
    ...
'''
# 한수의 개수 구하기


def hansu(num):
    b1 = num/100
    b2 = (num-(b1*100))/10
    b3 = num%10
    
    if((b1 + b3)/2 == b2):
        print("ok")
        return 1
    else: return 0
n = int(input("1000이하의 자연수를 입력하세요="))
cnt = 0

if(n<100):
    print(n)
elif(n<1000):
    for i in range(100, n+1):
        ans = hansu(n)
        if(hansu(n)==1): 
            cnt=cnt+1
            print(cnt)
    print(99+cnt)
        
