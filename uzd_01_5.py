# Zemniekam ir govis, cûkas un vistas. Govîm un cûkâm ir pa 4 kâjâm, vistâm – 2. 
#Izveidot programmu, kas prasa lietotâjam ievadît cûku, govju un vistu skaitu. 
#Tiek aprçíinâts kopçjais kâju daudzums. Rezultâts tiek izvadîts konsolç.

cukas= int(input("Lūdzu, ievadiet cūku skaitu:"))
govis= int(input("Lūdzu, ievadiet govju skaitu:"))
vistas=int(input("Lūdzu, ievadiet vistu skaitu:"))
skaits1=int(cukas*4)
skaits2=int(govis*4)
skaits3=int(vistas*2)
kopskaits= int(skaits1+skaits2+skaits3)
print (f"Kopējais, cūku, govju un vistu kāju skaits ir {kopskaits}.")