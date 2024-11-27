# Kâda valsts nolēma pâriet uz jaunu naudas sistēmu. Vecajâ sistēmā bija trîs naudas vienîbas: dâlderis, grasis, santîms. Naudas vērtîbas norâdîtas zemâk.
# 1 dâlderis = 37 graši
# 1 grasis = 162 santîmi
# Jaunajâ naudas sistçmâ paliek tikai santîmi un dâlderi. Santîms saglabâ savu vērtîbu, bet 1 dâlderis bûs vienâds ar 100 santîmiem. 
#Izveidot programmu, kas pârveidotu vecâs sistēmas naudu uz jaunu. Lietotâjam prasa ievadît vecâs sistēmas dâlderus, grašus un santîmus. Tiek aprķēinâts jaunâs sistēmas dâlderu un grašu daudzums. Rezultâts tiek parâdîts konsolē.
dalderi=int(input("Lūdzu, ievadiet dālderu skaitu: "))
grasi=int(input("Lūdzu, ievadiet grašu skaitu: "))
santims=int(input("Lūdzu, ievadiet santīmu skaitu: "))
grasi1=int(dalderi*37)
santims1=int(grasi1*162)
dalderi1=int(grasi1*162//100)
print(f"Dālderu skaits ir {dalderi1} un santīmu skaits ir {santims1}")


