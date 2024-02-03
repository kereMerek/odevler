import time

#Kullanıcıdan iki string alın, bu stringleri birleştirin ve tüm karakterleri küçük harfe çevirin.
string1 = input("Birinci stringi girin: ")
string2 = input("İkinci stringi girin: ")
birlesik_string = string1 + string2
kucuk_harf_string = birlesik_string.lower()
print("Birleştirilmiş ve küçük harfe çevrilmiş string:", kucuk_harf_string)
