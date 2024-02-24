# List Comprehension
# Bu konuda listeleri üretmek ve oluşturmak için Pythonda çok pratik 
# bir yöntem olan "List Comprehension" konusunu öğreneceğiz. 
# Biliyorsunuz Pythonda birçok işimizi çok kısa kodlarla halledebiliyoruz. 
# Ancak kodları daha da kısaltmak ve pratik yöntemler kullanmak her zaman isteriz. 
# Şimdi örneklerimizle list comprehension'ı anlamaya çalışalım.


# liste = [1,2,3,4]
# liste.append(5)
# print(liste)

# liste1 = [1,2,3,4,5]
# liste2 =list()

# for i in liste1:
#     liste2.append(i)
# print(liste2)

# liste1 = [1,2,3,4,5,6]
# liste2 = [i for i in liste1]
# print(liste2)

# liste1 = [1,2,3,4,5,6]
# liste2= [i ** 2 for i in liste1]
# print(liste2)

# liste1 = [1,2,3,4,5,6]
# liste2 = [8 for i in liste1]
# print(liste2)

# liste1 = [(1,2),(3,4),(5,6)]
# liste2 = [i*j for i,j in liste1]
# print(liste2)

#liste1 = [1,2,3,4,5,6,7,8,9]
# liste2 = list()
# for i in liste1:
#     if  not (i ==3 or i ==7):
#         liste2.append(i)
# print(liste2)

# liste2 =[i for i in liste1 if not (i ==3 or i == 5)]
# print(liste2)

# a ="ogeday"
# liste =[i * 3 for i in a]
# print(liste)


liste1 = [[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]
# for i in liste1:
#     print(i)


# liste2 = list()
# for i in liste1:
#     for j in i:
#         print("j: ",j)
#         liste2.append(j)
# print(liste2)

# liste2 = [j for i in liste1 for j in i]
# print(liste2)