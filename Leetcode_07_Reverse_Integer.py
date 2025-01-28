#7. Reverse Integer
def reverse(self, x: int) -> int:
    a = 0
    if x<0:
        s = -1
    else:
        s = 1
    x *= s

    while x:
        a = a * 10 + x % 10
        x //= 10

    return 0 if a < -2**31 or a > 2**31 - 1 else s * a
