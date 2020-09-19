aloitusarvo = int(input('Anna aloitusarvo: '))
lopetusarvo = int(input('Anna lopetusarvo: '))

# for lauseella

print('Toteutus for-lauseella:')
for i in range(aloitusarvo, lopetusarvo + 1):
    print(i, end=' ')
    i = i + 1
print()

# while lauseelle
i = aloitusarvo
print('Toteutus while-lauseella:')
while i < (lopetusarvo + 1):
    print(i, end=' ')
    i = i + 1
print()
