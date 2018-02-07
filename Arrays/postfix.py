def  postfix_to_infix(expression):
    stack = []
    prev_op = None
    OPERATORS = ['+', '-', '*', '/', '^']
    PRIORITY = {'+':1, '-':1, '*':2, '/':2}
    for ch in expression:
        if not ch:
            continue
        if not ch in OPERATORS:
            stack.append(ch)
        else:
            b = stack.pop()
            a = stack.pop()
            if prev_op and len(a) > 1 and PRIORITY[ch] > PRIORITY[prev_op]:
                expr = '('+a+')' + ch + b
            else:
                expr = a + ch + b
            stack.append(expr)
            prev_op = ch
    print(stack[-1])
    return stack[-1]

if __name__ == "__main__":
    formula = "ab - cd +/"
    postfix_to_infix(formula)
