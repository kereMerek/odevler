
import time

#Bir string içinde belirli bir karakterin kaç kez geçtiğini sayın.
veri = input("Bir string girin: ")
karakter = input("Sayısını bulmak istediğiniz karakteri girin: ")
sayac = veri.count(karakter)
print(f"'{karakter}' karakteri '{veri}' stringinde {sayac} kez geçiyor.")

time.sleep(5)