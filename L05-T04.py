def kysyMerkkijono():
    merkkijono = input('Anna merkkijono, 5-15 merkkiä: ')
    return merkkijono


def tarkistaPituus(merkit):
    pituus = 0
    for m in merkit:
        pituus = pituus + 1
    return pituus


def paaohjelma():
    merkkijono = kysyMerkkijono()
    pituus = tarkistaPituus(merkkijono)
    if pituus > 4 and pituus < 16:
        print('Annoit sopivan merkkijonon,', pituus, 'merkkiä.')
    elif pituus < 5:
        print('Liian lyhyt,', pituus, 'merkkiä, anna uusi.')
        paaohjelma()
    else:
        print('Liian pitkä,', pituus, 'merkkiä, anna uusi.')
        paaohjelma() 


paaohjelma()

print('Kiitos ohjelman käytöstä.')