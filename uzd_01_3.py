# Izveidot programmu, kura prasa lietotâjam sekunþu skaitu. Sekundes tiek pârveidotas par “x hours y minutes z seconds” tipa tekstu. Rezultâts tiek parâdîts konsolç.
import math
sekundes = float(input("Lūdzu, ievadi sekunžu skaitu: "))
x= float(sekundes/3600)
y= float(sekundes/60)
z=sekundes
print (f"Sekunžu skaits ir {x} stundas, {y} minūtes un {z} sekundes")

