summa = 0
lkm = 0
while (True):
    arvosana = int(input('Anna kurssiarvosana väliltä 1-5 (-1 lopettaa): '))
    if (arvosana == -1):
        break
    elif (arvosana < 1) or (arvosana > 5):
        print('Väärä syöte. Vain arvosanat 1-5 kelpaavat (-1 lopettaa).')
    else:
        summa = summa + arvosana
        lkm = lkm + 1
keskiarvo = (summa / lkm)
ka = str(round(keskiarvo, 2))
print('Arvosanojen keskiarvo on', ka + '.')