lopetus = input('Haluatko lopettaa ohjelman suorittamisen (k/K): ')
if lopetus == 'k' or lopetus == 'K':
    print('Kiitos ohjelman käytöstä.')
else:
    nimi = input('Anna nimi: ')
    salasana = input('Anna salasana: ')
    if nimi == 'Matti' and salasana == 'salasana':
        print('Käyttäjä tunnistettu.')
    else:
        print('Antamasi nimi oli', len(nimi), 'merkkiä pitkä, mutta se tai salasana ei ollut oikein.')