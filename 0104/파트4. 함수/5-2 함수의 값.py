def root(a, b, c):
    r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

    return r1, r2

x = 1
y = 2
z = -8

# a * x^2 + b * x + c = 0, a != 0 인 x에 관한 2차방정식에 대해,
# 근의 공식은

r1, r2 = root(x, y, z)
print('근은 {} {}'.format(r1, r2))