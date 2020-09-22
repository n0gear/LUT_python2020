a = int(input('Anna a:n arvo: '))
b = int(input('Anna b:n arvo: '))

while (True):
    if (a <= b):
        if (a < 10000):
            if (b < 10000):
                print('a:', a, 'b:', b)
                a = a * 2
                b = b + 100
            else:
                break
        else:
            print('a:', a, 'b:', b)
            break
    else:
        print('a:', a, 'b:', b)
        break
print('Kiitos ohjelman käytöstä.')
