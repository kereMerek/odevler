import time


#Kullanıcıdan bir kelime ve bir harf alın, kelimenin içindeki o harfi kaç kez içerdiğini kontrol edin.

kelime = input("Bir kelime girin: ")
harf = input("Sayısını bulmak istediğiniz harfi girin: ")
sayac = kelime.count(harf)


print(f"'{harf}' harfi, '{kelime}' kelimesinde {sayac} kez geçiyor.")

time.sleep(5)