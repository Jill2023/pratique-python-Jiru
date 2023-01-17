str1="  salut tout le monde  "
print(len(str1))
str2=str1.strip()
print(str2)
print(len(str2))
str3=str1.lstrip()
print(str3)
print(len(str3))

str4=str1.rstrip()
print(str4)
print(len(str4))

str5="***salut***tout***le***monde***"
str6=str5.strip("*")
print(str6)
print(len(str6))

print(str5.replace("*"," "))

str7="SALUT TOUT le monde"
print(str7.lower())
print(str7.upper())

str8="salut tout le monde le monde le monde"
print(str8.count("le monde"))
print(str8.startswith("salut"))
print(str8.endswith("monde"))

str9="un-deux-trois-quatre-cinq-six-sept-huit-neuf-dix"
print(str9.split("-"))


