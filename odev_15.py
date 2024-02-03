import time
#Bir liste oluşturun, listenin ortasına yeni bir sayı ekleyin.
my_liste = [1, 2, 3, 4, 5]
liste_uzunluk = len(my_liste)
eklenen_sayi = 99
my_liste.insert(liste_uzunluk // 2, eklenen_sayi)
print("Güncellenmiş liste:", my_liste)
time.sleep(5)