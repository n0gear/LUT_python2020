alaraja = int(input('Anna alueen alaraja: '))
ylaraja = int(input('Anna alueen yläraja: '))
for i in range(alaraja, ylaraja + 1):
    if (i % 5 != 0):
        print(i, 'ei ole jaollinen viidellä, hylätään.')
    elif (i % 7 != 0):
        print(i, 'ei ole jaollinen seitsemällä, hylätään.')
    else:
        print('Luku', i, 'on jaollinen 5:llä ja 7:llä.')
        break
print('Lopetetaan etsintä.')
