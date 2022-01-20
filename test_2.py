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


def Hansu(num):
    b1 = int(num/100)
    b2 = int((num-(b1*100))/10)
    b3 = int(num%10)
    #print(b1, b2, b3)
    if((b1 + b3)/2 == b2):
        return 1
    else: return 0
n = int(input())
cnt = 0

if(n<100):
    print(n)
elif(n<1000):
    for i in range(100, n+1):
        ans = Hansu(i)
        if(ans==1): 
            cnt=cnt+1
    print(99+cnt)
elif(n==1000):
    n=999
    for i in range(100, n+1):
        ans = Hansu(i)
        if(ans == 1):
            cnt=cnt+1
    print(99+cnt)
        
