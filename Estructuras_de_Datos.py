lista_compra = ["Pan", "Leche", "Yogur", "Arroz" ]

diccionario = {"Pepe" : 20, "Agus" : 10}

pila = [1, 2, 3, 4]
pila.append(5)
pila.append(6)
ultimo = pila.pop()
print(pila[-1])

from collections import deque
cola_impresion = deque()

cola_impresion.append("Documento_1.pdf")
cola_impresion.append("Documento_2.pdf")
cola_impresion.append("Documento_3.pdf")

print("Estado de la Cola (Llegada de datos):")
print(cola_impresion)
print("-" * 30)

print("Procesando y Eliminando de la Cola...")
documento_actual = cola_impresion.popleft()
print("Se a Impreso:", documento_actual )

print("Procesando y Eliminando de la Cola...")
documento_actual = cola_impresion.popleft()
print("Se a Impreso:", documento_actual )

print("-" * 30)
print("Estado de la Cola tras Procesar 2 Elementos:")
print(cola_impresion)

lista_compra.append("Galletas")
lista_compra.insert(5, "Fruta")
print(lista_compra)

lista_compra[3] = "Tarta"

notas_clase = {"Mateo" : 50, "Valeria" : 90, "Carlos" : 64}
print(notas_clase)
if notas_clase["Carlos"] == 64:
    print("Super Carlos 64")
    notas_clase["Carlos"] = "Que Dijiste?"
print(notas_clase)

top_gd = {"Trick" : 4, "Zlevii" : 5, "Zoink" : 1, "Netermind" : 3, "Wpopoff" : 2}
top_gd_ordenado = sorted(top_gd.items(), key = lambda jugador: jugador[1])
top_gd_final = dict(top_gd_ordenado) 
print(top_gd_final)

def agenda_contactos(agenda):
    while True:
        print("Bienvenido a la Agenda Telefonica! Que accion Realizar?")
        comando_usuario = input("E = Eliminar | A = Añadir | B = Buscar | S = Salir: ")

        if comando_usuario == "E":
            print("Contactos Actuales: ", agenda)
            contacto_borrar = input("Que Contacto Quieres Eliminar?: ")

            if contacto_borrar in agenda:
                agenda.pop(contacto_borrar)
                print("¡Se ha eliminado correctamente!")
            else:
                print("No Esta en la Lista de Contactos")
        elif comando_usuario == "A":
            contacto_añadir = input("¿Qué usuario quieres añadir?:")
            nuevo_numero = input("¿Cual es su numero de telefono?:")
            if len(nuevo_numero) > 11:
                print("Numero de Telefono Invalido")
            else:
                agenda[contacto_añadir] = nuevo_numero
                print("¡Se ha añadido correctamente!")
        elif comando_usuario == "B":
            contacto_buscar = input("¿Qué contacto quieres buscar?:")
            if contacto_buscar in agenda:
                print(f"El numero de {contacto_buscar} es: {agenda[contacto_buscar]}")
            else:
                print("No Esta en la Lista de Contactos")
        elif comando_usuario == "S":
            break
        else:
            print("Comando Invalido")
agenda = {"Pepe" : "123456789", "Agus" : "987654321"}
agenda_contactos(agenda)