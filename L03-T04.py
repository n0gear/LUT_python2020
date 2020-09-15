sana1 = input('Anna sana 1: ')
sana2 = input('Anna sana 2: ')

if (sana1 < sana2):
    print('\'' + sana1 + '\' on aakkosissa aiemmin kuin \'' + sana2 + '\'.')
elif (sana2 < sana1):
    print('\'' + sana2 + '\' on aakkosissa aiemmin kuin \'' + sana1 + '\'.')
else:
    print('Sanat ovat samoja.')
if ('z' in sana1):
    print('Kirjain \'z\' löytyy sanasta 1.')
if ('z' in sana2):
    print('Kirjain \'z\' löytyy sanasta 2.')
if ('z' not in sana1 and 'z' not in sana2):
    print('Kummastakaan sanasta ei löytynyt kirjainta \'z\'.')

sana = input('Anna testattava sana: ')

if (sana == sana[::-1]):
    print('Antamasi sana \'' + sana + '\' on palindromi.')
else: 
    print('Antamasi sana ei ole palindromi.')
    print('Se on väärinpäin \'' + sana[::-1] + '\' ja oikein päin \'' + sana + '\'.')
