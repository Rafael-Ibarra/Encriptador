def mostrar_menu():
    print("{:^31}".format("-=[ Encriptador de Mensajes ]=-\n"))
    print("{:<}".format("1.- Encriptar Mensaje"))
    print("{:<}".format("2.- Desencriptar Mensaje"))
    print("{:<}".format("3.- Salir\n"))
    
def calcular_numeros_primos(rango_inicial, rango_final):
    numeros_primos = []
    
    for i in range(rango_inicial, (rango_final + 1)):
        veces_sin_residuo = 0
    
        for j in range(1, (i+1)):
            if ((i % (j)) == 0):
                veces_sin_residuo += 1
            
        if (veces_sin_residuo <= 2 and i != 0 and i != 1):
                numeros_primos.append(i)
    
    return numeros_primos

def digitos_primo_mayor(numeros_primos):
    digitos_primo_mayor = len(str(numeros_primos[len(numeros_primos) - 1]))
    return digitos_primo_mayor

def asignacion_letra(numeros_primos, llave):
    relacion_primo_letra = []
    abecedario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
    
    for i in range(len(abecedario)):
        relacion_primo_letra.append([numeros_primos[(llave - 1) + i], abecedario[i]])
        
    return relacion_primo_letra

def encriptar_mensaje(mensaje, numeros_primos, llave):
    relacion_primo_letra = asignacion_letra(numeros_primos, llave)
    mensaje_encriptado = []
    
    for i in range(len(mensaje)):
        if (mensaje[i] != " "):
            for j in range(len(relacion_primo_letra)):
                if mensaje[i] == relacion_primo_letra[j][1]:
                    mensaje_encriptado.append(relacion_primo_letra[j][0])
                    break
        else:
            mensaje_encriptado.append(" ")
        
    return mensaje_encriptado

def desencriptar_mensaje(mensaje_encriptado, numeros_primos, llave):
    relacion_primo_letra = asignacion_letra(numeros_primos, llave)
    digitos_mayor = digitos_primo_mayor(numeros_primos)
    mensaje_desencriptado = []
    
    #Esto aun no funciona puesto que se revisa el texto encriptado cifra por cifra
    for i in range(len(mensaje_encriptado)):
        if (mensaje_encriptado[i] != " "):
            for j in range(len(relacion_primo_letra)):
                if mensaje_encriptado[i] == relacion_primo_letra[j][0]:
                    mensaje_desencriptado.append(relacion_primo_letra[j][1])
                    break
        else:
            mensaje_desencriptado.append(" ")
            
    return mensaje_desencriptado
        
def sistema():
    mostrar_menu()
    
    res = 0
    
    while (res != 3):
        res = int(input("Seleccione una opción: "))
        if (res == 1):
            rango_inicial = int(input("Inserte un número para el inicio del rango: "))
            rango_final = int(input("Inserte un número para el final del rango: "))
        
            numeros_primos = calcular_numeros_primos(rango_inicial, rango_final)
        
            llave = int(input("Inserta un número para la llave: "))
        
            mensaje = input("Inserta un mensaje a encriptar: ")
        
            mensaje_encriptado = encriptar_mensaje(mensaje, numeros_primos, llave)
        
            print("Tu mensaje ha sido encriptado: ", *mensaje_encriptado, sep="")

        elif (res == 2):
            rango_inicial = int(input("Inserte un número para el inicio del rango: "))
            rango_final = int(input("Inserte un número para el final del rango: "))
        
            numeros_primos = calcular_numeros_primos(rango_inicial, rango_final)
        
            llave = int(input("Inserta un número para la llave: "))
            
            mensaje_encriptado = input("Inserta un mensaje a encriptar: ")
        
            mensaje_desencriptado = desencriptar_mensaje(mensaje_encriptado, numeros_primos, llave)
        
            print("Tu mensaje ha sido desencriptado: ", *mensaje_desencriptado, sep="")
        elif (res == 3):
            return "Saliendo del programa..."
        else:
            print("Opción no válida.")
            
        mostrar_menu()

if __name__ == "__main__":
    print(sistema())  