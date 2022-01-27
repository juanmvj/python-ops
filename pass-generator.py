''' 
Simple password generator in python

'''

import random


lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "_.,*^?¿'¡!·$%&/()="
numbers = "1234567890"

all = lower + upper + symbols + numbers

length = 16

password = "".join(random.sample(all,length))

print(password)