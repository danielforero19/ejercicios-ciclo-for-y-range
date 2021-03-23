añoInicio=int(input("Año inicial:"))
añoFin=int(input("Año final:"))
for año in range(añoInicio, añoFin+1):
   if not año%10==0:

       continue

   if not año%4==0:

       continue

   if año%100!=0 or año%400==0:

       print(año)