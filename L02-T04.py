pii = 3.14

kokonaisluku = int(input('Anna positiivinen kokonaisluku: '))
print('Luku', kokonaisluku, 'kerrottuna itsellään on', kokonaisluku * 3)
sade = int(input('Anna ympyrän säteen pituus kokonaislukuna: '))
sade_str = str(sade)
ympyra_ala = pii * sade**2
ympyra_ala_str = str(ympyra_ala)
print('Ympyrän säde on', sade_str + ', kehä on', 2 * sade * pii, 'ja pinta-ala on ' + ympyra_ala_str + '.')
sivu1 = int(input('Anna suorakulmion yhden sivun pituus kokonaislukuna: '))
sivu2 = int(input('Anna suorakulmion toisen sivun pituus kokonaislukuna: '))

keha = 2 * (sivu1 + sivu2)
ala = sivu1 * sivu2

sivu1str = str(sivu1)
sivu2str = str(sivu2)
keha_str = str(keha)
ala_str = str(ala)

print('Suorakulmion sivut ovat', sivu1str, 'ja ' + sivu2str + '; kehä on', keha_str + '; ja pinta-ala on', ala_str + '.')
print('Kiitos ohjelman käytöstä.')