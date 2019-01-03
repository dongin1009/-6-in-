
def add_10 (value):
    """value에 10을 더한 값을 돌려주는 함수"""
    if value < 10:
        return 10  # 즉시 종료
    else:
        result = value + 10
    return result

n = add_10(5)
print(n)
n = add_10(42)
print(n)

n = round(1.5)
print(n)