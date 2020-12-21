#one time password generator
import random
print('''Enter "BUILD" to generate a OTP''')
s=input()
if s=="BUILD" or s=="build":
    t=random.randint(0,9)*100000+random.randint(0,9)*10000+random.randint(0,9)*1000+random.randint(0,9)*100+random.randint(0,9)*10+random.randint(0,9)
    print("your one time password is ",t)
else:
    print("try again")