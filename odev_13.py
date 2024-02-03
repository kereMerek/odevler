import time

#Bir set oluşturun, set içine bir sayı ekleyin, ardından bu sayıyı setden çıkarın.
my_set = {1, 2, 3, 4, 5}
eklenen_sayi = 6
my_set.add(eklenen_sayi)
my_set.remove(eklenen_sayi)
print("Oluşturulan set:", my_set)
time.sleep(5)