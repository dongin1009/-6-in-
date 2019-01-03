def print_root(a, b, c):
    r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

    print('해는 {} 또는 {}'.format(r1, r2))

x = 1
y = 2
z = -8

# a * x^2 + b * x + c = 0, a != 0 인 x에 관한 2차방정식에 대해,
# 근의 공식은

print_root(x, y, z)


x = 2
y = -6
z = -8

# 한 번 더 구하려면

print_root(x, y, z)


def print_round(number):
    rounded = round(number)
    print(rounded)

print_round(4, 6)
print_round(2, 2)
print_round(3, 6)