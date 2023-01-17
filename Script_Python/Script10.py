str1="salut tout le monde"
print(str1[3])
print(str1[18])
print(str1[-1])
print(str1[-2])
print(len(str1))
print(str1[len(str1)-1])
#Decoupage de chanie de carateres
print(str1[0:9])
print(str1[6:10])
print(str1[6:])
print(str1[6:19])
str2="sabacada"
print(str2[1::2])
print(str1[1::2])
print(str2[1::3])
print(str1[1::3])
print(str1[:7])
print(str1[-4:])
print(str1[::-1])
str3="Jiru"
str4="Zhou"
str5=str3+" "+str4
print(str5)
print(str3,str4)

str2=str2+str2
print(str2)
for i in str2:
    print(i)
for i in enumerate(str2):
    print(i)