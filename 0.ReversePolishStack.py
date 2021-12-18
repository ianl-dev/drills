def evalRPN(tokens) -> int:
        # go through each element
        # keep last two tokens in stack, pop
        # finish until we reach end of list
        to_eval = []
        
        for token in tokens:
            # Token is a number
            try:
                to_eval.append(int(token)) # Add to stack
            except:
                # Token is an operand
                if len(to_eval) >= 2:
                    last = to_eval.pop()
                    second_last = to_eval.pop()
                    # Perform operation
                    if token == '+':
                        result = second_last + last
                    elif token == '-':
                        result = second_last - last
                    elif token == '*':
                        result = second_last * last
                    elif token == '/':
                        result = int(second_last/last)
                    # Add back to stack
                    print(result)
                    to_eval.append(result)
        return to_eval.pop()