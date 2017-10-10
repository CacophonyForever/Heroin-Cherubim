import random
def inc():
    st = random.randint(0,7)
    return str(st) + str(st+1) + str(st+2)
def dec():
    st = random.randint(2,9)
    return str(st) + str(st-1) + str(st-2)
def sandw():
    b = random.randint(0,9)
    m = random.randint(0,9)
    return str(b) + str(m) + str(b)

def easyrand():
    ret=''
    for n in range(0,3):
        t = random.randint(0,2)
        if (t==0):
           ret = ret + inc()
        if (t==1):
            ret = ret + dec()
        if (t==2):
            ret = ret + sandw()
    return ret

