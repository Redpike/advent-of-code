def check(password_string):
    if 'i' in password_string or 'o' in password_string or 'l' in password_string:
        return 0
    count = 0
    flag = 0
    char = ''
    for i in range(len(password_string) - 1):
        if password_string[i] == password_string[i + 1] and password_string[i] not in char:
            count += 1
            char += password_string[i]
    for i in range(len(password_string) - 2):
        if password_string[i] == chr(ord(password_string[i + 1]) - 1) and password_string[i + 1] == chr(ord(password_string[i + 2]) - 1):
            flag = 1
    if count >= 2 and flag == 1:
        return 1
    else:
        return 0


def genenarate_next_password(password_string):
    temp = ''
    if (ord(password_string[len(password_string) - 1]) - 96) == 26:
        temp += genenarate_next_password(password_string[:len(password_string) - 1]) + 'a'
    else:
        return password_string[:len(password_string) - 1] + chr(ord(password_string[len(password_string) - 1]) + 1)
    return temp


def get_new_password(password_string):
    while True:
        password_string = genenarate_next_password(password_string)
        if check(password_string):
            break
    return password_string


def main():
    password_string = 'vzbxkghb'
    new_password = get_new_password(password_string)
    print('Day 11 Part 1:', new_password)
    print('Day 11 Part 2:', get_new_password(new_password))


if __name__ == '__main__':
    main()
