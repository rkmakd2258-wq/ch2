# 형변환의 종류
# 강제 형변환 : str(100) int("100")
# 자동 형변환 (묵시적 형변화)
# 컴퓨터가 계산 중에 자동으로 자료형을 바꾸는 것

print(type(4.5), type(2)) #float int
# 컴퓨터가 계산을 위해 2를 2.0으로 변환한 것
print(4.5/2) #float/int => float/float

# 타입을 확인하는 함수들
# type : 값의 정확한 타입을 확인
print(type(4.5))
# isinstance : 해당타입이 맞는지 확인
print(isinstance(4.5, float))
print(isinstance(4.5, (int, float)))