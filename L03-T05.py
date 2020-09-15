pituus = int(input('Anna pituus (senteissä): '))
paino = int(input('Anna paino (kilogrammoissa): '))
pituus_metreissa = pituus / 100
painoindeksi = (paino / (pituus_metreissa ** 2))

if painoindeksi < 15:
    kuvaus = '(Sairaalloinen alipaino)'
elif painoindeksi <= 15 or painoindeksi < 17:
    kuvaus = '(Merkittävä alipaino)'
elif painoindeksi <= 17 or painoindeksi < 18.5:
    kuvaus = '(Normaalia alhaisempi paino)'
elif painoindeksi <= 18.5 or painoindeksi < 25:
    kuvaus = '(Normaali paino)'
elif painoindeksi <= 25 or painoindeksi < 30:
    kuvaus = '(Lievä ylipaino)'
elif painoindeksi <= 30 or painoindeksi < 35:
    kuvaus = '(Merkittävä ylipaino)'
elif painoindeksi <= 35 or painoindeksi < 40:
    kuvaus = '(Vaikea ylipaino)'
elif painoindeksi >= 40:
    kuvaus = '(Sairaalloinen ylipaino)'

print('Painoindeksi on', round(painoindeksi, 1), kuvaus)

tavoiteindeksi = float(input('Anna tavoiteindeksi: '))
painontiputus = paino - ((pituus_metreissa * pituus_metreissa) * tavoiteindeksi)

if tavoiteindeksi < painoindeksi:
    print('Painoa tulisi tiputtaa', str(round(painontiputus, 1)), 'kilogrammaa.')
else: 
    print('Painoa tulisi kerätä', str(abs(round(painontiputus, 1))), 'kilogrammaa.')