import time
#Bir dict oluşturun ve dictin içindeki string türündeki değerlerin karakter sayılarının toplamını bulun.
my_dict = {'anahtar1': 'Merhaba', 'anahtar2': 'Dünya', 'anahtar3': 'Python'}
toplam_karakter_sayisi = sum(len(deger) for deger in my_dict.values())
print("String değerlerin karakter sayılarının toplamı:", toplam_karakter_sayisi)
time.sleep(5)