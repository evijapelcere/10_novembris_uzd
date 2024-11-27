# Izveidot programmu, kura prasa lietotājam ievadît cilindra râdiusu un tâ augstumu, tiek aprēķināts cilindra laukums un tilpums. Rezultâts tiek parâdîts konsole.
# tilpums = 3.14 * rādiuss * rādiuss * augstums
# laukums = 2 * (3.14 * rādiuss * rādiuss) + augstums * (2 * 3.14 * rādiuss)
import math
augstums = float(input("Lūdzu, ievadi Cilindra augstumu: "))
radius = float(input("Lūdzu, ievadi cilindra rādiusu:"))
tilpums = (float(math.pi*radius*radius*augstums))
laukums=(float(2*math.pi*radius**2+augstums*2*math.pi*radius))
print(f"Cilindra tilpums ir {tilpums} un laukums ir {laukums}.")

