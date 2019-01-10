
def checkPrime(num):
    if num==1 or num==2 or prime(num):
        return False
    else:
        return True

def prime(num):
    for i in range(3,num-1):
        if (num%i)==0:
            return True

value = input('enter the value')
print(value)

if checkPrime(value):
    print('prime')
else:
    print('not')

