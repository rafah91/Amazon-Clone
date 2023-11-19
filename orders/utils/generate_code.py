import random

def generate_code(length=8):
    data= '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code = ''.joint(random.choice(data) for x in range(length))
    return code