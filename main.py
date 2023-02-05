print('\n\n\n\t\t\t Bienvenidos a la Calculadora de Indice de Masa Corporal\n')


personas = int(input( "personas: "))

#Aqui verificamos que la cantidad sea mayor a 0 si no, no tiene sentido pedir nada
while personas > 0:

    n = input("Introduzca su nombre por favor: ")
    ln = input('Introduzca su apellido paterno:  ')
    mn = input('Introduzca su apell1ido materno:  ')
   #Se pide al edad que siempre es un entero por eso el int()
    e = int(input("Su edad en años por favor: "))
    #como la altura es en metros y no centimetros hay que ponerle punto y por ende es un flotante float()
    a = float(input ("Su altura en metros por favor: "))
    #Aqui se duplica codigo pero bueno... decimos que est (de estatura) es igual a altura (No me diga)
    est = a
    #La masa en kilogramos si puede tener decimales asi que la dejamos flotante
    m = float (input("Su masa en kilogramos por favor :"))
    #Calculo del IMC, masa (En kilogramos) entre la estatura (En metros) elevada al cuadrado
    IMC = m / est**2
    #Le decimos si es menor o mayor de edad, si es menor a 18 es menor, si no es mayor edad
    #Solo ruegue porque a nadie se le ocurra meter numeros negativos, le va a decir que es menor de edad
    if(e < 18):
        print(n,ln,mn)
        print("Usted es menor de edad")
    else:
        print(n,ln,mn)
        print("Usted es mayor de edad")
    #Le imprimos el IMC para que se pong
    print("Su IMC: " + str(IMC) )

    #Hacemos las distintas validaciones
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
        print ("obesidad media")
    elif IMC >= 40.00:
        print ("obesidad morbida")
    personas = personas - 1
    print(n,ln,mn,'Gracias por usar la IMC')
    input('Presione cualquier tecla para terminar')

