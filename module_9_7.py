def is_prime(func):
    def primer(a, b, c):
        if check_prime(a + b + c):
            print('Простое')
            return func(a, b, c)
        else:
            print('Составное')
            return func(a, b, c)
    return primer


def check_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)