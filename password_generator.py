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

    password_len = input('How many characters are needed: ')
    password_len = int(password_len)
    password = ''.join(random.choice(password_options) for i in range(password_len))
    print(password)

if __name__ == '__main__':
    main()
