def osr(x=""):
    z = 0
    for zn in x:
        if zn in 'bcdfghjklmnpqrstvwxz':
            z +=1
            break
        else:
            z =0
    if z != 0:
        zn = False
        print(zn)
    else:
        zn = True
        print(zn)
osr('kukucka')
osr('aaauuu')