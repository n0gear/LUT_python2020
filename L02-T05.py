print('Tämä ohjelma laskee antamiesi 3 luvun keskiarvon.')
luku1 = int(input('Anna luku 0 ja 10 väliltä: '))
luku2 = int(input('Anna toinen luku 0 ja 10 väliltä: '))
luku3 = int(input('Anna kolmas luku 0 ja 10 väliltä: '))

summa = str(luku1 + luku2 + luku3)
keskiarvo = float((luku1 + luku2 + luku3) / 3)
keskiarvo_str = str(keskiarvo)

k_arvo_koko = int(keskiarvo)
k_arvo_koko_str = str(k_arvo_koko)

k_arvo_kolme_des = float(round(keskiarvo, 3))
k_arvo_kolme_des_str = str(k_arvo_kolme_des)

print('Antamiesi lukujen summa on', summa + '.')
print('Antamiesi lukujen keskiarvo on', keskiarvo_str + '.')
print('Keskiarvo on kokonaislukuna', k_arvo_koko_str + '.')
print('Keskiarvo pyöristettynä 3 desimaalin tarkkuuteen on', k_arvo_kolme_des_str + '.')
