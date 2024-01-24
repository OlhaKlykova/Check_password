# param@ s - пароль для проверки
def check_password(s):
    has_upper = False
    has_lower = False
    has_num = False

    # Проверяем каждый символ в поле
    for i in s:
        if 'A' <= i <= 'Z':
            has_upper = True
        elif 'a' <= i <= 'z':
            has_lower = True
        elif '0' <= i <= '9':
            has_num = True

    # Если пароль отвечает всм четырем требованиям
    if len(s) >= 8 and has_num and has_upper and has_lower:
        return True
    # Если как минимум одно требование не соблюдено
    return False


def main():
    password = input('Введите пароль')
    if check_password(password):
        print('Пароль надежный')
    else:
        print('Пароль не надежный')


if __name__ == '__main__':
    main()