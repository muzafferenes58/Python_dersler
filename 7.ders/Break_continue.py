# Döngülerde kullanılan ifadeler : break ve continue
# Döngülerde kullanılabilen break ve continue ifadelerini öğrenmeye çalışacağız. 
# Bu ifadeleri kullanarak döngü yapılarını daha efektif kullanabiliriz.

# break ifadesi
# break ifadesi döngülerde programcılar tarafından en çok kullanılan ifadedir. Anlamı şu 
# şekildedir;

#         Döngü herhangi bir yerde ve herhangi bir zamanda break ifadesiyle karşılaştığı zaman
#         çalışmasını bir anda durdurur. Böylelikle döngü hiçbir koşula bağlı kalmadan 
# sonlanmış olur.
        
        
# break ifadesi sadece ve sadece içindeki bulunduğu döngüyü sonlandırır. Eğer iç içe 
# döngüler bulunuyorsa ve en içteki döngüde break kullanılmışsa sadece içteki döngü sona erer. 
# Örneklerle break ifadesini anlamaya çalışalım.

# i = 0
# while(i < 20 ):
#     print(i)
#     i +=1

# i = 0
# while(i<20):
#     print(i)
#     if i == 10:
#         break
#     i += 1


# liste = [1,2,3,4,5,6,7,8,9]
# for i in liste:
#     if i ==5:
#         break
#     print(i)

# i = 10
# while(i<20):
#     if i ==15:
#         break

#     print(i)
#     i += 1


# while True: # Sonsuz döngü. Nasıl sonlandırabiliriz ? 
#      isim = input("İsminiz(Çıkmak için q tuşuna basın.):")
#      if (isim == "q"): # break ile tabii ki.
#          print("Çıkış yapılıyor...")
#          break
#      print(isim)

# continue ifadesi
# continue ifadesi break'e göre biraz daha az kullanılan bir ifadedir. 
# Anlamı şu şekildedir; Döngü herhangi bir yerde ve herhangi bir zamanda 
# continue ifadesiyle karşılaştığı zaman geri kalan işlemlerini yapmadan 
# direk bloğunun sonuna gider. continue ifadesini anlamak için örneklerimize bakalım.

# liste = [1,2,3,4,5,6,7,8,9]
# for  i in liste:
#     if i == 3 or i ==5:
#         continue
#     print("i",i)

# liste = [1,2,3,4,5,6,7,8,9]
# for i in liste:
#      print("i: ",i)

