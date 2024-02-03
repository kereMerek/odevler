import time
#Bir liste oluşturun ve listenin ortasındaki elemanı bir tuplee ekleyin.
my_liste = [1, 2, 3, 4, 5]
liste_uzunluk = len(my_liste)
orta_eleman = my_liste[liste_uzunluk // 2]
tuple_eklenen_eleman = (orta_eleman,)
print("Oluşturulan tuple:", tuple_eklenen_eleman)
time.sleep(5)
