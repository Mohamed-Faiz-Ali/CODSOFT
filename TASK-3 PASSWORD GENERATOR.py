import random
import string

print('HELLO , WELCOME TO THE PASSWORD GENERATOR !!!')
length = int(input('\n ENTER THE LENGTH OF THE PASSWORD : '))
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
all = lower + upper + num 
temp = random.sample(all,length)
password = "".join(temp)
all = string.ascii_letters + string.digits + string.punctuation
passs = "".join(random.sample(all,length))
print("THE PASSWORD IS : {} ".format(password))
