import time

#Kullanıcıdan bir cümle alın ve cümlenin içindeki kelimeleri alfabetik sıraya göre sıralayın.
cumle = input("Bir cümle girin: ")
kelimeler = cumle.split()
sirali_kelimeler = sorted(kelimeler)

print("Cümlenin içindeki kelimeler alfabetik sıraya göre şu şekildedir:")
for kelime in sirali_kelimeler:
    print(kelime)

time.sleep(15)