luku1 = int(input('Anna ensimmäinen luku: '))
luku2 = int(input('Anna toinen luku: '))
print('Laskin osaa seuraavat toiminnot:')
print('1) Summa')
print('2) Erotus')
print('3) Tulo')
print('4) Osamäärä')
print('5) Potenssi')
print('Antamasi luvut ovat', luku1, 'ja', luku2)
valinta = int(input('Valitse toiminto (1-5): '))
if valinta == 1:
    print('Summa', luku1, '+', luku2, '=', luku1 + luku2)
elif valinta == 2:
    print('Erotus', luku1, '-', luku2, '=', luku1 - luku2)
elif valinta == 3:
    print('Tulo', luku1, '*', luku2, '=', luku1 * luku2)
elif valinta == 4:
    if luku1 == 0 or luku2 == 0:
        print('Nollalla ei voi jakaa.')
    else:
        print('Osamäärä', luku1, '/', luku2, '=', round(luku1 / luku2, 2))
elif valinta == 5:
    print('Potenssi', luku1, '**', luku2, '=', luku1 ** luku2)
else:
    print('Toimintoa ei tunnistettu.')
print('Kiitos ohjelman käytöstä.')   
