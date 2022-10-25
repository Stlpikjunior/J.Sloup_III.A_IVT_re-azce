def pcr(x=""):
  p = 0
  for z in range(0,10):
    y = 0
    while y<len(x):
      if str(z) in x[y]:
        p +=1
      y+= 1

  print('Pocet cislic v retazci je:',p)

pcr("na farme mame od roku 2012 12krav a 230oviec")
pcr('Hello world')
