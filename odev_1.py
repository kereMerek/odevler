import time

#Kullanıcıdan bir cümle alın, cümlenin başındaki ve sonundaki boşlukları kaldırın, ardından tüm harfleri küçük harfe çevirin.

cumle = input("Bir cümle girin: ")
duzenlenmis_cumle = cumle.strip().lower()
print("Düzenlenmiş Cümle:", duzenlenmis_cumle)

time.sleep(5)