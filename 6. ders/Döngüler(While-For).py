# Döngü Yapılarını Kullanma
# Şimdiye kadar yazdığımız programlarda yazdığımız programlar 
# bir defa çalışıyor ve sona eriyordu. Ancak biz çoğu zaman 
# programlarımızın belli koşullarda çalışmasını sürekli devam 
# ettirmesini ve işlemlerini tekrar etmesini isteriz. 
# İşte bunları yapmamızı sağlayan yapılara döngü diyoruz.

# Döngüler bütün programlama dillerinde bulunan ve belli 
# koşullarda işlemlerini sürekli tekrar eden yapılardır. 
# İsterseniz gerçek hayattaki programlara bakarak döngü mantığını anlamaya çalışalım.

# Örneğin , siz ATM makinesine gidip kartınızı yerleştiriyorsunuz 
# ve program başlıyor. Para Çekme, Para Yatırma , Vergileri Ödeme 
# gibi işlemleri tekrar tekrar gerçekleştiriyorsunuz. Programın 
# sona ermesi ise Kart İade seçeneği ile gerçekleşiyor. Yani siz 
# Kart İade tuşuna basmadığınız sürece ATM makinesi çalışmaya devam ediyor. 
# Buna bakarak ,aslında ATM makinesi döngü yapılarını kullanıyor diyebiliriz.

# Başka bir örnek düşünelim. Örneğin siz bir siteye login olma işlemi 
# gerçekleştiriyorsunuz. Biz kullanıcı adı ve parolayı yanlış girdiğimiz 
# sürece program sürekli bize kullanıcı adı ve parola soruyor. Programın 
# sona ermesi ise biz kullanıcı adı ve parolayı doğru girdiğimizde gerçekleşiyor. 
# Yine burada da siz döngü yapılarının kullanıldığını düşünebilirsiniz.

# Biz de artık bu bölümle birlikte Pythondaki while ve for döngülerini 
# kullanarak programlarımızı daha efektif bir şekilde yazabileceğiz.


# sonsuz dögü
#i = 0
#while(i<10):
#    print("i nin değeri: ",i)


#i =0 
#while(i<10):
#    print("i nin değeri,",i)
#    i +=1    
#print("end of the program!")

#i = 0
#while(i<=20):
#    if(i%2==0):
#        print("i nin değeri",i)
#    i += 1

#i = 0
#while(i<=40):
#    print("Python Öğreniyorum")
#    i += 1    
        
#i = 0
#liste =[1,2,3,4,5,6]
#while(i < len(liste)):
#    print("index",i, "value",liste[i])
#    i += 1

# For Döngüleri
# Bu konuda Pythondaki for döngülerinin yapısını ve for döngülerinin 
# kullanım alanlarını öğreneceğiz. Ancak ondan önce , Pythondaki in 
# operatörünü öğrenmeye çalışalım.

# in Operatörü
# Pythondaki in operatörü , bir elemanın başka bir listede,demette veya 
# stringte (karakter dizileri) bulunup bulunmadığını kontrol eder. Kullanımı şu şekildedir;


#print("a" in "merhaba")
#print("t" in "selam")

# liste = [1,2,3,4,5]
# for i in liste:
#     print("eleman",i)

# liste = [1,2,3,4,5]
# toplam = 0
# for i in liste:
#      toplam += i
# print("toplam",toplam)#

# liste = [1,2,3,4,5]
# for i in liste:
#     if i % 2 ==0:
#         print("eleman",i)

# s = "Python"
# for i in s:
#     print(i)

# s = "Python"
# for i in s:
#     print(i*3)


# demet =(1,2,3,4,5)
# for i in demet:
#     print(i)


# liste = [(1,2),(3,4),(5,6)]
# for i,j in liste:
#     print(i,j)

# liste = [(1,2,3),(4,5,6),(7,8,9)]
# for i in liste:
#      print(i)

# sözlük ={"ad":"enes","soyad":"gümüş"}
#print(sözlük.keys())
#print(sözlük.items())
#print(sözlük.values())

# for i in sözlük:
#     print(i)

# for i in sözlük.values():
#     print(i)

# for x,y in sözlük.items():
#     print(x,y)

# print(sözlük.get("ad"))

# while True:
#     isim = input("isminizi(çıkış yapmak için q ya basın)girin: ")
#     if isim == "q":
#         print("çıkış yapılıyor...")
#         break
#     print(isim)
    