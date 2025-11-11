#Algoritmo: Convertir Decimal a Binario
#Colaboradores: 
#Creador del repositorio: Andrés Pesantez(zlkd4rk)/Cuenta secundaria(Gisele43)
#Colaborador 1: Villacres Nicolas Alessandro(villacresnicolas7-alt)
#Colaborador 2: Yumbillo Ariel xd(arisuuuu010)¡28
#Si desea comprobar la conversión lo puede realizar en: https://masterplc.com/calculadora/convertir-binario-a-decimal
#Los ceros a la izquierda no afectan ya que funciona similar que en el sistema decimal ejemplo: 00015=15.
decimal = int(input("Ingrese un número en decimal: "))
if decimal == 0:
    print("El número en binario es: 0")
else:
    binario = ""   #Funciona como cadena de string, por lo que ceros y unos se van agregando a la variable binario
    while decimal > 0:
        residuo = decimal % 2
        binario = str(residuo) + binario
        decimal = decimal // 2
    print("El número en binario es:", binario)
print("Complete con ceros a la izquierda para completar el octeto ejem(00001011)")
