import time

#Bir dict oluşturun ve dictin içindeki string türündeki değerlerin hepsini birleştirerek tek bir string elde edin.
my_dict = {'anahtar1': 'Merhaba', 'anahtar2': 'Dünya', 'anahtar3': 'Python'}
birlesik_string = ''.join(my_dict.values())
print("String değerlerin birleştirilmiş hali:", birlesik_string)
time.sleep(5)