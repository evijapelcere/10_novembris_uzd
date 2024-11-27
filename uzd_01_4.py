# Izveidot kalkulatoru. Programma prasa lietotājam ievadīt divus skaitļus. Ar šiem skaitļiem tiek veiktas operācijas (saskaitīšana, atņemšana, reizināšana, dalīšana). Rezultāts tiek parādīts konsolē.

sk1=float(input('Ievadi pirmo skaitli:'))
sk2=float(input('Ievadi otro skaitli'))
summa=int(sk1+sk2)
starpiba=int(sk1-sk2)
reizinajums=int(sk1*sk2)
dalijums=int(sk1//sk2)
print(f"Pirmā skaitļa un otrā skaitļa summa ir {summa}, starpība ir {starpiba}, reizinājums ir {reizinajums}, un dalījums ir {dalijums}. ")