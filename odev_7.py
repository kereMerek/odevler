import time 


#Bir string içinde belirli bir alt dizeyi (substring) arayın ve yerine başka bir alt dize ekleyin.
ana_string = input("Bir string girin: ")

aranan_substring = input("Aranan alt dizeyi girin: ")

eklenecek_substring = input("Eklenecek alt dizeyi girin: ")
index = ana_string.find(aranan_substring)

if index != -1:
    yeni_string = ana_string[:index] + eklenecek_substring + ana_string[index + len(aranan_substring):]
    print("Yeni string:", yeni_string)
else:
    print("Aranan alt dize bulunamadı.")


time.sleep(5)