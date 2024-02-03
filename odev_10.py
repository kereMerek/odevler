import time

#Kullanıcıdan bir cümle alın, cümlede geçen kelimelerin içinde en uzun olanını bulun.

cumle = input("Bir cümle girin: ")
kelimeler = cumle.split()
en_uzun_kelime = max(kelimeler, key=len)
print("Cümledeki en uzun kelime:", en_uzun_kelime)

time.sleep(5)
