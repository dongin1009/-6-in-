
# 인사 로봇
number = 20
greeting = '안녕하세요'
place = '문자열 포맷의 세계'
welcome = '환영합니다'

# old way
print(number, '번 손님', greeting, '.', place, '에 오신 것을', welcome, '!') # 이게 편할때도 있지만

base = '()번 손님, {}. {}에 오신 것을 {}!'
new_way = base.format(number, greeting, place, welcome) # 이게 더 편할때도 있다.

print(base)
print(new_way)


mine = '가위'
yours = '바위'
result = '졌다...'  # 이 코드는 만들어 봣어요

print('나는 {}, 너는 {}, 그래서 {} '.format(mine, yours, result))