def parite(nombre):
    ''' Cette fonction permet de verifier la parite d'un nombre'''
    if nombre%2==0:
        print("le nombre est un pair")
    else:
        print("le nombre est une impaire")

parite(6)
parite(9)
print(parite.__doc__)