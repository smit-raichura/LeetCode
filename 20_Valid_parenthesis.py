def isValid(s: str) -> bool:
    opening_parenthesis = ['(', '[', '{']
    closing_parenthesis = [')', ']', '}']
    stack = []
    for bracket in s:
        if bracket in opening_parenthesis:
            stack.append(bracket)
            print(stack)
        else:
            if len(stack) == 0:
                return False
            else:
                if bracket == ')' and '(' == stack[-1]:
                    stack.pop() 
                elif bracket == ']' and '[' == stack[-1]:
                    stack.pop()
                elif bracket == '}' and '{' == stack[-1]:
                    stack.pop()
                else:
                    stack.append(bracket)
        print(stack)
    return stack == []
        
    

# isValid(']')