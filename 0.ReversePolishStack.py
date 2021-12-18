def evalRPN(tokens) -> int:
    # go through each element
    # keep last two tokens in stack, pop
    # finish until we reach end of list
    
    operations = {'+': lambda a, b: a+b,
                    '-': lambda a, b: a-b,
                    '*': lambda a, b: a*b,
                    '/': lambda a, b: int(a/b)}
    stack = []
    for token in tokens:
        if token in '+-*/':
            # Get operation function
            op = operations[token]
            if len(stack) >= 2:
                last = stack.pop()
                second_last = stack.pop()
                stack.append(op(second_last, last))
            else:
                print('Invalid operation')
        else:
            # Must be a number (postive or negative)
            stack.append(int(token))
    return stack[-1]
        
    