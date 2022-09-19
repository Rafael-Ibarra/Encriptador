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

def digitos_primo_mayor(relacion_primo_letra):
    digitos_primo_mayor = relacion_primo_letra[len(relacion_primo_letra) - 1][0]
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
    digitos_mayor = digitos_primo_mayor(relacion_primo_letra)
    cantidad_digitos = len(str(digitos_mayor))
    mensaje_encriptado = str(mensaje_encriptado)
    mensaje_desencriptado = ""
    
    while(mensaje_encriptado != ""):
        if (mensaje_encriptado[0] == " "):
            mensaje_desencriptado += " "
            mensaje_encriptado = mensaje_encriptado[1:]
        
        if (int(mensaje_encriptado[:cantidad_digitos]) < digitos_mayor):
            for i in range(len(relacion_primo_letra)):
                if (int(mensaje_encriptado[:cantidad_digitos]) == relacion_primo_letra[i][0]):
                    mensaje_desencriptado += relacion_primo_letra[i][1]
                    if (" " in mensaje_encriptado[:cantidad_digitos] ):
                        mensaje_encriptado = mensaje_encriptado[cantidad_digitos-1:]
                    else:
                        mensaje_encriptado = mensaje_encriptado[cantidad_digitos:]
                    break
        else:
            for i in range(len(relacion_primo_letra)):
                if (int(mensaje_encriptado[:cantidad_digitos-1]) == relacion_primo_letra[i][0]):
                    mensaje_desencriptado += relacion_primo_letra[i][1]
                    mensaje_encriptado = mensaje_encriptado[cantidad_digitos-1:]
                    break
    
    return mensaje_desencriptado
        
def sistema():
    mostrar_menu()
    
    res = 0
    
    while (res != 3):
        res = int(input("Seleccione una opción: "))
        requisitos_cumplidos = False
        
        if (res == 1):
            while (not requisitos_cumplidos):
            
                rango_inicial = int(input("Inserte un número para el inicio del rango: "))
                rango_final = int(input("Inserte un número para el final del rango: "))
        
                numeros_primos = calcular_numeros_primos(rango_inicial, rango_final)
                
                if (len(numeros_primos) >= 27):
                    requisitos_cumplidos = True
                else:
                    print("\nInserte un rango lo suficiente para almacenar 27 valores...\n")
        
            llave = int(input("Inserta un número para la llave: "))
        
            mensaje = input("Inserta un mensaje a encriptar: ")
        
            mensaje_encriptado = encriptar_mensaje(mensaje, numeros_primos, llave)
        
            print("\n Tu mensaje ha sido encriptado: ", *mensaje_encriptado, "\n", sep="")

        elif (res == 2):
            while (not requisitos_cumplidos):
                rango_inicial = int(input("Inserte un número para el inicio del rango: "))
                rango_final = int(input("Inserte un número para el final del rango: "))
        
                numeros_primos = calcular_numeros_primos(rango_inicial, rango_final)
                
                if (len(numeros_primos) >= 27):
                    requisitos_cumplidos = True
                else:
                    print("\nInserte un rango lo suficiente para almacenar 27 valores...\n")
        
            llave = int(input("Inserta un número para la llave: "))
            
            mensaje_encriptado = input("Inserta un mensaje encriptado: ")
        
            mensaje_desencriptado = desencriptar_mensaje(mensaje_encriptado, numeros_primos, llave)
        
            print("\nTu mensaje ha sido desencriptado: ", mensaje_desencriptado, "\n")
        elif (res == 3):
            return "Saliendo del programa..."
        else:
            print("Opción no válida.")
            
        mostrar_menu()

if __name__ == "__main__":
    print(sistema())  