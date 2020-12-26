#one time password generator
import random
import time
print('''Enter "GET" to generate a OTP''')

s=input()

if s=="get" or s=="GET":

    t=random.randint(0,9)*100000+random.randint(0,9)*10000+random.randint(0,9)*1000+random.randint(0,9)*100+random.randint(0,9)*10+random.randint(0,9)

    print("Please wait for 5 seconds while the OTP is being generated \n")

    time.sleep(5)

    print("Your One Time Password is ",t," Do not share this OTP with anyone")
else:

    print("Try Again")
