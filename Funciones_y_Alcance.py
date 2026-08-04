def calcular_media(numero1, numero2, numero3):
    print( (numero1 + numero2 + numero3) // 3)
calcular_media(7, 10, 9)

def aplicar_daño(vida_actual, daño):
    vida_restante = (vida_actual - daño)
    return vida_restante
nueva_vida_personaje = aplicar_daño(100, 80)

def saludo():
    print("Saludos!")
saludo()

def reaccion_del_bot(nivel_expresividad):
    def cara_del_bot():
        if nivel_expresividad > 100:
            return " Bien ^_^"
        else:
            return " Tranquilo -_-"
    expresividad_elegida = cara_del_bot()
    return "Estoy " + expresividad_elegida
print(reaccion_del_bot(120))

mensaje_usuario = "Hola Mundo!"
cantidad_letras = len(mensaje_usuario)
if cantidad_letras > 0:
    print("Tu Mensaje Tiene: " + str(cantidad_letras) + " Letras!")
else:
    print("Error el Mensaje no se a Procesado Correctamente")

def conversor_texto_numero(es_multiplo_3, es_multiplo_5):
    for numero in range(1, 101):
        if numero % 3 == 0 and numero % 5 == 0:
            print(str(es_multiplo_3) + str(es_multiplo_5) + str(numero))
        elif numero % 3 == 0:
             print(str(es_multiplo_3) + str(numero))
        elif numero % 5 == 0:
            print(str(es_multiplo_5) + str(numero))
        else:
            continue
conversor_texto_numero("Hola ", "Pepe! ")