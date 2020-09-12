kokonaisluku = int(input('Anna kokonaisluku: '))

if kokonaisluku < 0:
    print('Luku on pienempi kuin 0.')
elif kokonaisluku >= 0 and kokonaisluku < 10:
    print('Luku on pienempi kuin 10.')
elif kokonaisluku >= 10:
    print('Luku on suurempi tai yhtä suuri kuin 10.')

if kokonaisluku % 2:
    print('Antamasi luku on pariton.')
else:
    print('Antamasi luku on parillinen.')
