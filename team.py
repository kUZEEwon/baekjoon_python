print("★ 구구단을 출력합니다.\n")
for x in range(2, 10):
    print("------- [" + str(x) + "단] -------")
    for y in range(1, 10):
        print(x, "X", y, "=", x*y)
print("---------------------")

print("I like python")

def print_sum():
    a =100
    b= 200
    result=a+b
    print('print_sum() 내부 :',a,'과',b,'의 합은',result,'입니다')
a=10
b=20
print_sum()