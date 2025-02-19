#17. Letter Combinations of a Phone Number
def letterCombinations(self, digits: str) -> List[str]:
    d = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'],
             '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'],
             '8':['t','u','v'], '9':['w','x','y','z'] }
    def m(a,b):
        s = []
        for i in a:
            for j in b:
                s.append(i+j)
        return s 

    n = len(digits)
    if n == 0:
        return []
    elif n == 1:
        return d[digits]
    elif n == 2:
        a = d[digits[0]]
        b = d[digits[1]]
        return m(a,b)
    elif n ==3:
        a = d[digits[0]]
        b = d[digits[1]]
        c = m(a,b)
        e = d[digits[2]]
        return m(c,e)
    elif n ==4:
        a = d[digits[0]]
        b = d[digits[1]]
        c = m(a,b)
        e = d[digits[2]]
        f = m(c,e)
        g = d[digits[3]]
        return m(f,g)
