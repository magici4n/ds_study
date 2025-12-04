import infix_to_postfix
import stack

def postfix_cal(expression:str):
    postfix_expression = infix_to_postfix.infix_to_postfix(expression)
    result = 0
    op_stack = stack.Stack()

    for token in postfix_expression:
        if token in ('+','-','*','/'):
            if token == '+':
                a = op_stack.pop()
                b = op_stack.pop()
                result = a + b
                op_stack.push(result)
            elif token == '-':
                a = op_stack.pop()
                b = op_stack.pop()
                result = b - a
                op_stack.push(result)
            elif token == '*':
                a = op_stack.pop()
                b = op_stack.pop()
                result = a * b
                op_stack.push(result)
            else :
                a = op_stack.pop()
                b = op_stack.pop()
                result = b / a
                op_stack.push(result)
        else :
            op_stack.push(int(token))   #그냥 push하면 문자열 int()필수
    print(result)

postfix_cal("(1+2)*(3+4)")
postfix_cal("10+20/5")

