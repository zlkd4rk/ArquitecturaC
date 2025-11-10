#Algoritmo
print("Si desea comprobar la conversión lo puede realizar en: https://masterplc.com/calculadora/convertir-binario-a-decimal")
decimal = int(input("Ingrese un número en decimal: "))
if decimal == 0:
    print("El número en binario es: 0")
else:
    binario = ""
    while decimal > 0:
        residuo = decimal % 2
        binario = str(residuo) + binario
        decimal = decimal // 2
    print("El número en binario es:", binario)
print("Si el número en binario no completa los 8 digitos complete con ceros a la izuierda ejemplo: 00001010")
print("Explicación: Los ceros a la izquierda no influyen ya que no aportan ningún valor al número como 00005=5 y aplica en binario")
#Colaboradores: 
#Creador del repositorio: Andrés Pesantez(zlkd4rk)
#Colaborador 1: Villacres Nicolas(villacresnicolas7-alt)
#Colaborador 2: Yumbillo Ariel(xxxxxxxxxxxxxxx)
