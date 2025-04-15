print("Bienvenido a la compañia telefonica UWU, para saber si excedio su saldo ingrese los datos a continuacion")
DIA=int(input(" Ingrese el total de minutos utilizados en el DIA  "))
NOCHE=int(input(" Ingrese el total de minutos utilizados en la NOCHE  ")) #Variables que le solicito al cliente de minutos totales
if DIA<= 100:
    print ("No excede minutos en el DIA") #condicionales para saber si excede o no sus minutos
else:
    print ("Excede en ", DIA-100, "minutos en el DIA") # le resto los 100 primeros antes del cobro adicional

if NOCHE<= 80:
    print ("No excede minutos en la NOCHE")
else:
    print("Excede en", NOCHE-80, "minutos en la NOCHE")

PAGODIA=DIA*10
PAGONOCHE=NOCHE*7 # variables de cobro sin excedentes 

ADICIONALESDIA=((DIA-100)*15) # variables con el cobro adicional
ADICIONALESNOCHE=((NOCHE-80)*13)

DIAUWU=100*10 # variables con precio fijo para despues sumarle el cobro adicional , le puse ese nombre por el nombre de la empresa ficticia telefonica UWU
NOCHEUWU=80*7

if DIA<=100 and NOCHE<=80:
    print("Debe pagar", PAGODIA+PAGONOCHE) # condiciones para sacar el valor final a pagar para el cliente
elif DIA<=100 and NOCHE>80:
    print("Debe pagar", PAGODIA+(NOCHEUWU+ADICIONALESNOCHE))
elif DIA>100 and NOCHE<=80:
    print("Debe pagar", PAGONOCHE+(DIAUWU+ADICIONALESDIA))
else:
    print("Debe pagar",DIAUWU+NOCHEUWU+(ADICIONALESDIA+ADICIONALESNOCHE))
    




