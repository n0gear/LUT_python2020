def vertaaLuvut(luku1, luku2):
    # testaa kumpi luvuista on suurempi
    if (luku1 > luku2):
        print('Testatuista luvuista', luku1, 'on suurempi kuin', luku2)
        suurempi = luku1
    elif (luku2 > luku1):
        print('Testatuista luvuista', luku2, 'on suurempi kuin', luku1)
        suurempi = luku2
    else:
        print('Luvut ovat samansuuruiset.')
        suurempi = luku1
    # kerro tulos
    # palauta suurempi arvo
    # if luku1 == luku2 palauta eka ja tulosta "Luvut ovat samansuuruiset"
    return suurempi


luku1 = int(input('Anna ensimmäinen luku: '))
luku2 = int(input('Anna toinen luku: '))

suurempi = vertaaLuvut(luku1, luku2)
vahennettavaLuku = int(input('Paljonko vähennetään suuremmasta luvusta: '))
vahennysLuku = suurempi - vahennettavaLuku

if (suurempi == luku1):
    pienempi = luku2
else:
    pienempi = luku1
  
vertaaLuvut(pienempi, vahennysLuku)

print('Kiitos ohjelman käytöstä.')