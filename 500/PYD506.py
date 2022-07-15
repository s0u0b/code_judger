def compute(a, b, c):
    def quadratic_formula(square_root_of_discriminant):
        return (-b + square_root_of_discriminant) / (2 * a)

    discriminant_ = b ** 2 - 4 * a * c
    if discriminant_ > 0:
        print(f'{quadratic_formula(discriminant_ ** 0.5)}, {quadratic_formula(-discriminant_ ** 0.5)}')
    elif discriminant_ == 0:
        print(quadratic_formula(discriminant_ ** 0.5))
    elif discriminant_ < 0:
        print('Your equation has no root.')


a_ = int(input())
b_ = int(input())
c_ = int(input())
compute(a_, b_, c_)
