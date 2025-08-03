import stack

def parChecker(parSeq : str):
    S = stack.Stack()
    for p in parSeq:
        if p == '(':
            S.push(p)
        else:                   # p == ')'
            if S.isEmpty() :    #짝이 모자람
                return False
            else:
                S.pop()

    if S.isEmpty() :            #최종적으로 스택에 남아있는 것 확인
        return True
    else :
        return False
