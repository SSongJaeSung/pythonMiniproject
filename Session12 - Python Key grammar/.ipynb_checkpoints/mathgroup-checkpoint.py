# 기능: 입력값을 받아 반올림 수행
def roundFunction2( inValue, option):
    stdVal = 0.5
    if(option==0): # round
        stdVal = 0.5
    elif(option==1): #ceil
        stdVal = 1
    elif(option==2): #floor
        stdVal = 0
    else:
        pass
    step1 = inValue * 100
    step2 = int(step1 + stdVal)
    outvalue = step2 / 100
    return outvalue


# 기능: 입력값을 받아 반올림 수행
def roundFunction( inValue, option):
    stdVal = 0.5
    if(option==0): # round
        stdVal = 0.5
    elif(option==1): #ceil
        stdVal = 1
    elif(option==2): #floor
        stdVal = 0
    else:
        pass
    step1 = inValue * 100
    step2 = int(step1 + stdVal)
    outvalue = step2 / 100
    return outvalue


