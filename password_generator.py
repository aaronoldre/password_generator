import random
import string

def main():
    # all letter choices
    letters = string.ascii_letters
    
    # all the digits
    digits = string.digits
    
    # all the punctuation
    punctuation = string.punctuation
    
    # concat the characters
    password_options = letters + digits + punctuation

    password_len = input_validation()
    password = ''.join(random.choice(password_options) for i in range(password_len))
    print(password)


def input_validation():
    while True:
        print('How many characters are needed: ')
        password_len = input()
        try:
            password_len = int(password_len)
        except:
            print('Please use numeric digits.')
            continue
        if password_len < 1:
            print('Please enter a positive number.')
            continue
        break
    return password_len


if __name__ == '__main__':
    main()
