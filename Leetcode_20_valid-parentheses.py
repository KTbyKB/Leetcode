#20 valid-parentheses

def isValid(self, s: str) -> bool:
    if len(s) < 2:
        return False
    st = []
    for i in s:
        if i in ['(','[', '{']:
            st.append(i)
        elif st:
            if i == ')' and st.pop() != '(':
                return False
            elif i == ']' and st.pop() != '[':
                return False
            elif i == '}' and st.pop() != '{':
                return False
        else:
            return False
    if st:
        return False
    else:
        return True
