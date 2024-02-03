import time

#Bir dictk oluşturun, dicte yeni bir anahtar-değer çifti ekleyin, ardından bir anahtarı silin.
my_dict = {'anahtar1': 'değer1', 'anahtar2': 'değer2', 'anahtar3': 'değer3'}
eklenen_anahtar = 'anahtar4'
eklenen_deger = 'değer4'
my_dict[eklenen_anahtar] = eklenen_deger
silinecek_anahtar = 'anahtar2'
if silinecek_anahtar in my_dict:
    del my_dict[silinecek_anahtar]
    print(f"{silinecek_anahtar} anahtarı silindi.")
else:
    print(f"{silinecek_anahtar} anahtarı sözlükte bulunamadı.")
print("Oluşturulan sözlük:", my_dict)
time.sleep(5)