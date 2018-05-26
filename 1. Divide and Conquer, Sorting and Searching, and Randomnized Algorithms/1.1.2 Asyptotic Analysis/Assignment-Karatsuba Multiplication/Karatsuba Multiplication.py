
def K_M(x, y):
    lenx = len(str(x))
    leny = len(str(7))
    if lenx==1 or leny==1:
        return x*y
    else:
        if lenx>leny:
            base = int('1'+'0'*(leny-1))
        else:
            base = int('1'+'0'*(lenx-1))
        pad = str(base)[1:]
        x1 = int(str(x)[:lenx-len(pad)])
        x2 = int(str(x)[len(pad):])
        y1 = int(str(y)[:leny-len(pad)])
        y2 = int(str(y)[len(pad):])
        x1y1 = K_M(x1, y1)
        x2y2 = K_M(x2, y2)
        rest = K_M(x1+x2, y1+y2) - x1y1 -x2y2
        return int(str(x1y1)+2*pad) +int(str(rest) +pad) + x2y2


print(K_M(3141592653589793238462643383279502884197169399375105820974944592,2718281828459045235360287471352662497557247093699959574966967627))