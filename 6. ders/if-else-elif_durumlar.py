# Koşullu Durumlar - if - elif - else koşullu durumları
# Önceki konumuzda koşullu durumlardaki if-else kalıplarımızı öğrendik. 
# Bu bölümde de if-elif-else kalıplarını öğrenmeye çalışacağız.

# if-elif-else Blokları
# Önceki konumuzda koşullu durumlarımızla sadece tek bir koşulu kontrol 
# edebiliyorduk. Ancak programlamada bir durum bir çok koşula bağlı olabilir. 
# Örneğin bir hesap makinesi programı yazdığımızda kullanıcının girdiği işlemlere 
# göre koşullarımızı belirleyebiliriz. Bu tür durumlar için if-elif-else kalıplarını 
# kullanırız. Kullanımı şu şekildedir;
#            if koşul: 
#                Yapılacak İşlemler
#            elif başka bir koşul:
#                Yapılacak İşlemler
#            elif başka bir koşul:
#                Yapılacak İşlemler

#                 //
#                 //
#            else:
#                Yapılacak İşlemler 
# Programlarımızda, Kaç tane koşulumuz var ise o kadar elif bloğu oluşturabiliriz. 
# Ayrıca else in yazılması zorunlu değildir. if - elif - else kalıplarında,
# hangi koşul sağlanırsa program o bloğu çalıştırır ve if-elif-blokları sona erer. 
# Şimdi isterseniz kullanıcıya işlem seçtirdiğimiz bir programla , bu kalıbı öğrenmeye 
# başlayalım.

#işlem = int(input("işlem seçiniz: "))
#if(işlem == 1):
#    print("1. işlem seçildi.")
#elif(işlem == 2):
#    print("2. işlem seçildi.")
#elif(işlem == 3):
#    print("3. işlem seçildi.")
#else:
#    print("geçersiz işlem!")
#print("enes")


# if-if-if Blokları
# Bu blokları öğrenmeden önce isterseniz öğrendiğimiz bilgilerle, 
# bir harf notu hesaplama sistemi yapalım. Daha sonra bu kalıpları anlamaya çalışalım.


#note = int(input("lütfen notunuz giriniz: "))
#if(90 <= note):
#    print("AA")
#elif(note >= 80):
#    print("BA")
#elif(note >= 70):
#    print("BB")
#else:
#    print("FF")    


### if-if-if blokları:

#note = int(input("lütfen notunuz giriniz: "))
#if(note>=90):
#    print("AA")
#if(note>=80):
#    print("BB")
#if(note>=70):
#    print("BB")
#else:
#    print("FF")       


    # Burada gördüğümüz gibi programımız beklenmedik bir şekilde çalıştı. 
# Çünkü Pythonda programlar her zaman bütün if bloklarını kontrol eder ve 
# koşullar doğruysa bu blokları çalıştırır. İşte böyle not hesaplama gibi 
# programlarda elif kullanmamızın sebebi budur.

# Koşullu durumlarımız şimdilik bu kadar ! Kurs boyunca programlarımızda 
# birçok yerde koşullu durumları kullanacağız. 