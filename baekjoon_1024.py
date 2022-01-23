'''
python에서 입력값 2개 받기

예를 들어 a와 b를 받으면

# 입력받은 값을 공백을 기준으로 분리
a, b = input('문자열 두 개를 입력하세요: ').split()    
input에 split을 사용하면 
입력받은 값을 공백을 기준으로 분리

단, input().split()으로 입력받은 값은 문자열 상태
-> int를 사용하여 정수로 변환

a, b = input('숫자 두 개를 입력하세요: ').split()    
a = int(a)    # 변수를 정수로 변환한 뒤 다시 저장
b = int(b)    # 변수를 정수로 변환한 뒤 다시 저장
 
만약 매번 int로 자료형을 변환해주기 싫으면
map함수 사용

a, b = map(int, input('숫자 두 개를 입력하세요: ').split())
'''

N, L = map(int, input().split())

if L>100: print(-1)
else:
    while L <= 100:
        if (2 * N - (L * (L - 1))) % (2 * L) == 0:
            break
        else: L=L+1
    a = (2 * N - (L * (L - 1))) / (2 * L)
    if a<0 or L>100: print(-1)
    else:
        a = (2 * N - (L * (L - 1))) / (2 * L)
        for i in range(L):
            print(int(a+i), end=' ') 
            #end를 붙이면 끝에 공백을 넣으면서 한 줄로 만들어 준다.


        