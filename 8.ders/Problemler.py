# print(range(0,20))
# liste 

# liste =list(range(0,100))
# print(liste)

# sayı = int(input("Sayı: "))
# faktoriyel = 1

# while sayı > 0 :
#     faktoriyel*= sayı
#     sayı -= 1
# print(f"Sayının faktöriyeli: {faktoriyel}")

# liste = [1, 2, 3, 4, 5]
# tek_sayilar = []
# for eleman in liste:
#     if eleman % 2 == 1:
#         tek_sayilar.append(eleman)
# print(f"Tek sayılar: {tek_sayilar}")




# liste = [1,2,3,4,5]
# toplam =0
# for i in liste:
#     toplam += 1
#     print("toplam",toplam)

# liste = [1,2,3,4,5]
# toplam = 0
# for i in liste:
#     toplam += i
# print(toplam)

# x = "merhaba"
# x += " Dünya"
# print(x)

# liste = [1,2,3]
# liste+= [4]
# print(liste)

# y = 10
# y += y
# print(y

# z = 7
# z += len("merhaba")
# print(z)

# text = ""
# for i in range(5):
#     text += str(i)
#     print(i)

# toplam = 0

# geçici_sayı = sayı 
# while geçici_sayı > 0:
#     basamak= geçici_sayı %10
#     toplam += basamak ** basamak_sayısı
#     geçici_sayı //=10
# if toplam== sayı:
#     print(sayı,"bu sayı armstrong sayısıdır")
# else:
#     print(sayı,"bu sayı armstrong sayısı değil")
    


# for i in range(1,10):
#     for j in range(1,10):
#         print(i,j,sep ='*',end =" " )
#         print("=",i*j)


# for i in range(1,11):
#     for j in range(1,11):
#         print(f"{i} x {j} = {i*j}")
#         print("******")

# i = 1
# while i <= 10:
#     print("Sayaç: ",i)
#     i += 1
    
# while True:
#     cevap = input("Devam etmek isityormusunuz E/H: ")
#     if cevap.lower == "H":
#         break
#     else:
#         print("Devam ediliyor: ")

# while True:
#     sayı = ("Pozitif sayı giriniz: ")
#     if sayı > 0:
#         break
# else:
#     print("Hatalı giriş")


# while True:
#     sayı = int(input("Pozitif sayı girin: "))
#     if sayı > 0:
#         break
#     else:
#         print("Hatalı giriş")

# for i in range(0,11):
#     for j in range(0,11):
#         print(i*j, end ="\t ")


# for x in range(5):
#     for y in range(5):
#         print(f'({x},{y})', end =" ")
#     print()

# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j, end = "\t")
#     print()
# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# for i in range(0,11):
#     for j in range(0,11):
#         print(f"{i} x {j} = {i*j}")


# for i in range(0,10):
#     if i == 5 :
#         continue
#     print(i)

# my_list = ["A","B","C","D","D","C"] 
# for item in my_list:
#     if item == "D":
#         continue
#     print(item)

# for i in range(0,10):
#     if i % 2 != 0:
#         continue
#     print(i)

# for i in range(0,101):
#     if i % 3 != 0:
#         continue
#     print(i,end =" ")

# çift_sayılar = [i for i in range(1,101) if i % 2 ==0]
# print(çift_sayılar)


# while True:
#     isim = input("isim giriniz('q'): ")
#     if isim== "q":
#         print("çıkış yapılıyor...")
#         break
#     print(isim)

# liste= [1,2,3,4,5,6,7,8,9]
# for i in liste:
#     print("i: ",i)

# for i in liste:
#     if i == 5 or i == 4:
#         continue
#     print(i)

# i = 0
# while i <10:
#     print(i)
#     i +=1


# i =0
# while i<10:
#     if i == 2:
#         i +=1
#         continue
#     print(i)
#     i +=1
# liste = list(range(0,30))
# print(liste)

# print(*range(0,100,5))

# print(*range(20,0,-1))

# for i in range(0,33,3):
#     print(i)

# for i in range(1,10):
#     print("+ "*i)

# liste= [i*3 for i in range(0,11)]
# print(liste)

# liste= [(1,2),(3,4),(5,6)]
# liste2 = [i+j for i,j in liste]
# print(liste2)

# s = "python"
# liste= [i*3 for i in s]

# print(liste)
# for i in liste:
#     print(i)

# liste = [[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]
# for i in liste:
#     print(i)

# liste = [[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]
# liste2= list()
# for i in liste:
#     for x in i:
#         liste2.append(x)
# print(liste2)


# liste= [[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]
# # liste2=[x for i in liste for x in i]
# # print(liste2)
# # print(liste[0][0])
# print(liste[1][2])

