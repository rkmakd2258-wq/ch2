# 형변환이 필요한 이유

# 더하기를 하기 위해서 str을 int로 변환
# 두 항의 타입이 일치하지 않으면 에러남
print(int("10") + 20) # int + int

# str -> float
print(float("3.14")+1.1) #float + float

# 100원을 만들고 싶음
# 두 항을 문자열로 만들기
print(str(100) + "원") 

