print('\n\n\n\t\t\t Bienvenidos a la Calculadora de Indice de Masa Corporal\n')


personas = int(input( "personas: "))

#Aqui verificamos que la cantidad sea mayor a 0
while personas > 0:

    n = str(input("Introduzca su nombre por favor: "))
    ln = str(input('Introduzca su apellido paterno:  '))
    mn = str(input('Introduzca su apell1ido materno:  '))
   #Se pide al edad que siempre es un entero por eso el int()
    e = int(input("Su edad en años por favor: "))
    a = float(input("Su altura en metros por favor: "))
    #Aqui se duplica codigo pero bueno... decimos que est (de estatura) es igual a altura (No me diga)
    est = a
    m = float(input("Su masa en kilogramos por favor :"))
    #Calculo del IMC
    IMC = m / est**2
    if(e < 18):
        print(n,ln,mn)
        print("Usted es menor de edad")
    else:
        print(n,ln,mn)
        print("Usted es mayor de edad")
    #imprimos el IMC
    print("Su IMC: " + str(IMC) )

    #Hacemos las validaciones
    if IMC >= 0 and IMC <= 15.99 :
        print ("Delgadez severa")
    elif IMC >= 16.00 and IMC <= 16.99 :
        print ("Delgadez moderada")
    elif IMC >= 17.00 and IMC <= 18.49:
        print ("Delgadez leve")
    elif IMC >= 18.50 and IMC <= 24.99 :
        print ("Normal")
    elif IMC >= 25.00 and IMC <= 29.99:
        print ("Sobrepeso")
    elif IMC >= 30.00 and IMC <= 34.99:
        print ("obesidad leve")
    elif IMC >= 35.00 and IMC <= 39.00:
        print ("Obesidad media")
    elif IMC >= 40.00:
        print ("Obesidad morbida")
    personas = personas - 1
    print(n,ln,mn,'Gracias por usar la IMC')
    input('Presione cualquier tecla para terminar')

