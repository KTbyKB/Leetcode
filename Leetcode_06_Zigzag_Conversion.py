#6. Zigzag Conversion

def convert(self, s: str, numRows: int) -> str:
    res = ['']*numRows
    idx = 0
    direc = 1
    if numRows == 1 or numRows >= len(s):
        return s
    for i in s:
        res[idx] += i
        if idx == 0:
            direc = 1
        elif idx == numRows - 1:
            direc = -1
        idx += direc
    return ''.join(res)
