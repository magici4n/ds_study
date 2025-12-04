import stack

def infix_to_postfix(expression : str):
    out_stack = []
    op_stack = stack.Stack()
    expression =expression.replace(' ', '')
    for expr in expression:
        if expr == '*':
            op_stack.push(expr)
        elif expr == '/':
            op_stack.push(expr)
        elif expr == '+':
            if op_stack.isEmpty():
                op_stack.push(expr)
            else :
                while not op_stack.isEmpty():
                    tp = op_stack.top()
                    if tp == '(':
                        break
                    else:
                        out_stack.append(op_stack.pop())
                op_stack.push(expr)


        elif expr == '-':
            if op_stack.isEmpty():
                op_stack.push(expr)
            else:
                while not op_stack.isEmpty():
                    tp = op_stack.top()
                    if tp == '(':
                        break
                    else:
                        out_stack.append(op_stack.pop())
                op_stack.push(expr)
        elif expr == '(':
            op_stack.push(expr)
        elif expr == ')':
            while True:
                tp = op_stack.pop()
                if  tp == '(':
                    break
                else:
                    out_stack.append(tp)

        else :
            out_stack.append(expr)
    for _ in range(len(op_stack)):
        out_stack.append(op_stack.pop())

    print(*out_stack)
    return out_stack

