long = input('Anna pitkä sana: ')
print('Antamasi sanan viisi ensimmäistä kirjainta ovat', long[0:5])
print('Viisi viimeistä kirjainta ovat', long[-5:])
print('Kirjaimet 2,3,4 ja 5 ovat', long[1:5])
print()
print('Sanan joka toinen kirjain alkaen toisesta kirjaimesta:', long[1::2])
print()
print('Annoit sanan', '\'' + long + '\',', 'joka on takaperin', '\'' +
      long[::-1] + '\'.')
print()
aloitus = int(input('Anna aloituspaikka: '))
lopetus = int(input('Anna lopetuspaikka: '))
siirtyma = int(input('Anna siirtymä: '))

print('Antamillasi asetuksilla sana', long, 'tulostuu näin:',
      long[aloitus:lopetus:siirtyma])

pituus = len(long)
print()
print('Sana oli', pituus, 'merkkiä pitkä.')
