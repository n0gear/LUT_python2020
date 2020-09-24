def tulosta():
    print('\nNyt olemme tulosta-aliohjelmassa')
    print('Tämä aliohjelma tulostaa vain tekstiä.')
    print('Sopii hyvin valikon tulostamiseen.')

def laskutoimitus(luku):
    print('Aliohjelmassa: ' + str(luku))
    print('Aliohjelmassa luvun neliö: ' + str(luku**2))
    return None

def nimenpalautus(etunimi, sukunimi):
    kokonimi = etunimi + ' ' + sukunimi
    return kokonimi

print('Ensimmäinen vaihe:')    
tulosta()

print('\nToinen vaihe:')    
luku = int(input('Anna luku: '))
print('Päätasolla: ', str(luku))
laskutoimitus(luku)
print('Päätasolla aliohjelman jälkeen: ', str(luku))


print('\nKolmas vaihe:')
etunimi = input('Anna etunimi: ')
sukunimi = input('Anna sukunimi: ')

nimet = nimenpalautus(etunimi, sukunimi)

print('Etunimi \'' + etunimi + '\' ja sukunimi \'' + sukunimi + '\' muodostavat nimen \'' + nimet + '\'.' )

print('Kiitos ohjelman käytöstä.')
