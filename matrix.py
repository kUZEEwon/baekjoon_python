import numpy as np 
# 한국어 깨짐 해결
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
###########################################################################
'''
a_matrix = np.matrix([[2, 5], [1, 3], [6, 1]]) 
print(a_matrix) 
a_array = np.array([[2, 5], [1, 3], [6, 1]]) 
print(a_array)

* 행렬 생성

# matrix, array

numpy에서 행렬을 만드는 방법
1) matrix로 행렬 생성
2) array로 행렬 생성

결론적으로  numpy.matrix 는 더이상 권장되지 않으며 대신에  numpy.array 를 사용하라는 것


'''

print("\n***********************************************************\n")
#출처: https://generalbulldog.tistory.com/28 [보고의 진땀나는 하루]

# 행렬 연산
# dot(),@

a_matrix_a = np.matrix([[2, 5], [1, 3], [6, 1]]) # numpy.matrix를 사용하여 a행렬 생성 
b_matrix = np.matrix([[3], [2]]) # numpy.matrix를 사용하여 b행렬 생성 
c_matrix = a_matrix_a*b_matrix # numpy.matrix의 행렬의 곱 연산 
print(c_matrix) # 행렬의 곱 연산 결과 출력 
print(type(c_matrix)) # matrix의 type 출력

print("\n***********************************************************\n")

# numpy.array를 사용한 행렬의 곱
print("numpy.array를 사용한 행렬의 곱\n")
a_array = np.array([[2, 5], [1, 3], [6, 1]]) # numpy.array를 사용하여 a행렬 생성 
b_array = np.array([[3], [2]]) # numpy.array를 사용하여 b행렬 생성 
c_array = a_array @ b_array # numpy.array의 행렬의 곱 연산 
print(c_array) # 행렬의 곱 연산 결과 출력 
print(type(b_array)) # array의 type 출력
# numpy.array 에서 행렬의 곱을 하기 위해서는  dot() 함수나  @ 연산자

print("\n***********************************************************\n")
# 행렬식(determinant)
# np.linalg.det() ,  함수  numpy.linalg 를 사용
print("행렬식(determinant)")
d_array = np.array([[2, 5], [1, 3]]) # numpy.array를 사용하여 2x2 행렬 생성 
d_array_det = np.linalg.det(d_array) # d_array 행렬의 determinant 연산 
print(d_array_det) # determinant 연산 결과 출력


print("\n***********************************************************\n")

# 전치행렬

print("start")
d_array = np.array([[2,5],[1,3]]) # numpy.array를 사용하여 2x2 행렬 생성
print(np.transpose(d_array)) # np.transpose()를 이용한 전치행렬 출력
print(d_array.transpose()) # a.transpose()를 이용한 전치행렬 출력
print(d_array.T) # a.T를 이용한 전치행렬 출력

