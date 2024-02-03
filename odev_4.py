import time

#İki string'i birleştirin ve ardından bir substring arayın ve konumunu bulun.
string1 = input("İlk string'i girin: ")
string2 = input("İkinci string'i girin: ")
birlesik_string = string1 + string2
substring = input("Aranacak substring'i girin: ")
konum = birlesik_string.find(substring)

print(f"'{substring}' substring'i, birleştirilmiş string içinde {konum} indekste bulunuyor.")

time.sleep(5)