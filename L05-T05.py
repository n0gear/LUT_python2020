def valikko():
    print('Käytettävissä olevat toiminnot:')
    print('1) Määritä sana')
    print('2) Tulosta sana alusta loppuun')
    print('3) Tulosta sana lopusta alkuun')
    print('0) Lopeta')
    valinta = int(input('Valintasi: '))
    return valinta

def tulosta(sana):
    pituus = len(sana)
    alku = 0
    while (alku < pituus):
        print (sana[alku::])
        #pituus = pituus - 1
        alku = alku + 1
    print()
    return None


def paaohjelma():
    while (True):
        toiminto = valikko()
        if (toiminto == 1):
            sana = input('Anna sana: ')
            print()
        elif (toiminto == 2):
            tulosta(sana)
        elif (toiminto == 3):
            sana = sana[::-1]
            tulosta(sana)
        elif (toiminto == 0):
            break
        else:
            print('Valintaa ei tunnistettu, yritä uudestaan.')
            print()
    return None

print('Tämä ohjelma tulostaa sanan käyttäjän haluamalla tavalla.')
paaohjelma()
print('Kiitos ohjelman käytöstä.')
