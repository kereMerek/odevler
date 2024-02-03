import time

#Kullanıcıdan bir kelime alın ve kelimenin içindeki tüm 'a' harflerini '@' ile değiştirin.

kelime = input("Bir kelime girin: ")

yenilenmis_kelime = kelime.replace('a', '@')

print("Değiştirilmiş kelime:", yenilenmis_kelime)

time.sleep(5)