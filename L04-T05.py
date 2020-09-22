alaraja = int(input('Anna alueen alaraja: '))
ylaraja = int(input('Anna alueen yläraja: '))
alkuluku = 0
luku = 0
for numero in range(alaraja, ylaraja + 1):
    if ((numero == 0) or (numero == 1)):
        print(numero, 'ei ole kelvollinen alkuluku.')
        luku = luku + 1
    else:
        for i in range(2, numero):
            if ((numero % i) == 0):
                print(numero, 'ei ole alkuluku, koska', i, '*', int(numero/i), '=', int(i * (numero/i)))
                luku = luku + 1
                break
        else:
            print(numero, 'on alkuluku.')
            viimeinen_al = numero
            alkuluku = alkuluku + 1
print('Tutkittiin', alkuluku + luku, 'lukua, joista', alkuluku, 'oli alkulukuja.')
print('Viimeinen löydetty alkuluku oli', str(viimeinen_al) + ('.'))
print('Kiitos ohjelman käytöstä.')
    