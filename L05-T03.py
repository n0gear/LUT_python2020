def tulostus(teksti, toistot):
    for i in range(1, toistot + 1):
        print(teksti)
    print()


teksti = ''

while(True):
    teksti = input('Anna teksti: ')
    if teksti == 'lopeta':
        print('Lopetetaan.')
        break
    toistot = int(input('Anna luku: '))
    
    tulostus(teksti, toistot)

print('Kiitos ohjelman käytöstä.')