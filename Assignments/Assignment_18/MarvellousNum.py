
def Add(No1, No2):
    Ans = 0.0
    Ans = No1 + No2
    return Ans

def Sub(No1, No2):
    Ans = 0.0
    Ans = No1 - No2
    return Ans

def Mult(No1, No2):
    Ans = 0.0
    Ans = No1 * No2
    return Ans

def Div(No1, No2):
    Ans = 0.0
    Ans = No1 / No2
    return Ans

def ChkPrime(No):
    flag = True
    NoHalf = int(No/2)

    for i in range(2, NoHalf+1):
        if(No % i == 0):
            flag = False
            break

    return flag

