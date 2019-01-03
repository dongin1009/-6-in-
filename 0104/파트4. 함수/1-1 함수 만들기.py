def print_sqrt():
    r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

    print('해는 {} 또는 {}'.format(r1, r2))

a = 1
b = 2
c = -8

# a * x^2 + b * x + c = 0, a != 0 인 x에 관한 2차방정식에 대해,
# 근의 공식은

print_sqrt()


a = 2
b = -6
c = -8

# 한 번 더 구하려면

print_sqrt()