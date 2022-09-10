import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'


def is_valid(check):
    if check.lower().strip() == 'да' or check.lower().strip() == 'нет':
        return True
    return False


def gen_password():
    chars = ''
    password_list = []

    if gp_digits.lower().strip() == 'да':
        chars += digits
        password_list.append(random.choice(digits))
    if gp_uppercase.lower().strip() == 'да':
        chars += uppercase_letters
        password_list.append(random.choice(uppercase_letters))
    if gp_lowercase.lower().strip() == 'да':
        chars += lowercase_letters
        password_list.append(random.choice(lowercase_letters))
    if gp_punctuation.lower().strip() == 'да':
        chars += punctuation
        password_list.append(random.choice(punctuation))

    while len(password_list) < gp_len:
        if gp_exceptions.lower().strip() == 'да':
            for i in password_list:
                if i in 'il1Lo0O':
                    password_list.remove(i)
        password_list.append(random.choice(chars))
    random.shuffle(password_list)

    new_password = ''.join(password_list)

    return new_password


while True:
    gp_quantity = input('Сколько паролей вам нужно сгенерировать?\n>>> ')
    if gp_quantity.isdigit():
        gp_quantity = int(gp_quantity)
        break
    print('Введите целое число!')
while True:
    gp_len = input('Сколько символов должно быть в вашем пароле?\n>>> ')
    if gp_len.isdigit():
        gp_len = int(gp_len)
        break
    print('Введите целое число!')
while True:
    gp_digits = input('В пароле нужны цифры от 0 до 9? (да / нет)\n>>> ')
    if is_valid(gp_digits):
        break
    print('Введите "да" или "нет"!')
while True:
    gp_uppercase = input('В пароле нужны прописные буквы? (да / нет)\n>>> ')
    if is_valid(gp_uppercase):
        break
    print('Введите "да" или "нет"!')
while True:
    gp_lowercase = input('В пароле нужны строчные буквы? (да / нет)\n>>> ')
    if is_valid(gp_lowercase):
        break
    print('Введите "да" или "нет"!')
while True:
    gp_punctuation = input('В пароле нужны символы "!#$%&*+-=?@^_"?'
                           ' (да / нет)\n>>> ')
    if is_valid(gp_punctuation):
        break
    print('Введите "да" или "нет"!')
while True:
    gp_exceptions = input('Исключать ли неоднозначные символы "il1Lo0O"?'
                          ' (да / нет)\n>>> ')
    if is_valid(gp_exceptions):
        break
    print('Введите "да" или "нет"!')


for _ in range(gp_quantity):
    print(gen_password())
