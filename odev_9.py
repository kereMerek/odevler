import time

#Kullanıcıdan bir kelime alın ve kelimenin palindrome (tersinden de okunduğunda aynı olan) olup olmadığını kontrol edin.

kelime = input("Bir kelime girin: ")
ters_kelime = kelime[::-1]
if kelime == ters_kelime:
    print("Girilen kelime bir palindrome'dir.")
else:
    print("Girilen kelime bir palindrome değildir.")

    time.sleep(5)