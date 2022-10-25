def pnm(n: int, x=""):
    y = (len(x))
    if n < y:
        print('znak na danom mieste je: ',x[n])
    else:
        print("tento znak neexistuje")


pnm(7, "hello world")
pnm(0,'hi world')
