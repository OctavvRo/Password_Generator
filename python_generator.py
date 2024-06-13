import random
import string

def generate_password(lenght: int = 12):

    ###Create a variable that contains letters, digits and signs###
    alphabet = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(alphabet) for i in range(lenght))

    return password


password1 = generate_password()

print(password1)